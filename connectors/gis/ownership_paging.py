"""Audit bounded WFS page chains without inventing a transactional snapshot."""
import hashlib
import xml.etree.ElementTree as ET
from urllib.parse import parse_qsl, urlparse, urljoin
from collections.abc import Callable

from connectors.gis.ownership_probe import normalize_sample
from connectors.gis.ownership_snapshot import _request_bbox


def request_identity(url: str) -> tuple[tuple, int, int]:
    _request_bbox(url, allow_paging=True)
    parsed = urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password or parsed.fragment:
        raise ValueError('UNSAFE_PAGE_URL')
    params = {k.lower(): v for k, v in parse_qsl(parsed.query, keep_blank_values=True)}
    start = int(params.pop('startindex', '0'))
    count = params.get('count', '')
    if not count.isascii() or not count.isdecimal() or int(count) <= 0:
        raise ValueError('EXPLICIT_POSITIVE_COUNT_REQUIRED')
    return (parsed.netloc.lower(), parsed.path, tuple(sorted(params.items()))), start, int(count)


def validated_next(raw: bytes, url: str) -> str | None:
    """Validate continuation before any network request, never follow foreign URLs."""
    identity, start, count = request_identity(url)
    normalized = normalize_sample(raw)
    returned = len(normalized['features'])
    if returned > count:
        raise ValueError('PAGE_EXCEEDS_REQUESTED_COUNT')
    link = ET.fromstring(raw).get('next')
    if not link:
        return None
    if returned == 0:
        raise ValueError('EMPTY_PAGE_WITH_CONTINUATION')
    next_url = urljoin(url, link)
    next_identity, next_start, _ = request_identity(next_url)
    if next_identity != identity or next_start != start + returned:
        raise ValueError('CHANGED_OR_NONCONTIGUOUS_NEXT_REQUEST')
    return next_url


def inspect_pages(pages: list[tuple[bytes, dict]], *, transaction_safe: bool = False) -> dict:
    """transaction_safe must come from verified capabilities; never default true.

    This audit does not grant publication rights or verify the station/buffer.
    Even a structurally complete chain remains subject to spatial validation.
    """
    if not pages:
        raise ValueError('NO_PAGES')
    base, _, _ = request_identity(pages[0][1]['url'])
    expected_start = 0
    ids, source_ids, matched_counts, observations, manifests = set(), set(), [], [], []
    next_url = None
    for index, (raw, source) in enumerate(pages):
        if not source.get('source_id') or source['source_id'] in source_ids or not source.get('retrieval_date'):
            raise ValueError('INVALID_PAGE_PROVENANCE')
        source_ids.add(source['source_id'])
        if hashlib.sha256(raw).hexdigest() != source['sha256']:
            raise ValueError('PAGE_HASH_MISMATCH')
        identity, start, _ = request_identity(source['url'])
        if identity != base or start != expected_start:
            raise ValueError('CHANGED_OR_NONCONTIGUOUS_PAGE_REQUEST')
        if index and next_url is None:
            raise ValueError('PAGE_AFTER_DECLARED_END')
        normalized = normalize_sample(raw)
        for feature in normalized['features']:
            if feature['id'] in ids:
                raise ValueError('DUPLICATE_PARCEL_ACROSS_PAGES')
            ids.add(feature['id'])
            observations.append({'parcel_id': feature['id'], 'source_id': source['source_id'],
                                 'registration_group': feature['properties']['registration_group']})
        root = ET.fromstring(raw)
        matched = root.get('numberMatched', '')
        matched_counts.append(int(matched) if matched.isascii() and matched.isdecimal() else None)
        expected_start += len(normalized['features'])
        next_url = validated_next(raw, source['url'])
        manifests.append(source)
    known = {n for n in matched_counts if n is not None}
    if len(known) > 1:
        raise ValueError('MATCHED_COUNT_CHANGED_BETWEEN_PAGES')
    reasons = []
    if next_url:
        reasons.append('PAGE_CHAIN_NOT_FINISHED')
    if None in matched_counts:
        reasons.append('MATCHED_COUNT_UNKNOWN')
    if known and next(iter(known)) != len(ids):
        reasons.append('TOTAL_COUNT_MISMATCH')
    if transaction_safe is not True:
        reasons.append('TRANSACTIONAL_SNAPSHOT_NOT_GUARANTEED')
    return {'method_version': 'ownership_page_audit_v1', 'sources': manifests,
            'page_count': len(pages), 'unique_parcel_count': len(ids),
            'number_matched_per_page': matched_counts, 'server_sequence_exhausted': next_url is None,
            'next_url': next_url, 'transaction_safe_declared': transaction_safe is True,
            'blocking_reasons': reasons, 'area_result': None, 'observations': observations,
            'status': 'BLOCKED_FOR_AREA_ANALYSIS' if reasons else 'PAGE_CHAIN_READY_FOR_SPATIAL_REVIEW',
            'limitations': ['Exhausted pages do not prove cadastral or spatial completeness.',
                            'Stable counts and unique IDs alone cannot detect every live update.']}


def fetch_page_chain(initial_url: str, *, fetch: Callable[[str], bytes],
                     archive: Callable[[str, bytes], dict], max_pages: int = 10,
                     max_records: int = 10000) -> list[tuple[bytes, dict]]:
    """Bounded orchestration. Caller supplies time-limited transport and immutable archive.

    Raw responses are archived before parsing, including malformed responses.
    No retry or partial-success disguise: errors propagate; archived evidence remains.
    """
    _, start, count = request_identity(initial_url)
    if start != 0 or type(max_pages) is not int or type(max_records) is not int or min(max_pages, max_records) <= 0:
        raise ValueError('INVALID_FETCH_LIMITS_OR_START')
    url, pages = initial_url, []
    while url:
        if len(pages) >= max_pages:
            raise ValueError('PAGE_LIMIT_REACHED')
        if len(pages) * count + count > max_records:
            raise ValueError('RECORD_REQUEST_BUDGET_REACHED')
        raw = fetch(url)
        source = archive(url, raw)
        if source.get('url') != url:
            raise ValueError('ARCHIVE_URL_MISMATCH')
        pages.append((raw, source))
        audit = inspect_pages(pages)
        url = audit['next_url']
    return pages

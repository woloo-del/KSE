"""Generate review candidates, never canonical station identities."""
from __future__ import annotations

from collections import defaultdict
import re

from connectors.gis.discovery import canonical_text


def split_station_label(label: str) -> tuple[str, tuple[int, ...]]:
    """Only a terminal explicit kV suffix is removable; retain aliases/plans."""
    match = re.fullmatch(r"(.+?)\s+(\d+(?:\s*/\s*\d+)*)\s*kV", label.strip(), re.I)
    if not match:
        return canonical_text(label), ()
    return canonical_text(match[1]), tuple(int(v.strip()) for v in match[2].split('/'))


def candidates(profiles: list[dict], stations: list[dict]) -> list[dict]:
    """Input station locator is scoped to its checksummed source snapshot."""
    index: dict[str, list[dict]] = defaultdict(list)
    locators = set()
    for station in stations:
        locator = (station['table'], station['fid'])
        if locator in locators:
            raise ValueError('DUPLICATE_SOURCE_LOCATOR')
        locators.add(locator)
        name, voltages = split_station_label(station['name'])
        index[name].append({**station, 'voltage_levels_kV': list(voltages)})
    results, ids = [], set()
    for profile in profiles:
        if profile['profile_id'] in ids:
            raise ValueError('DUPLICATE_PROFILE_ID')
        ids.add(profile['profile_id'])
        matches = index.get(canonical_text(profile['name_reported']), [])
        compatible = [s for s in matches if profile['voltage_kV'] in s['voltage_levels_kV']]
        if not matches:
            status = 'NO_EXACT_NAME_CANDIDATE'
        elif len(matches) > 1:
            status = 'AMBIGUOUS_NAME'
        elif compatible:
            status = 'SINGLE_NAME_VOLTAGE_CANDIDATE'
        elif not matches[0]['voltage_levels_kV']:
            status = 'VOLTAGE_UNKNOWN'
        else:
            status = 'VOLTAGE_NOT_LISTED'
        results.append({'profile_id': profile['profile_id'],
                        'name_reported': profile['name_reported'],
                        'voltage_kV': profile['voltage_kV'], 'review_status': status,
                        'candidates': matches, 'canonical_station_id': None,
                        'identity_confirmed': False,
                        'classification': 'INFERRED',
                        'required_review': ['PRIMARY_SOURCE_IDENTITY', 'TEMPORAL_SCOPE',
                                            'OWNERSHIP_AND_CONNECTION_VOLTAGE']})
    return results

"""Reproducible private inventory and lexical research shortlist, not a grid model."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.discovery import discover, NAME_FIELDS
from connectors.gis.geopackage import read_features
from connectors.gis.historical_capacity import capacity_observations
from connectors.gis.historical_investments import LAYERS


def build(root: Path, output: Path, query: str) -> dict:
    private = (ROOT / 'data/private').resolve()
    root, output = root.resolve(), output.resolve()
    if not root.is_relative_to(private) or not output.is_relative_to(private) or output.is_relative_to(root) or output.exists():
        raise ValueError('Use private source directory and new separate private output directory.')
    discover({}, query)
    paths = sorted(root.glob('*.gpkg'))
    if not paths:
        raise ValueError('NO_GEOPACKAGES')
    layers, candidates = [], []
    for path in paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        features, errors = read_features(path)
        if errors:
            raise ValueError('SOURCE_GEOMETRY_ERRORS')
        source = path.relative_to(private).as_posix()
        cells = 0
        for feature in features:
            observations, _ = capacity_observations(feature.properties)
            cells += len(observations)
            matches = discover(feature.properties, query)
            if matches:
                identity = json.dumps([source, digest, feature.table, feature.fid], ensure_ascii=False)
                candidates.append({'candidate_id': hashlib.sha256(identity.encode()).hexdigest(),
                    'source_file': source, 'source_sha256': digest, 'source_table': feature.table,
                    'source_fid': feature.fid,
                    'name': next((feature.properties[k] for k in NAME_FIELDS if feature.properties.get(k)), None),
                    'matches': matches, 'geometry_type': feature.geometry.geom_type,
                    'source_srs_id': feature.srs_id, 'canonical_asset_id': None,
                    'electrical_relationship': 'UNKNOWN', 'current_capacity_MW': None})
        layers.append({'source_file': source, 'source_sha256': digest,
                       'records': len(features), 'geometry_types': dict(Counter(f.geometry.geom_type for f in features)),
                       'role': 'HISTORICAL_INVESTMENT_OR_SPATIAL_PLAN' if path.stem in LAYERS else 'HISTORICAL_STATION_INVENTORY',
                       'capacity_source_cells': cells})
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('SOURCE_CHANGED')
    result = {'method': 'gis_usefulness_discovery_v1', 'access': 'PRIVATE',
              'retrieval_date': datetime.now(timezone.utc).isoformat(), 'query': query,
              'summary': {'layers': len(layers), 'source_records': sum(x['records'] for x in layers),
                          'lexical_candidate_records': len(candidates),
                          'unique_grid_assets': None, 'confirmed_electrical_relationships': 0},
              'layers': layers, 'candidates': candidates,
              'limitations': ['Name mentions and group membership are research leads, not electrical edges.',
                             'Inventory and investment records may describe the same asset; not deduplicated.',
                             'A historical capacity cell is not a current station capacity measurement.',
                             'No engineering accuracy or completeness of the underlying dataset is asserted.']}
    lines = ['# Co wnoszą przekazane dane GIS', '',
             'Prywatny przegląd kompilacji; stan 2024 zadeklarowany przez użytkownika, nie aktualny model sieci.', '',
             '## Przydatność', '',
             '- Lokalizacje stacji: punkt wyjścia do mapy i wyszukania obiektów do weryfikacji.',
             '- Nazwy, kody i operatorzy: kandydaci do łączenia wpisów z dokumentami; bez automatycznego scalania.',
             '- Grupy mocy: kontekst publikacji operatora, nie dowód połączenia linią lub wspólnego transformatora.',
             '- Historyczne pola MW: punkt odniesienia po weryfikacji dat, kierunku i zakresu; nie bieżąca rezerwa.',
             '- Warstwy inwestycji: tropy zmian sieci i źródła do dalszego sprawdzania.',
             '- Warstwy liniowe dotyczą zadań inwestycyjnych; nie tworzą pełnego grafu istniejącej sieci.', '',
             '## Zakres plików', '', '| Warstwa | Rekordy | Geometrie | Komórki mocy |', '|---|---:|---|---:|']
    lines.extend(f"| {Path(x['source_file']).stem} | {x['records']} | {x['geometry_types']} | {x['capacity_source_cells']} |" for x in layers)
    lines += ['', '## Tropy dla zapytania: ' + query, '',
              'Lista poniżej to dopasowania tekstowe. Nie jest listą przyłączonych stacji lub projektów.', '']
    for record in candidates:
        lines.append(f"- {record['name'] or 'Wpis zadania'} — {record['source_file']}, fid {record['source_fid']}; "
                     + ', '.join(m['match_kind'] + ': ' + m['source_field'] for m in record['matches']))
    lines += ['', '## Czego nadal nie wiemy', '',
              'Aktualnych obciążeń, pełnego pipeline PV/BESS/wiatru i wniosków bez odpowiedzi, '
              'połączeń feeder–GPZ, układu szyn, impedancji, granic własności oraz aktualnej rezerwy importowej i eksportowej. '
              'Bliskość na mapie ani grupa publikacyjna nie uzupełniają tych braków.', '',
              'Szczegóły proweniencji: usefulness.json. Pochodzenie i prawa do szerszego wykorzystania: NEED-012.', '']
    output.mkdir(parents=True)
    (output / 'usefulness.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf8', newline='\n')
    (output / 'review.md').write_text('\n'.join(lines), encoding='utf8', newline='\n')
    print(json.dumps(result['summary']))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--query', required=True)
    args = parser.parse_args()
    build(args.root, args.output, args.query)

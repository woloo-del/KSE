"""Render a private progress comparison from preserved results; no coordinates exported."""
import json
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    directory = ROOT / 'data/private/reviews/wegrowo_land_2026-10-06'
    before = json.loads((directory / 'land_diagnostic.json').read_text(encoding='utf8'))
    now = json.loads((directory / 'land_diagnostic_two_counties.json').read_text(encoding='utf8'))
    labels = json.loads((ROOT / 'data/reference/registration_group_labels.json').read_text(encoding='utf8'))
    for value in (before, now):
        if value['access'] != 'PRIVATE' or value['method_version'] != 'registration_group_buffer_v1':
            raise ValueError('UNEXPECTED_RESULT')
    if before['center'] != now['center'] or before['radius_m'] != now['radius_m']:
        raise ValueError('INCOMPARABLE_BUFFERS')
    data = {key: {'count': len(value['parcel_observations']), 'coverage': value['geometric_coverage']['percent_of_buffer']}
            for key, value in [('before', before), ('now', now)]}
    data.update(overlap=now['unknown_components']['overlap']['area_m2'], gap=now['unknown_components']['missing_geometry']['area_m2'],
                groups=[{'code': str(i), 'label': labels['labels'][str(i)], 'ha': now['groups'][str(i)]['area_ha'],
                         'percent': now['groups'][str(i)]['percent_of_buffer']} for i in range(1, 17)],
                sources=[{'label': 'GUGiK — działki miasta Grudziądz', 'url': now['sources']['COUNTY_EXPORT_GRUDZIADZ_GPKG']['locator']},
                         {'label': 'GUGiK — działki powiatu grudziądzkiego', 'url': now['sources']['COUNTY_EXPORT_GRUDZIADZ_RURAL_GPKG']['locator']},
                         {'label': 'EGiB — znaczenie grup rejestrowych', 'url': 'https://eli.gov.pl/eli/DU/2024/219/ogl'}])
    template = (ROOT / 'scripts/templates/land_progress.html').read_text(encoding='utf8')
    encoded = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(template.replace('__LAND_DATA__', encoded), encoding='utf8')
    print('Private progress comparison generated.')


if __name__ == '__main__':
    main()

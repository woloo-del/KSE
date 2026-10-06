"""Create a readable PRIVATE review from preserved spatial results and dated labels."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def describe(result: dict, dictionary: dict) -> str:
    if result.get('method_version') != 'registration_group_buffer_v1':
        raise ValueError('UNSUPPORTED_AREA_METHOD')
    if result.get('access') != 'PRIVATE' or result.get('ownership_binary_split') is not None:
        raise ValueError('UNEXPECTED_SCOPE')
    expected = {str(i) for i in range(1, 17)}
    if (dictionary.get('schema_version') != 'registration_group_labels_v1'
            or set(dictionary['labels']) != expected or set(result['groups']) != expected):
        raise ValueError('GROUP_DICTIONARY_MISMATCH')
    lines = ['# Węgrowo — prywatna kontrola struktury grup rejestrowych', '',
             'Lokalizacja: historyczny kandydat z GIS użytkownika, nadal niezweryfikowany.',
             'To zestawienie powierzchni geometrii działek w buforze, nie udziałów praw własności.', '',
             f"Metoda: {result['method_version']}; promień: {result['radius_m']} m; CRS: {result['crs']}.",
             f"Słownik: {dictionary['schema_version']}, sprawdzony {dictionary['verified_at']}.", '',
             '| Grupa | Opis skrócony | ha w buforze | % całego bufora |',
             '|---|---|---:|---:|']
    for code in sorted(expected, key=int):
        area = result['groups'][code]
        lines.append(f"| {code} | {dictionary['labels'][code]} | {area['area_ha']:.2f} | {area['percent_of_buffer']:.2f} |")
    unknown = result['unknown_total']
    lines.extend(['', f"Nierozstrzygnięte: {unknown['area_m2']:.3f} m². Wartości tabeli zaokrąglono; dokładne wyniki zachowano w JSON.", '',
                  *['- ' + warning for warning in dictionary['warnings']], '',
                  'Nie ustalono praw komercyjnej redystrybucji danych paczek. Nie opublikowano tego wyniku w aplikacji.', '',
                  '## Pochodzenie', '', dictionary['basis'], ''])
    for source in dictionary['sources']:
        lines.append(f"- {source['source_id']}: {source['url']} (SHA-256: {source['sha256']})")
    for source_id, source in result['sources'].items():
        lines.append(f"- {source_id}: {source['locator']} (pobranie: {source['retrieval_date']}; SHA-256: {source['sha256']})")
    return '\n'.join(lines) + '\n'


def main() -> None:
    directory = ROOT / 'data/private/reviews/wegrowo_land_2026-10-06'
    input_path = directory / 'land_diagnostic_two_counties.json'
    dictionary_path = ROOT / 'data/reference/registration_group_labels.json'
    raw, labels = input_path.read_bytes(), dictionary_path.read_bytes()
    text = describe(json.loads(raw), json.loads(labels))
    text += f"\nSHA-256 wyniku: {hashlib.sha256(raw).hexdigest()}\n\nSHA-256 słownika: {hashlib.sha256(labels).hexdigest()}\n"
    output = directory / 'land_groups_review_v1.md'
    if output.exists() and output.read_text(encoding='utf8') != text:
        raise ValueError('REFUSE_OVERWRITE_DIFFERENT_REVIEW')
    output.write_text(text, encoding='utf8')
    print('Private review created; no public export.')


if __name__ == '__main__':
    main()

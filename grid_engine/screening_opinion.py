"""Explainable evidence screening, not a calibrated connection probability."""
from decimal import Decimal, InvalidOperation

METHOD = 'documentary_screening_v2'
TECHNOLOGIES = {'BESS', 'PV', 'WIND', 'PV+BESS', 'WIND+BESS', 'PV+WIND+BESS'}


def assess(project: dict, pipeline: dict, investment_review: dict | None = None) -> dict:
    allowed = {'technology', 'voltage_kV', 'export_MW', 'import_MW', 'energy_MWh'}
    if set(project) - allowed or not isinstance(project.get('technology'), str) or project['technology'] not in TECHNOLOGIES:
        raise ValueError('Nieprawidłowy typ projektu lub pola wejściowe.')
    if type(project.get('voltage_kV')) is not int or project['voltage_kV'] not in (110, 220):
        raise ValueError('Pilot obsługuje Radkowice 110 lub 220 kV.')
    normalized = {k: project[k] for k in ('technology', 'voltage_kV')}
    for key in ('export_MW', 'import_MW', 'energy_MWh'):
        value = project.get(key)
        if value in (None, ''):
            normalized[key] = None
            continue
        if isinstance(value, bool):
            raise ValueError('Moc i pojemność muszą być liczbami.')
        try:
            number = Decimal(str(value))
        except InvalidOperation as exc:
            raise ValueError('Nieprawidłowa liczba.') from exc
        if not number.is_finite() or number < 0:
            raise ValueError('Moc i pojemność muszą być nieujemne i skończone.')
        normalized[key] = str(number)
    findings = [{
        'id': 'NO_ELECTRICAL_MODEL', 'kind': 'Brak danych',
        'text': 'Brakuje aktualnej topologii ruchowej, obciążeń i pełnych parametrów elektrycznych. Nie można wyznaczyć rezerwy MW ani sprawdzić N-1.',
        'basis': ['docs/02_feasibility_matrix.md'],
    }, {
        'id': 'PARTIAL_INVENTORY', 'kind': 'Ryzyko informacyjne',
        'text': 'Publiczny wykaz obejmuje znaną część pipeline. Nie potwierdza wszystkich projektów, ich realizacji ani zajętości mostu.',
        'basis': ['PSE_PIPELINE', 'docs/gpz_pipeline.md'],
    }]
    if normalized['voltage_kV'] == 220:
        findings.append({
            'id': 'DOCUMENTED_AGREEMENTS', 'kind': 'Potwierdzony punkt odniesienia',
            'text': f"W próbce PSE z {pipeline['source_date']} są {len(pipeline['records'])} wpisy projektów dla Radkowic 220 kV. Ich umowy uzasadniają dalsze badanie tego punktu, lecz nie dowodzą możliwości przyłączenia kolejnego projektu.",
            'basis': ['PSE_PIPELINE'],
        })
    else:
        findings.append({
            'id': 'NO_110_PIPELINE', 'kind': 'Brak danych',
            'text': 'Zestawienia projektów 220 kV nie przenosimy na 110 kV. Dane PGE wymagają uzupełnienia; nie ma porównywalnego zestawienia dla wybranego poziomu.',
            'basis': ['NEED-011', 'docs/12_radkowice_110kv_research.md'],
        })
    if investment_review is not None and investment_review['status']=='UNRESOLVED_DATE_OR_SCOPE':
        years=sorted({claim['completion_year_reported'] for claim in investment_review['claims']})
        findings.append({
            'id':'INVESTMENT_DATE_OR_SCOPE_UNRESOLVED','kind':'Rozbieżność źródeł',
            'text':f"Publikacje PSE podają różne lata zakończenia wymiany transformatora w Radkowicach: {', '.join(map(str,years))}. Trzeba wyjaśnić zakres i datę odbioru. Nie wynika z tego dodatkowa dostępna moc ani parametr transformatora.",
            'basis':[claim['source_id'] for claim in investment_review['claims']],
        })
    directions = []
    for field, title in [('export_MW', 'Oddawanie do sieci'), ('import_MW', 'Pobór z sieci')]:
        value = normalized[field]
        directions.append({'direction': title, 'requested_MW': value, 'available_MW': None,
                           'conclusion': 'Brak wartości wejściowej' if value is None else
                           ('Nie zadeklarowano mocy w tym kierunku' if Decimal(value) == 0 else
                            'Wymaga potwierdzenia operatora; brak udokumentowanej rezerwy dla tego scenariusza')})
    return {'method': METHOD, 'classification': 'INFERRED', 'project': normalized,
            'verdict': 'Wymaga dalszej weryfikacji',
            'explanation': 'Istnieją dowody pozwalające rozpocząć analizę lokalizacji, ale dostępne dane nie rozstrzygają technicznej możliwości przyłączenia tego projektu.',
            'data_confidence': 'Ograniczona — niepełne pokrycie i brak danych operacyjnych',
            'score': None, 'probability': None, 'findings': findings, 'directions': directions,
            'next_steps': ['Potwierdzić punkt i poziom napięcia z operatorem.',
                           'Pozyskać aktualny schemat, parametry wspólnego przyłącza i status jego realizacji.',
                           'Ustalić warunki importu oraz eksportu dla zadanych limitów PCC.'],
            'assumptions': ['Podane MW są maksymalnymi mocami na PCC, nie sumą mocy urządzeń.',
                            'Parametry użytkownika nie zmieniają danych źródłowych.',
                            'Brak rankingu stacji i kalibracji liczbowego scoringu.',
                            'Technologia i MWh stanowią kontekst; nie obliczamy profili pracy ani wpływu pojemności na ograniczenia.']}

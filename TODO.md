# TODO — Grid Connection Intelligence

Aktualizacja rejestru: **2026-09-17**. Źródło edytowalne: [todo.json](data/project/todo.json).

Widok generowany. Aktualizujemy JSON, zachowując ID, historię Git i dowody zakończenia. Nie ustalono terminów dla niezaplanowanych zadań. P0 = warunek najbliższego etapu, P1 = rozwój po fundamentach, P2 = dalszy rozwój. Priorytety są kolejnością organizacji pracy, nie scoringiem sieci.

## Najbliższe zadania bez nieukończonych zależności

- **KSE-009 — Zweryfikować dostęp do publikacji PGE** (P0, Zagrożone). 16.09 ponownie otrzymano HTML zamiast dwóch PDF. Konkretna pomoc zapisana jako NEED-011; nadal bez danych mocy PGE w modelu.
- **KSE-010 — Ustalić prawa źródeł wybranych do pilota** (P0, Do zrobienia). Sprawdzić podstawę wykorzystania XLSX PSE, portalu inwestycji i BIP Chęcin dla pilota Radkowic.
- **KSE-030 — Potwierdzić zewnętrzną kopię archiwum** (P0, Do zrobienia). Zachować sześć ZIP wymienionych w docs/reproducibility.md na niezależnym prywatnym nośniku i sprawdzić je z właściwymi manifestami przez --verify-only. Potwierdzić datę kopii.
- **KSE-033 — Prywatne obserwacje i wspólna infrastruktura przyłączeniowa** (P0, W toku). Uwzględnić prywatny przegląd schematów i etapów, rozstrzygnąć rewizje oraz przypisania pól (NEED-013). Nie przenosić relacji projektowych do bieżącego modelu bez dowodu wykonania.
- **KSE-011 — Przetestować uwierzytelnione API ENTSO-E** (P1, Do zrobienia). W odrębnym kroku wykonać małe zapytanie z lokalnym poświadczeniem, bez logowania tokenu.
- **KSE-012 — Potwierdzić eksport ENEA i TAURON** (P1, Do zrobienia). Sprawdzić dokumentowane pliki/API portali i dopuszczalny sposób pobierania.
- **KSE-036 — Weryfikacja i normalizacja historycznej warstwy GIS** (P1, W toku). Weryfikować pierwotne publikacje i legendy, w tym kolejkę linków z rejestru inwestycji; rozstrzygnąć powiązania, rozbieżności eksportów i prawa wykorzystania. Historyczne rekordy nie stanowią aktualnej bazy infrastruktury.

## Pełny rejestr

| ID | Zadanie | Etap | Status | Priorytet | Zależności |
|---|---|---|---|---|---|
| KSE-001 | Research źródeł i granic dokładności | Research | Zrobione | P0 | — |
| KSE-002 | Katalog i kontrola próbek źródłowych | Research | Zrobione | P0 | KSE-001 |
| KSE-003 | Git i odtwarzanie snapshotów | Organizacja | Zrobione | P0 | — |
| KSE-004 | Wykluczenie lokalnych sekretów z Git | Organizacja | Zrobione | P0 | — |
| KSE-005 | Specyfikacja pipeline wybranego GPZ | Produkt | Zrobione | P0 | KSE-001 |
| KSE-006 | TODO i generator pełnego raportu Excel | Organizacja | Zrobione | P0 | KSE-002 |
| KSE-007 | Ustalić zakres i kryteria MVP | Produkt | Zrobione | P0 | KSE-001, KSE-005 |
| KSE-008 | Wyjaśnić konflikt dat Energi | Dane | Zrobione | P0 | KSE-002 |
| KSE-009 | Zweryfikować dostęp do publikacji PGE | Dane | Zagrożone | P0 | KSE-002 |
| KSE-010 | Ustalić prawa źródeł wybranych do pilota | Dane | Do zrobienia | P0 | KSE-007 |
| KSE-011 | Przetestować uwierzytelnione API ENTSO-E | Dane | Do zrobienia | P1 | KSE-004 |
| KSE-012 | Potwierdzić eksport ENEA i TAURON | Dane | Do zrobienia | P1 | KSE-002 |
| KSE-013 | Wybrać stację i obszar pilota | Produkt | W toku | P0 | KSE-007, KSE-010 |
| KSE-014 | Zaprojektować model i architekturę pilota | Model | Do zrobienia | P0 | KSE-013 |
| KSE-015 | Connector pipeline PSE XLSX | Connectory | Do zrobienia | P0 | KSE-014, KSE-010 |
| KSE-016 | Connector dokumentów OSD pilota | Connectory | Do zrobienia | P0 | KSE-014, KSE-010 |
| KSE-017 | Canonical ID i deduplikacja projektów | Model | Do zrobienia | P0 | KSE-015, KSE-016 |
| KSE-018 | Graf referencyjny pilota | Topologia | Do zrobienia | P0 | KSE-017 |
| KSE-019 | BIP i inwestycje w obszarze pilota | Dane | Do zrobienia | P1 | KSE-013, KSE-010 |
| KSE-020 | Warstwy GIS i kontrola CRS | GIS | Do zrobienia | P1 | KSE-013, KSE-010 |
| KSE-021 | Zestawienie projektów A/B/C dla GPZ | Analityka | Do zrobienia | P0 | KSE-017, KSE-018 |
| KSE-022 | Screening BESS i hybryd z PCC | Analityka | Do zrobienia | P0 | KSE-021 |
| KSE-023 | Walidacja pilota na niezależnych dowodach | Walidacja | Do zrobienia | P0 | KSE-022 |
| KSE-024 | Pierwszy interfejs i mapa dowodów | UI | Do zrobienia | P1 | KSE-023 |
| KSE-025 | Cykliczne aktualizacje i historia zmian | V1 | Do zrobienia | P1 | KSE-015, KSE-016, KSE-023 |
| KSE-026 | Rozszerzenie pokrycia OSD i regionów | V1 | Do zrobienia | P2 | KSE-023, KSE-025 |
| KSE-027 | Scenariusze przyszłej sieci i trasy | V2 | Do zrobienia | P2 | KSE-019, KSE-020, KSE-023 |
| KSE-028 | Metodologia confidence i scoringu | V2 | Do zrobienia | P2 | KSE-023, KSE-026 |
| KSE-029 | Dane techniczne i model rozpływowy | Long-term | Do zrobienia | P2 | KSE-023 |
| KSE-030 | Potwierdzić zewnętrzną kopię archiwum | Organizacja | Do zrobienia | P0 | KSE-003 |
| KSE-031 | Eksperymentalny graf dowodów Radkowic | Model | Zrobione | P0 | KSE-002, KSE-007 |
| KSE-032 | Rozszerzenie dowodów 110 kV i przegląd materiału użytkownika | Research | Zrobione | P0 | KSE-031 |
| KSE-033 | Prywatne obserwacje i wspólna infrastruktura przyłączeniowa | Model | W toku | P0 | KSE-032 |
| KSE-034 | Lokalna aplikacja pilotażowa — ocena przesłanek Radkowic | MVP UI | Zrobione | P0 | KSE-032 |
| KSE-035 | Pierwszy prywatny przegląd pakietu mostu i historycznego GIS | Research | Zrobione | P0 | KSE-032 |
| KSE-036 | Weryfikacja i normalizacja historycznej warstwy GIS | Data quality | W toku | P1 | KSE-035 |
| KSE-037 | Rozbieżności dat inwestycji PSE w ocenie pilota | Data quality | Zrobione | P0 | KSE-034 |
| KSE-038 | Historyczny rejestr wpisów o inwestycjach z GIS | Data quality | Zrobione | P1 | KSE-035 |
| KSE-039 | Projekt PRSP po konsultacjach: dowody inwestycji w pilocie | Data quality | Zrobione | P1 | KSE-034 |
| KSE-040 | Audyt przydatności GIS i rzeczywistej próbki OSM Radkowic | Data quality | Zrobione | P1 | — |

## Kryteria zakończenia i dowody

### KSE-001 — Research źródeł i granic dokładności

- Odpowiedzialność: Codex.
- Następny krok: Uzupełniać badanie po nowych ustaleniach.
- Kryterium: Raport odpowiada osobno dla SN, 110 i 220/400 kV; zawiera źródła i niewiadome.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-10.
- Dowody/kontekst: [docs/01_data_research.md](docs/01_data_research.md).

### KSE-002 — Katalog i kontrola próbek źródłowych

- Odpowiedzialność: Codex.
- Następny krok: Zachować historię kolejnych publikacji.
- Kryterium: Rejestr źródeł, status dostępu, daty, hashe próbek i raport kontroli są zapisane.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-10.
- Dowody/kontekst: [data/catalog/data_sources.json](data/catalog/data_sources.json), [data/catalog/research_validation.json](data/catalog/research_validation.json).

### KSE-003 — Git i odtwarzanie snapshotów

- Odpowiedzialność: Codex.
- Następny krok: Utrzymywać pary ZIP–manifest. 16.09 sprawdzono odtwarzanie sześciu archiwów (42 elementy), wybór manifestu i kontrolę bez zapisu; kopia zewnętrzna osobno w KSE-030.
- Kryterium: Lokalna historia Git i archiwum z hashami; test odtworzenia przechodzi. Nie oznacza wykonania zewnętrznej kopii.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-10.
- Dowody/kontekst: [docs/reproducibility.md](docs/reproducibility.md), [scripts/research_archive.py](scripts/research_archive.py), [tests/test_research_archive.py](tests/test_research_archive.py).

### KSE-004 — Wykluczenie lokalnych sekretów z Git

- Odpowiedzialność: Codex.
- Następny krok: Utrzymać wykluczenie w raportach i backupach źródeł.
- Kryterium: _secrets nie jest śledzony ani automatycznie odczytywany przez generatory.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-10.
- Dowody/kontekst: [.gitignore](.gitignore).

### KSE-005 — Specyfikacja pipeline wybranego GPZ

- Odpowiedzialność: Codex.
- Następny krok: Przenieść reguły do modelu i testów pilota.
- Kryterium: Grupy przyłączone / planowane / oczekujące, status nieznany, deduplikacja i kierunki są opisane.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-10.
- Dowody/kontekst: [docs/gpz_pipeline.md](docs/gpz_pipeline.md).

### KSE-006 — TODO i generator pełnego raportu Excel

- Odpowiedzialność: Codex.
- Następny krok: Aktualizować rejestr po wykonanych pracach i generować raport po ważnych zmianach.
- Kryterium: TODO ma stabilne ID i zależności; skrypt tworzy szczegółowy XLSX z bieżących plików bez sekretów; testy przechodzą.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-11.
- Dowody/kontekst: [scripts/generate_project_report.ps1](scripts/generate_project_report.ps1), [scripts/validate_project_report.py](scripts/validate_project_report.py), [tests/test_report_data.mjs](tests/test_report_data.mjs), [docs/project_reporting.md](docs/project_reporting.md).

### KSE-007 — Ustalić zakres i kryteria MVP

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Realizować pilot dokumentacyjny Radkowic według zapisanych kryteriów; rozszerzenia uzgadniać osobno.
- Kryterium: Zapisany zakres pilota, mierzalne kryteria odbioru i wyłączenia bez obietnicy nieuzasadnionych MW/probability.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-11.
- Dowody/kontekst: [docs/02_feasibility_matrix.md](docs/02_feasibility_matrix.md), [docs/08_roadmap.md](docs/08_roadmap.md), [docs/09_pilot_scope.md](docs/09_pilot_scope.md).

### KSE-008 — Wyjaśnić konflikt dat Energi

- Odpowiedzialność: Codex.
- Następny krok: Utrzymać kwarantannę do uzyskania spójnej publikacji lub wyjaśnienia operatora.
- Kryterium: Udokumentowane rozstrzygnięcie lub kwarantanna konfliktowej daty, bez nadpisania źródła.
- Nieukończone zależności: brak.
- Ryzyko: Konflikt dat pozostaje nierozstrzygnięty; ukończono kontrolę i kwarantannę..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-11.
- Dowody/kontekst: [docs/07_data_quality.md](docs/07_data_quality.md), [connectors/energa/date_quality.py](connectors/energa/date_quality.py), [tests/test_energa_date_quality.py](tests/test_energa_date_quality.py), [data/catalog/energa_date_review_2026-09-11.json](data/catalog/energa_date_review_2026-09-11.json).

### KSE-009 — Zweryfikować dostęp do publikacji PGE

- Odpowiedzialność: Codex.
- Następny krok: 16.09 ponownie otrzymano HTML zamiast dwóch PDF. Konkretna pomoc zapisana jako NEED-011; nadal bez danych mocy PGE w modelu.
- Kryterium: Odczytana próbka z datą i prawami albo udokumentowane utrzymanie blokady.
- Nieukończone zależności: brak.
- Ryzyko: HTTP 200 zwracał stronę odrzucenia zamiast danych..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/discovery_log.md](docs/discovery_log.md), [data/catalog/pge_radkowice_access_2026-09-11.json](data/catalog/pge_radkowice_access_2026-09-11.json).

### KSE-010 — Ustalić prawa źródeł wybranych do pilota

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Sprawdzić podstawę wykorzystania XLSX PSE, portalu inwestycji i BIP Chęcin dla pilota Radkowic.
- Kryterium: Każde źródło pilota ma rozstrzygniętą podstawę użycia lub jest wyłączone. Kontakt z operatorem wymaga zlecenia użytkownika.
- Nieukończone zależności: brak.
- Ryzyko: Publiczny dostęp nie rozstrzyga komercyjnego wykorzystania; zastrzeżenia Stoen..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/01_data_research.md](docs/01_data_research.md).

### KSE-011 — Przetestować uwierzytelnione API ENTSO-E

- Odpowiedzialność: Codex.
- Następny krok: W odrębnym kroku wykonać małe zapytanie z lokalnym poświadczeniem, bez logowania tokenu.
- Kryterium: Próbka XML i opis zakresu, dat, limitów i praw; żadnych sekretów w URL manifestu, logach ani Git.
- Nieukończone zależności: brak.
- Ryzyko: Dostarczenie klucza nie jest dowodem jego działania; test jeszcze niewykonany..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/01_data_research.md](docs/01_data_research.md).

### KSE-012 — Potwierdzić eksport ENEA i TAURON

- Odpowiedzialność: Codex.
- Następny krok: Sprawdzić dokumentowane pliki/API portali i dopuszczalny sposób pobierania.
- Kryterium: Mała poprawna próbka z trwałego kanału lub jawny brak potwierdzonego eksportu.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/discovery_log.md](docs/discovery_log.md).

### KSE-013 — Wybrać stację i obszar pilota

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Potwierdzić granice PSE/PGE i prawa źródeł; relacja 110 kV Radkowice–Wolica ma dowód administracyjny.
- Kryterium: Rzeczywisty GPZ, udokumentowane powiązania, projekty i inwestycje; wybór uzasadniony dowodami.
- Nieukończone zależności: KSE-010.
- Ryzyko: Brak potwierdzonych granic własności i kompletnego pipeline PGE; prawa źródeł nadal otwarte..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/08_roadmap.md](docs/08_roadmap.md), [docs/10_radkowice_pilot.md](docs/10_radkowice_pilot.md), [data/reference/radkowice_pse_projects_2026-07-31.json](data/reference/radkowice_pse_projects_2026-07-31.json), [docs/11_radkowice_evidence_model.md](docs/11_radkowice_evidence_model.md), [docs/12_radkowice_110kv_research.md](docs/12_radkowice_110kv_research.md).

### KSE-014 — Zaprojektować model i architekturę pilota

- Odpowiedzialność: Codex.
- Następny krok: Uszczegółowić obserwacje, wnioski, projekty, grupy mocy, historię i relacje.
- Kryterium: Schemat, kontrakty walidacji i decyzja architektury; BESS/PCC, statusy i daty rozdzielone.
- Nieukończone zależności: KSE-013.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/03_system_architecture.md](docs/03_system_architecture.md), [docs/04_data_model.md](docs/04_data_model.md).

### KSE-015 — Connector pipeline PSE XLSX

- Odpowiedzialność: Codex.
- Następny krok: Wdrożyć fetch/parse/normalize/validate/store na rzeczywistych próbkach.
- Kryterium: Testy nagłówków, jednostek, dat, braków i zmian formatu; każdy rekord wskazuje arkusz/wiersz i snapshot.
- Nieukończone zależności: KSE-014, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [data/catalog/data_sources.json](data/catalog/data_sources.json).

### KSE-016 — Connector dokumentów OSD pilota

- Odpowiedzialność: Codex.
- Następny krok: Wybrać właściwe publikacje importu, eksportu i pipeline.
- Kryterium: Poprawny odczyt tabel i scenariuszy; konflikty dat i nieznane wartości nie trafiają po cichu do agregacji.
- Nieukończone zależności: KSE-014, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/07_data_quality.md](docs/07_data_quality.md).

### KSE-017 — Canonical ID i deduplikacja projektów

- Odpowiedzialność: Codex.
- Następny krok: Rozdzielić inwestycję, wniosek i historię etapów; sprawdzać operatora, napięcie i aliasy.
- Kryterium: Przypadki wielu wniosków i nazw nie podwajają projektów; niejednoznaczne dopasowania pozostają jawne.
- Nieukończone zależności: KSE-015, KSE-016.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/gpz_pipeline.md](docs/gpz_pipeline.md).

### KSE-018 — Graf referencyjny pilota

- Odpowiedzialność: Codex.
- Następny krok: Połączyć udokumentowane stacje, linie, transformację i projekty.
- Kryterium: Każda krawędź ma dowód, czas i pewność; brak sztucznego domykania grafu po odległości.
- Nieukończone zależności: KSE-017.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/04_data_model.md](docs/04_data_model.md).

### KSE-019 — BIP i inwestycje w obszarze pilota

- Odpowiedzialność: Codex.
- Następny krok: Sprawdzić aktualne rejestry właściwych organów i dokumenty planów operatorów.
- Kryterium: Źródła z datami i prawami; etap administracyjny nie jest automatycznie WP ani budową.
- Nieukończone zależności: KSE-013, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/discovery_log.md](docs/discovery_log.md).

### KSE-020 — Warstwy GIS i kontrola CRS

- Odpowiedzialność: Codex.
- Następny krok: Rozpocząć od zachowanej próbki OSM Radkowic: normalizacja geometrii, ID, CRS, dat i atrybucji; relacje elektryczne pozostają odrębne. Patrz docs/08_roadmap.md.
- Kryterium: GetFeature/pakiety sprawdzone, poprawne CRS i geometrie; prawa i daty zachowane.
- Nieukończone zależności: KSE-013, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/01_data_research.md](docs/01_data_research.md).

### KSE-021 — Zestawienie projektów A/B/C dla GPZ

- Odpowiedzialność: Codex.
- Następny krok: Powiązać znane projekty z kartą stacji na podstawie dowodów; pokazać niepełne pokrycie operacyjnych, planowanych i oczekujących, bez zamiany braków na zero.
- Kryterium: Potwierdzone przyłączenie, plan i oczekiwanie odróżnione; deduplikacja i kierunkowe sumy z pokryciem.
- Nieukończone zależności: KSE-017, KSE-018.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/gpz_pipeline.md](docs/gpz_pipeline.md), [scripts/build_radkowice_pipeline.py](scripts/build_radkowice_pipeline.py), [tests/test_radkowice_pipeline.py](tests/test_radkowice_pipeline.py), [data/reference/radkowice_pipeline_view_2026-07-31_v1.json](data/reference/radkowice_pipeline_view_2026-07-31_v1.json).

### KSE-022 — Screening BESS i hybryd z PCC

- Odpowiedzialność: Codex.
- Następny krok: Połączyć parametry projektu z faktami, ograniczeniami i niewiadomymi.
- Kryterium: Ładowanie/rozładowanie osobno; limity PCC zachowane; brak arbitralnej rezerwy MW i score.
- Nieukończone zależności: KSE-021.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/05_grid_capacity_methodology.md](docs/05_grid_capacity_methodology.md).

### KSE-023 — Walidacja pilota na niezależnych dowodach

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Przygotować próbę referencyjną projektów i relacji oraz kryteria porównania.
- Kryterium: Oddzielnie zmierzona poprawność ekstrakcji, dopasowań, pokrycia i wniosków; błędy opisane.
- Nieukończone zależności: KSE-022.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/07_data_quality.md](docs/07_data_quality.md).

### KSE-024 — Pierwszy interfejs i mapa dowodów

- Odpowiedzialność: Codex.
- Następny krok: Po walidacji geometrii dodać mapę dowodów do istniejącej aplikacji: źródła i status relacji, bez awansu przecięć do połączeń.
- Kryterium: Mapa z tekstowymi dowodami, datami i niewiadomymi; testy podstawowej ścieżki użytkownika.
- Nieukończone zależności: KSE-023.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/08_roadmap.md](docs/08_roadmap.md).

### KSE-025 — Cykliczne aktualizacje i historia zmian

- Odpowiedzialność: Codex.
- Następny krok: Zaprojektować harmonogram, cache, limity, korekty i powiadomienia.
- Kryterium: Zmiana źródła wykrywana, historia zachowana, błąd parsera zatrzymuje promocję danych.
- Nieukończone zależności: KSE-015, KSE-016, KSE-023.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/03_system_architecture.md](docs/03_system_architecture.md).

### KSE-026 — Rozszerzenie pokrycia OSD i regionów

- Odpowiedzialność: Codex.
- Następny krok: Powtórzyć proces walidacji dla następnego operatora i regionu.
- Kryterium: Każdy nowy obszar ma jawny zakres i miary pokrycia; brak deklaracji kompletności kraju.
- Nieukończone zależności: KSE-023, KSE-025.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/08_roadmap.md](docs/08_roadmap.md).

### KSE-027 — Scenariusze przyszłej sieci i trasy

- Odpowiedzialność: Codex.
- Następny krok: Rozwijać scenariusze udokumentowanych inwestycji i terminów; nie przypisywać automatycznego przyrostu MW. Trasy wymagają osobnej warstwy ograniczeń.
- Kryterium: Plany oddzielone od obecnej infrastruktury; zakresy i założenia uzasadnione danymi.
- Nieukończone zależności: KSE-019, KSE-020, KSE-023.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/05_grid_capacity_methodology.md](docs/05_grid_capacity_methodology.md).

### KSE-028 — Metodologia confidence i scoringu

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Zdefiniować cel wskaźnika i zbiór kalibracyjny przed wagami.
- Kryterium: Odrębne score/confidence, wyjaśnienia, walidacja; bez danych kalibracyjnych wynik pozostaje UNKNOWN.
- Nieukończone zależności: KSE-023, KSE-026.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/06_scoring_methodology.md](docs/06_scoring_methodology.md).

### KSE-029 — Dane techniczne i model rozpływowy

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Ekspertyza wpływu nie będzie dostępna od użytkownika w tym pilocie. Oceniać inne źródła parametrów; nie uzależniać ewidencji i modelu dokumentacyjnego od power-flow.
- Kryterium: Kompletne wymagane wejścia i niezależna walidacja; w przeciwnym razie dokumentacja niewykonalności.
- Nieukończone zależności: KSE-023.
- Ryzyko: Publiczne dane mogą nie wystarczyć; brak gwarancji osiągalności etapu..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/05_grid_capacity_methodology.md](docs/05_grid_capacity_methodology.md).

### KSE-030 — Potwierdzić zewnętrzną kopię archiwum

- Odpowiedzialność: Użytkownik.
- Następny krok: Zachować sześć ZIP wymienionych w docs/reproducibility.md na niezależnym prywatnym nośniku i sprawdzić je z właściwymi manifestami przez --verify-only. Potwierdzić datę kopii.
- Kryterium: Istnieje niezależna kopia archiwum zgodna z manifestem. Sam lokalny ZIP i push nie spełniają warunku.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/reproducibility.md](docs/reproducibility.md).

### KSE-031 — Eksperymentalny graf dowodów Radkowic

- Odpowiedzialność: Codex.
- Następny krok: Wykorzystać doświadczenia w pełnym modelu pilota; uzupełniać tylko udokumentowane relacje.
- Kryterium: Odtwarzalny graf źródłowy z testami, niepełnym pokryciem i jawnymi niewiadomymi; nie zastępuje KSE-014 ani KSE-018.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-11.
- Dowody/kontekst: [docs/11_radkowice_evidence_model.md](docs/11_radkowice_evidence_model.md), [scripts/build_radkowice_graph.py](scripts/build_radkowice_graph.py), [grid_engine/evidence_graph.py](grid_engine/evidence_graph.py), [tests/test_evidence_graph.py](tests/test_evidence_graph.py), [data/reference/radkowice_evidence_graph_v1.json](data/reference/radkowice_evidence_graph_v1.json).

### KSE-032 — Rozszerzenie dowodów 110 kV i przegląd materiału użytkownika

- Odpowiedzialność: Codex.
- Następny krok: Rozwinąć integrację prywatnych obserwacji osobno; nadal sprawdzać aktualny stan sieci.
- Kryterium: Publiczny dowód z zachowanym snapshotem i grafem v2; prywatny przegląd z proweniencją poza ogólnym eksportem.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-11.
- Dowody/kontekst: [docs/12_radkowice_110kv_research.md](docs/12_radkowice_110kv_research.md), [docs/private_sources.md](docs/private_sources.md), [tests/test_wolica_evidence.py](tests/test_wolica_evidence.py).

### KSE-033 — Prywatne obserwacje i wspólna infrastruktura przyłączeniowa

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Uwzględnić prywatny przegląd schematów i etapów, rozstrzygnąć rewizje oraz przypisania pól (NEED-013). Nie przenosić relacji projektowych do bieżącego modelu bez dowodu wykonania.
- Kryterium: Źródła prywatne i pochodne wyniki dziedziczą dostęp; miejsca nie są MW; konflikty danych i status planowany pozostają jawne.
- Nieukończone zależności: brak.
- Ryzyko: Brak ekspertyzy wpływu nie blokuje ewidencji. Brak danych sieciowych wyklucza wyliczanie rezerwy MW i częstości ograniczeń..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/private_sources.md](docs/private_sources.md), [docs/04_data_model.md](docs/04_data_model.md), [docs/13_shared_connection_model.md](docs/13_shared_connection_model.md), [grid_engine/shared_connection.py](grid_engine/shared_connection.py), [tests/test_shared_connection.py](tests/test_shared_connection.py), [scripts/analyze_shared_connection.py](scripts/analyze_shared_connection.py), [tests/test_shared_connection_replay.py](tests/test_shared_connection_replay.py), [docs/14_observation_history.md](docs/14_observation_history.md), [grid_engine/observation_history.py](grid_engine/observation_history.py), [tests/test_observation_history.py](tests/test_observation_history.py), [scripts/build_radkowice_history.py](scripts/build_radkowice_history.py), [tests/test_radkowice_history.py](tests/test_radkowice_history.py), [data/reference/radkowice_observation_history_v1.json](data/reference/radkowice_observation_history_v1.json), [grid_engine/historical_assignments.py](grid_engine/historical_assignments.py), [tests/test_historical_assignments.py](tests/test_historical_assignments.py), [scripts/analyze_historical_assignments.py](scripts/analyze_historical_assignments.py), [grid_engine/strict_json.py](grid_engine/strict_json.py), [tests/test_historical_assignment_replay.py](tests/test_historical_assignment_replay.py), [grid_engine/historical_connection_parameters.py](grid_engine/historical_connection_parameters.py), [tests/test_historical_connection_parameters.py](tests/test_historical_connection_parameters.py), [data/project/information_requests.json](data/project/information_requests.json), [docs/15_information_requests.md](docs/15_information_requests.md), [docs/16_radkowice_public_followup.md](docs/16_radkowice_public_followup.md).

### KSE-034 — Lokalna aplikacja pilotażowa — ocena przesłanek Radkowic

- Odpowiedzialność: Codex.
- Następny krok: Test użytkownika i rozwój pokrycia danych; zweryfikować pobieranie JSON poza przeglądarką Codex.
- Kryterium: Lokalny widok publicznych dowodów, osobne kierunki i napięcia, jawne braki, odtwarzalny wynik bez fikcyjnego scoringu.
- Nieukończone zależności: brak.
- Ryzyko: Pilot jakościowy, nie pełne MVP. Automatyczne potwierdzenie pobrania JSON w Codex nieudane; tekst raportu dostępny w widoku..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-16.
- Dowody/kontekst: [docs/17_local_application.md](docs/17_local_application.md), [backend/local_app.py](backend/local_app.py), [grid_engine/screening_opinion.py](grid_engine/screening_opinion.py), [tests/test_local_app.py](tests/test_local_app.py).

### KSE-035 — Pierwszy prywatny przegląd pakietu mostu i historycznego GIS

- Odpowiedzialność: Codex.
- Następny krok: Rozstrzygnąć rewizje i pochodzenie; kontynuować weryfikację szczegółową, bez automatycznego importu do publicznego pilota.
- Kryterium: Inwentaryzacja i hashe, kontrola kluczowych rysunków i struktury GeoPackage, prywatne wnioski oraz jawne ograniczenia zakresu.
- Nieukończone zależności: brak.
- Ryzyko: Nie jest pełnym audytem wykonawczym, CAD, geometrii GIS ani praw wykorzystania..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-16.
- Dowody/kontekst: [docs/private_sources.md](docs/private_sources.md), [scripts/inspect_private_materials.py](scripts/inspect_private_materials.py), [tests/test_private_material_inspection.py](tests/test_private_material_inspection.py).

### KSE-036 — Weryfikacja i normalizacja historycznej warstwy GIS

- Odpowiedzialność: Codex + Użytkownik.
- Następny krok: Weryfikować pierwotne publikacje i legendy, w tym kolejkę linków z rejestru inwestycji; rozstrzygnąć powiązania, rozbieżności eksportów i prawa wykorzystania. Historyczne rekordy nie stanowią aktualnej bazy infrastruktury.
- Kryterium: Udokumentowana proweniencja i dostęp; geometrie sprawdzone, duplikaty oznaczone, historia oddzielona od bieżących danych.
- Nieukończone zależności: brak.
- Ryzyko: Publiczne źródła składowe nie potwierdzają dokładności i licencji całego opracowania..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/private_sources.md](docs/private_sources.md), [scripts/audit_private_gis_geometry.py](scripts/audit_private_gis_geometry.py), [scripts/normalize_private_gis_capacity.py](scripts/normalize_private_gis_capacity.py), [tests/test_gis_geometry.py](tests/test_gis_geometry.py), [tests/test_historical_gis_capacity.py](tests/test_historical_gis_capacity.py), [scripts/compare_private_gis_tables.py](scripts/compare_private_gis_tables.py), [tests/test_gis_tables.py](tests/test_gis_tables.py), [connectors/gis/compound_groups.py](connectors/gis/compound_groups.py), [scripts/review_private_gis_groups.py](scripts/review_private_gis_groups.py), [tests/test_compound_groups.py](tests/test_compound_groups.py).

### KSE-037 — Rozbieżności dat inwestycji PSE w ocenie pilota

- Odpowiedzialność: Codex.
- Następny krok: Wyjaśnić zakres i odbiór zadania — NEED-014; rozszerzać ewidencję inwestycji.
- Kryterium: Oba publiczne snapshoty zachowane, ekstrakcja z testami, jawna rozbieżność w API i ocenie, bez automatycznego wybrania daty i mocy.
- Nieukończone zależności: brak.
- Ryzyko: Tożsamość zakresu i data fizycznego załączenia nadal nieustalone..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-17.
- Dowody/kontekst: [docs/16_radkowice_public_followup.md](docs/16_radkowice_public_followup.md), [connectors/pse/investment_dates.py](connectors/pse/investment_dates.py), [scripts/build_radkowice_investment_review.py](scripts/build_radkowice_investment_review.py), [tests/test_pse_investment_dates.py](tests/test_pse_investment_dates.py), [tests/test_local_app.py](tests/test_local_app.py).

### KSE-038 — Historyczny rejestr wpisów o inwestycjach z GIS

- Odpowiedzialność: Codex.
- Następny krok: Weryfikować publikacje pierwotne z prywatnej kolejki; powiązania i bieżący status wymagają osobnych dowodów.
- Kryterium: Wersjonowany prywatny wynik, stabilne identyfikatory wpisów, oryginalne atrybuty i hashe; brak awansu planowanej daty do stanu istniejącego.
- Nieukończone zależności: brak.
- Ryzyko: Rekordy nie są unikalnymi inwestycjami. Linki z kompilacji nie zostały zbiorczo zweryfikowane; nieznane prawa i aktualność pozostają otwarte..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-17.
- Dowody/kontekst: [docs/private_sources.md](docs/private_sources.md), [connectors/gis/historical_investments.py](connectors/gis/historical_investments.py), [scripts/normalize_private_gis_investments.py](scripts/normalize_private_gis_investments.py), [tests/test_historical_gis_investments.py](tests/test_historical_gis_investments.py).

### KSE-039 — Projekt PRSP po konsultacjach: dowody inwestycji w pilocie

- Odpowiedzialność: Codex.
- Następny krok: Zweryfikować późniejsze wersje i rzeczywiste wykonanie; rozwijać powiązania bez automatycznego łączenia zakresów.
- Kryterium: Oryginalny PDF i archiwum, dwa sprawdzone wiersze z parserem i testami, jawne daty oraz ograniczenia w aplikacji i eksporcie.
- Nieukończone zależności: brak.
- Ryzyko: Projekt planu nie potwierdza uzgodnienia, załączenia ani dodatkowych dostępnych MW..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-17.
- Dowody/kontekst: [docs/16_radkowice_public_followup.md](docs/16_radkowice_public_followup.md), [connectors/pse/development_plan.py](connectors/pse/development_plan.py), [scripts/build_radkowice_development_plan.py](scripts/build_radkowice_development_plan.py), [tests/test_pse_development_plan.py](tests/test_pse_development_plan.py), [tests/test_local_app.py](tests/test_local_app.py).

### KSE-040 — Audyt przydatności GIS i rzeczywistej próbki OSM Radkowic

- Odpowiedzialność: Codex.
- Następny krok: Pozyskać regionalną geometrię OSM i zweryfikować kandydatów połączeń z dokumentami operatorów.
- Kryterium: Prywatna kompilacja odseparowana, publiczna próbka OSM z hashami i wersjami, selekcja przestrzenna przetestowana, brak awansu geometrii do potwierdzonej topologii.
- Nieukończone zależności: brak.
- Ryzyko: OSM nie potwierdza kompletności, własności urządzeń, układu pracy ani wolnej mocy..
- Termin docelowy: nie ustalono.
- Zakończono: 2026-09-17.
- Dowody/kontekst: [docs/18_gis_osm_integration.md](docs/18_gis_osm_integration.md), [connectors/gis/discovery.py](connectors/gis/discovery.py), [connectors/gis/osm_station.py](connectors/gis/osm_station.py), [tests/test_gis_discovery.py](tests/test_gis_discovery.py), [tests/test_osm_station.py](tests/test_osm_station.py), [data/catalog/osm_radkowice_archive_2026-09-17.json](data/catalog/osm_radkowice_archive_2026-09-17.json).

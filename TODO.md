# TODO — Grid Connection Intelligence

Aktualizacja rejestru: **2026-09-11**. Źródło edytowalne: [todo.json](data/project/todo.json).

Widok generowany. Aktualizujemy JSON, zachowując ID, historię Git i dowody zakończenia. Nie ustalono terminów dla niezaplanowanych zadań. P0 = warunek najbliższego etapu, P1 = rozwój po fundamentach, P2 = dalszy rozwój. Priorytety są kolejnością organizacji pracy, nie scoringiem sieci.

## Najbliższe zadania bez nieukończonych zależności

- **KSE-007 — Ustalić zakres i kryteria MVP** (P0, W toku). Uzyskać akceptację propozycji raportu jednego GPZ i kryteriów odbioru.
- **KSE-009 — Zweryfikować dostęp do publikacji PGE** (P0, Zagrożone). Sprawdzić zwykły dostęp lub oficjalny kanał bez obchodzenia blokady.
- **KSE-030 — Potwierdzić zewnętrzną kopię archiwum** (P0, Do zrobienia). Wykonać prywatną kopię ZIP na drugim nośniku i potwierdzić jej odczyt.
- **KSE-011 — Przetestować uwierzytelnione API ENTSO-E** (P1, Do zrobienia). W odrębnym kroku wykonać małe zapytanie z lokalnym poświadczeniem, bez logowania tokenu.
- **KSE-012 — Potwierdzić eksport ENEA i TAURON** (P1, Do zrobienia). Sprawdzić dokumentowane pliki/API portali i dopuszczalny sposób pobierania.

## Pełny rejestr

| ID | Zadanie | Etap | Status | Priorytet | Zależności |
|---|---|---|---|---|---|
| KSE-001 | Research źródeł i granic dokładności | Research | Zrobione | P0 | — |
| KSE-002 | Katalog i kontrola próbek źródłowych | Research | Zrobione | P0 | KSE-001 |
| KSE-003 | Git i odtwarzanie snapshotów | Organizacja | Zrobione | P0 | — |
| KSE-004 | Wykluczenie lokalnych sekretów z Git | Organizacja | Zrobione | P0 | — |
| KSE-005 | Specyfikacja pipeline wybranego GPZ | Produkt | Zrobione | P0 | KSE-001 |
| KSE-006 | TODO i generator pełnego raportu Excel | Organizacja | Zrobione | P0 | KSE-002 |
| KSE-007 | Ustalić zakres i kryteria MVP | Produkt | W toku | P0 | KSE-001, KSE-005 |
| KSE-008 | Wyjaśnić konflikt dat Energi | Dane | Zrobione | P0 | KSE-002 |
| KSE-009 | Zweryfikować dostęp do publikacji PGE | Dane | Zagrożone | P0 | KSE-002 |
| KSE-010 | Ustalić prawa źródeł wybranych do pilota | Dane | Do zrobienia | P0 | KSE-007 |
| KSE-011 | Przetestować uwierzytelnione API ENTSO-E | Dane | Do zrobienia | P1 | KSE-004 |
| KSE-012 | Potwierdzić eksport ENEA i TAURON | Dane | Do zrobienia | P1 | KSE-002 |
| KSE-013 | Wybrać stację i obszar pilota | Produkt | Do zrobienia | P0 | KSE-007, KSE-010 |
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
- Następny krok: Utrzymywać commity i instrukcję odtwarzania.
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
- Następny krok: Uzyskać akceptację propozycji raportu jednego GPZ i kryteriów odbioru.
- Kryterium: Zapisany zakres pilota, mierzalne kryteria odbioru i wyłączenia bez obietnicy nieuzasadnionych MW/probability.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
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
- Następny krok: Sprawdzić zwykły dostęp lub oficjalny kanał bez obchodzenia blokady.
- Kryterium: Odczytana próbka z datą i prawami albo udokumentowane utrzymanie blokady.
- Nieukończone zależności: brak.
- Ryzyko: HTTP 200 zwracał stronę odrzucenia zamiast danych..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/discovery_log.md](docs/discovery_log.md).

### KSE-010 — Ustalić prawa źródeł wybranych do pilota

- Odpowiedzialność: Użytkownik + Codex.
- Następny krok: Sprawdzić licencje, regulaminy, automatyzację i redystrybucję dla konkretnego zakresu.
- Kryterium: Każde źródło pilota ma rozstrzygniętą podstawę użycia lub jest wyłączone. Kontakt z operatorem wymaga zlecenia użytkownika.
- Nieukończone zależności: KSE-007.
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
- Następny krok: Porównać kandydatów według źródeł, relacji 110 kV/PSE i projektów.
- Kryterium: Rzeczywisty GPZ, udokumentowane powiązania, projekty i inwestycje; wybór uzasadniony dowodami.
- Nieukończone zależności: KSE-007, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/08_roadmap.md](docs/08_roadmap.md).

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
- Następny krok: Pobrać małe wycinki działek, topografii i ograniczeń przyrodniczych.
- Kryterium: GetFeature/pakiety sprawdzone, poprawne CRS i geometrie; prawa i daty zachowane.
- Nieukończone zależności: KSE-013, KSE-010.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/01_data_research.md](docs/01_data_research.md).

### KSE-021 — Zestawienie projektów A/B/C dla GPZ

- Odpowiedzialność: Codex.
- Następny krok: Zbudować raport grup statusu oraz nieznanych i konfliktowych rekordów.
- Kryterium: Potwierdzone przyłączenie, plan i oczekiwanie odróżnione; deduplikacja i kierunkowe sumy z pokryciem.
- Nieukończone zależności: KSE-017, KSE-018.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/gpz_pipeline.md](docs/gpz_pipeline.md).

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
- Następny krok: Udostępnić wybór projektu/GPZ i czytelny raport zwalidowanych danych.
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
- Następny krok: Opracować warianty inwestycji i osiągalności przestrzennej.
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
- Następny krok: Ocenić dostęp do parametrów, profili i topologii operatora oraz solverów.
- Kryterium: Kompletne wymagane wejścia i niezależna walidacja; w przeciwnym razie dokumentacja niewykonalności.
- Nieukończone zależności: KSE-023.
- Ryzyko: Publiczne dane mogą nie wystarczyć; brak gwarancji osiągalności etapu..
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/05_grid_capacity_methodology.md](docs/05_grid_capacity_methodology.md).

### KSE-030 — Potwierdzić zewnętrzną kopię archiwum

- Odpowiedzialność: Użytkownik.
- Następny krok: Wykonać prywatną kopię ZIP na drugim nośniku i potwierdzić jej odczyt.
- Kryterium: Istnieje niezależna kopia archiwum zgodna z manifestem. Sam lokalny ZIP i push nie spełniają warunku.
- Nieukończone zależności: brak.
- Ryzyko: brak dodatkowej uwagi w rejestrze.
- Termin docelowy: nie ustalono.
- Zakończono: nie zakończono.
- Dowody/kontekst: [docs/reproducibility.md](docs/reproducibility.md).

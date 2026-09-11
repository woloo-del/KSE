# Wymagania dla przyszłego modelu danych

Aktualizacja 11.09.2026: powstał [eksperymentalny model Radkowic](11_radkowice_evidence_model.md) i walidator `grid_engine/evidence_graph.py`. Celowo rozróżnia poziom napięcia od fizycznej sekcji szyn oraz relację taryfową od własności. To ograniczony graf dokumentacyjny; pełny model bazy, obserwacji, wniosków i historii nadal wymaga opracowania.

**10.09.2026 — notatka z etapu 1. To nie jest wdrożony schemat bazy.**

Minimalne obiekty domenowe: `OPERATOR`, `SOURCE`, `SOURCE_SNAPSHOT`, `OBSERVATION`, `GRID_NODE`, `SUBSTATION/GPZ`, `BUS`, `TRANSFORMER`, `LINE`, `FEEDER`, `CONNECTION_POINT`, `PROJECT`, `GENERATION_ASSET`, `STORAGE_ASSET`, `DEMAND_ASSET`, `GRID_INVESTMENT`. Potrzebna jest także jednostka `CAPACITY_REPORTING_GROUP`, ponieważ publikowane moce bywają wspólne dla grupy stacji. Grupa raportowa nie jest fizycznym węzłem i nie musi być identyczna z kompletną grupą ograniczeń elektrycznych.

| Obszar | Wymaganie wynikające z badań |
|---|---|
| Tożsamość | Własny stabilny ID, identyfikatory operatora, aliasy, operator, napięcie, geometria; brak scalenia wyłącznie po podobieństwie nazwy |
| Obserwacja | Wartość i jednostka, klasyfikacja REPORTED/MEASURED/CALCULATED/ESTIMATED/INFERRED/UNKNOWN, źródło i snapshot, strona/arkusz/wiersz/pole, daty |
| Czas | Osobno publication_date, observation_date/source_date, retrieval_date, valid_from/to oraz moment rejestracji wiedzy; nieznane daty pozostają null |
| Konflikt | Obie wersje wartości lub daty, dowody, status rozstrzygnięcia; nie nadpisywać jednej drugą |
| Relacja | Obiekt początkowy/końcowy, typ, confirmed/probable/inferred/unknown, dowody, okres, stan planowany/istniejący |
| Projekt | Technologie jako składniki, SPV/inwestor z dowodami, etapy procedury jako historia; nie wszystkie wpisy są osobnymi projektami |
| BESS | P_export_MW, P_import_MW, energy_capacity_MWh, duration_h, PCC_export_limit_MW, PCC_import_limit_MW; brakujące pola null |
| Hybryda | Składniki zainstalowane niezależnie od limitów PCC i scenariusza pracy |
| Dostępność operatora | Kierunek, napięcie, grupa/stacja, horyzont, wariant WP, ograniczenia i definicja raportu |
| Inwestycja | planned/under_construction/commissioned/cancelled/unknown, status dokumentu i daty oczekiwane oddzielone od rzeczywistych |
| Wynik analizy | Snapshot, parametry projektu, wersja metody, konfiguracja, czas analizy, źródła wejściowe i wyjaśnienie; score i confidence odrębne |

Szczegółowy projekt SQL/API oraz walidacja kontraktów należą do etapu 2. Katalog źródeł w etapie 1 nie jest zamiennikiem modelu obserwacji technicznych.

Wymaganie widoku [pipeline GPZ](gpz_pipeline.md) dodaje odrębny `CONNECTION_APPLICATION` z własnym identyfikatorem i historią statusów, związany z projektem oraz wskazanym punktem przyłączenia. Status wykonania przyłączenia, eksploatacji i procedury wniosku należy przechowywać oddzielnie. Brak odpowiedzi w źródle jest UNKNOWN; nie oznacza automatycznie potwierdzonego oczekiwania na odpowiedź.

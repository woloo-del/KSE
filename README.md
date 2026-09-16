# Grid Connection Intelligence - Polska

Stan na **16.09.2026**: pierwszy przegląd źródeł zakończony, rozwijany jest lokalny pilot dokumentacyjny Radkowic 220/110 kV. Działają narzędzia badawcze, graf dowodów, historia obserwacji, ewidencja wspólnego przyłącza i widok trzech wpisów PSE. Projekt nie zawiera aplikacji produkcyjnej ani zweryfikowanego modelu rozpływowego.

**Wniosek:** publiczne dane pozwalają budować audytowalny system rozpoznania sytuacji przyłączeniowej. Nie pozwalają obecnie wiarygodnie wyznaczać wolnej mocy każdego GPZ ani procentowego prawdopodobieństwa uzyskania warunków przyłączenia.

## Dokumenty

- [Rejestr TODO](TODO.md)
- [Raport Excel — generowanie i aktualizacja](docs/project_reporting.md)
- [Brakujące dokumenty i informacje](docs/15_information_requests.md)
- [Graf dowodów Radkowic](docs/11_radkowice_evidence_model.md)
- [Historia obserwacji i parametrów](docs/14_observation_history.md)

- [Raport badawczy i executive summary](docs/01_data_research.md)
- [Katalog źródeł](docs/data_sources.md) oraz [wersja JSON](data/catalog/data_sources.json)
- [Wstępna macierz wykonalności](docs/02_feasibility_matrix.md)
- [Wymaganie: projekty i pipeline wybranego GPZ](docs/gpz_pipeline.md)
- [Kierunek architektury — do etapu 2](docs/03_system_architecture.md)
- [Wymagania dla modelu danych](docs/04_data_model.md)
- [Granice metody oceny mocy](docs/05_grid_capacity_methodology.md)
- [Status metodologii scoringu](docs/06_scoring_methodology.md)
- [Jakość danych i walidacja](docs/07_data_quality.md)
- [Proponowane etapy rozwoju](docs/08_roadmap.md)
- [Decyzje](docs/decision_log.md)
- [Wyniki kontroli lokalnych](data/catalog/research_validation.json)
- [Pierwszy push i codzienna praca z Git](docs/git_workflow.md)
- [Odtwarzanie środowiska i archiwum danych](docs/reproducibility.md)

## Struktura

`connectors/` nie zawiera jeszcze produkcyjnego pobierania danych; obejmuje pomocniczą kontrolę dat publikacji Energi. Datowane foldery `data/raw/research/` przechowują niezmieniane próbki, a `data/catalog/` — katalog 64 źródeł i manifesty SHA-256. `data/reference/` zawiera wersjonowane grafy, historię oraz widok pipeline Radkowic. Moduły `grid_engine/` obsługują dowody, czas, konflikty i ewidencję miejsc; nie obliczają dostępnych MW. Dane prywatne pozostają osobno. Nie utworzono fikcyjnej infrastruktury poza oznaczonymi testami.

## Odtworzenie kontroli

W Pythonie z pakietami `pypdf` i `openpyxl`:

```powershell
python scripts/build_research_catalog.py
python scripts/validate_research.py
```

Pierwszy skrypt generuje katalog z notatek ogólnych i pilota Radkowic. Drugi sprawdza integralność zachowanych próbek, strukturę katalogu i podstawowe formaty danych. Są to narzędzia badawcze, nie pełny pipeline produkcyjny.

Po odtworzeniu odpowiednich archiwów można uruchomić pilot:

```powershell
python scripts/build_radkowice_graph.py
python scripts/build_radkowice_pipeline.py
python -m unittest discover -s tests
```

Widok pipeline dotyczy stanu dokumentu na 31.07.2026: trzech wpisów z obowiązującymi umowami. Nie potwierdza fizycznego przyłączenia, kompletności stacji ani obsadzenia mostu. Ponowienie generatora zachowuje identyczny wynik; zmienione dane lub kod wymagają osobnej wersji wyniku. Reguły i ograniczenia opisuje [dokumentacja pipeline](docs/gpz_pipeline.md).

`scripts/probe_research_sources.ps1` wykonuje jednorazowe próby wskazane w `config/research_probes*.json`. Nie uruchamiaj ich ponownie bez nowej daty i nazw snapshotów: zachowane pliki nie są nadpisywane. HTTP 200 nie oznacza poprawnych danych; w próbie PGE oznaczał stronę blokady. Skrypt nie jest cyklicznym scraperem ani obejściem zabezpieczeń.

Próbki źródłowe są lokalnym materiałem audytowym i nie są przeznaczone do publikacji w Git. Dostęp techniczny nie stanowi potwierdzenia praw do komercyjnego ponownego wykorzystania. Radkowice są obszarem eksperymentu; kwestie licencyjne, pełna architektura produkcyjna i metodologia scoringu pozostają otwarte. Nie wyznaczamy Grid Connection Score ani prawdopodobieństwa uzyskania WP. Zewnętrzna kopia archiwów wymaga potwierdzenia (NEED-010); sam push nie obejmuje surowych źródeł.

Folder `_secrets/` jest lokalny i wykluczony z Git, także w podkatalogach. Nie dodawać go przez `git add -f` ani do archiwów źródeł; poświadczenia nie są danymi badawczymi.

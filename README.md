# Grid Connection Intelligence — Polska

Stan na **10.09.2026**: zakończony pierwszy przegląd źródeł i prób dostępu. Projekt jest na etapie badań; nie zawiera aplikacji produkcyjnej ani zweryfikowanego modelu rozpływowego.

**Wniosek:** publiczne dane pozwalają budować audytowalny system rozpoznania sytuacji przyłączeniowej. Nie pozwalają obecnie wiarygodnie wyznaczać wolnej mocy każdego GPZ ani procentowego prawdopodobieństwa uzyskania warunków przyłączenia.

## Dokumenty

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

`connectors/` rezerwuje miejsce dla źródeł PSE, PGE, ENEA, TAURON, Energa, Stoen, ENTSO-E, BIP i GIS. Nie zawiera jeszcze connectorów produkcyjnych. `data/raw/research/2026-09-10/` zawiera niezmieniane próbki źródłowe; `data/staging/research/` — podglądy kontrolne PDF. `data/catalog/` zawiera rejestr i manifesty pobrań z SHA-256. `data/processed/` i `data/reference/` pozostają bez danych analitycznych. Nie utworzono fikcyjnej infrastruktury.

## Odtworzenie kontroli

W Pythonie z pakietami `pypdf` i `openpyxl`:

```powershell
python scripts/build_research_catalog.py
python scripts/validate_research.py
```

Pierwszy skrypt generuje katalog i jego widok Markdown z jawnych notatek `data/catalog/source_notes.json`. Drugi sprawdza integralność zachowanych próbek, strukturę katalogu i podstawowe formaty danych. Są to narzędzia badawcze, nie pipeline normalizujący dane do modelu sieci.

`scripts/probe_research_sources.ps1` wykonuje jednorazowe próby wskazane w `config/research_probes*.json`. Nie uruchamiaj ich ponownie bez nowej daty i nazw snapshotów: zachowane pliki nie są nadpisywane. HTTP 200 nie oznacza poprawnych danych; w próbie PGE oznaczał stronę blokady. Skrypt nie jest cyklicznym scraperem ani obejściem zabezpieczeń.

Próbki źródłowe są lokalnym materiałem audytowym i nie są przeznaczone do publikacji w Git. Dostęp techniczny nie stanowi potwierdzenia praw do komercyjnego ponownego wykorzystania. Nie wybrano jeszcze ostatecznej architektury, regionu pilotażowego ani wag scoringu.

Folder `_secrets/` jest lokalny i wykluczony z Git, także w podkatalogach. Nie dodawać go przez `git add -f` ani do archiwów źródeł; poświadczenia nie są danymi badawczymi.

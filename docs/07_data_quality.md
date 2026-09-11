# Jakość danych — ustalenia i kontrola etapu 1

**10.09.2026.** Autorytet źródła A–H według AGENTS.md jest oddzielony od kompletności, świeżości, pewności relacji i praw do wykorzystania. Katalog nie zawiera arbitralnych liczbowych ocen jakości.

## Znalezione przypadki wymagające ostrożności

| Przypadek | Dowód | Obsługa |
|---|---|---|
| HTTP 200 bez danych | PGE: zachowany HTML odrzucenia, 346 bajtów | BLOCKED; nie sukces parsera |
| Sprzeczne daty | Energa pipeline: nazwa 31.08, nagłówek i metadane 30.06 | Zachować konflikt, source_date nierozstrzygnięta |
| Inna data strony i arkusza | PSE: aktualizacja strony 01.09, XLSX stan 31.07 | Dwa odrębne pola, bez „odmładzania” danych |
| Przyszłe zamiast obecnych mocy | PSE: tabela importowa nowych planowanych stacji | FUTURE_GRID; nie bieżąca rezerwa |
| Starsze wejścia w nowej publikacji | Stoen: część informacji o małych źródłach z IV kw.2025 | Wiek wejść odrębny od daty wydania |
| Null w API | PSE poze-redoze: brak wartości w próbce | UNKNOWN, bez zamiany na 0 |
| Najstarsze wyniki bez filtra | PSE $first=2: obserwacje z 2024 | Próba interfejsu, nie snapshot bieżącego KSE |
| Anonimizacja i nieustalone punkty | TAURON: wybrane wiersze próbki | Brak scalenia „Osoba prawna” do jednego inwestora |
| Mapowy podgląd bez eksportu | ENEA Power BI | Nie deklarować działającego API danych |

## Wykonana kontrola

`scripts/validate_research.py` kontroluje wymagane pola rejestru, unikalność ID, format dat i URL, rozstrzygnięcie braku liczbowej oceny jakości, powiązania z manifestami, SHA-256 i rozmiary zachowanych plików. Sprawdza parsowalność zachowanych JSON/XML, otwarcie PDF/XLSX i charakterystyczne pola próbek API. Wykrywa blokadę PGE oraz potwierdza nagłówkową rozbieżność dat Energi. Sprawdza lokalne odnośniki dokumentacji.

Wynik wykonania: [research_validation.json](../data/catalog/research_validation.json). Obrazy kontrolne wybranych stron PDF zapisano lokalnie w `data/staging/research/` i obejrzano. Nie wykonano pełnej ekstrakcji ani walidacji wszystkich rekordów z tabel operatorów. Nie ma skonfigurowanego projektu produkcyjnego ani jego zestawu testów/lintera.

Testy odtwarzania `python -m unittest discover -s tests -v`: **3/3 OK**. Sprawdzono przywrócenie 34 plików z rzeczywistego archiwum, wykrycie uszkodzenia oraz odmowę nadpisania odmiennego pliku. Sprawdzenie składni PowerShell zakończyło się powodzeniem. Kontrola próbek JSON rozpoznaje rzeczywisty schemat v2 Energy-Charts (`series`, `data.timestamp/values`), a nie pola starszego interfejsu.

## Wymagania dla przyszłych parserów

### Kontrola dat Energi — 11.09.2026

Ponownie odczytana [oficjalna strona przyłączeń](https://energa-operator.pl/przylaczenie-do-sieci/informacje-o-stanie-przylaczen) nadal wskazuje [PDF o nazwie 2026_08_31](https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf). Odczyt treści online i zachowanej próbki wskazuje nagłówek „Stan na 30.06.2026” oraz tytuł metadanych z czerwcem. Nie otrzymano wyjaśnienia operatora. Nie przypisujemy dokumentowi pewnej daty sierpniowej ani czerwcowej dla wszystkich rekordów.

Moduł `connectors/energa/date_quality.py` porównuje datę nazwy, nagłówka i tytułu metadanych. Konflikt, niepoprawna data lub brak nagłówka powoduje kwarantannę i `source_date=null`. Zgodność dat sama nie dopuszcza źródła do bieżącego pipeline: nadal potrzeba walidacji rekordów, aktualności i praw. Nie jest to jeszcze pełny connector ani parser tabel projektowych.

Wynik dla zachowanej próbki: [energa_date_review_2026-09-11.json](../data/catalog/energa_date_review_2026-09-11.json). Stary PDF i wcześniejszy raport walidacji pozostają niezmienione. Zadanie KSE-008 zamykamy przez wdrożenie kwarantanny, zgodnie z jego kryterium; konflikt źródła pozostaje nierozstrzygnięty.

Odtworzenie po przywróceniu archiwum (Python z `requirements-research.txt`; nowa nazwa wyjścia chroni historię):

```powershell
python -m connectors.energa.date_quality data/raw/research/2026-09-10/energa_pipeline_2026-08-31.pdf --source-url https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf --output data/catalog/energa_date_review_repeat.json
python -m unittest discover -s tests -p test_energa_date_quality.py -v
```

Wykonano 7 testów, w tym rzeczywistego PDF; wszystkie przeszły. Metoda rozpoznaje wyłącznie wskazany wzorzec dat, więc zmieniony nagłówek powoduje zatrzymanie, a nie zgadywanie daty z wierszy projektów.

Parser ma sprawdzać sygnaturę i typ odpowiedzi, wymagane nagłówki, jednostki i zakres tabel, daty, wartości null, duplikaty, zgodność poziomu napięcia i zmiany historyczne. Niezrozumiała zmiana schematu ma zatrzymać promocję do warstwy analitycznej. Błędów nie wolno ignorować; klasy: FETCH_ERROR, PARSE_ERROR, SCHEMA_ERROR, VALIDATION_ERROR, SOURCE_CHANGED, RATE_LIMITED, AUTH_ERROR, UNKNOWN_ERROR.

Potrzebne będą reprezentatywne próbki i testy jednostek oraz rzeczywistych wariantów tabel. Każdy znormalizowany rekord musi wskazywać snapshot i miejsce w źródle. Test poprawnego otwarcia PDF nie dowodzi poprawności ekstrakcji mocy lub przypisania projektu.

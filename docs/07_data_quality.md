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

Parser ma sprawdzać sygnaturę i typ odpowiedzi, wymagane nagłówki, jednostki i zakres tabel, daty, wartości null, duplikaty, zgodność poziomu napięcia i zmiany historyczne. Niezrozumiała zmiana schematu ma zatrzymać promocję do warstwy analitycznej. Błędów nie wolno ignorować; klasy: FETCH_ERROR, PARSE_ERROR, SCHEMA_ERROR, VALIDATION_ERROR, SOURCE_CHANGED, RATE_LIMITED, AUTH_ERROR, UNKNOWN_ERROR.

Potrzebne będą reprezentatywne próbki i testy jednostek oraz rzeczywistych wariantów tabel. Każdy znormalizowany rekord musi wskazywać snapshot i miejsce w źródle. Test poprawnego otwarcia PDF nie dowodzi poprawności ekstrakcji mocy lub przypisania projektu.

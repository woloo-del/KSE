# Materiały użytkownika i prywatne wyniki

Od 11.09.2026 dokumenty przekazane do analizy mogą być przechowywane w `data/private/`. Ten katalog jest wyłączony z Git. Ogólny raport Excel czyta jawną listę dokumentów i nie obejmuje prywatnych plików ani ich treści. Dane nie stają się publicznym źródłem operatora przez samo przesłanie pliku.

Prywatny przegląd zachowuje niezmieniony dokument, SHA-256, wersję notatki i obserwacji, strony dowodowe, datę odczytu oraz osobną paczkę z manifestem. Zmiana przeglądu wymaga nowej wersji; nie należy nadpisywać poprzedniej. Prywatne archiwum wymaga niezależnej kopii, podobnie jak archiwum publicznych źródeł. Nie potwierdzono jej wykonania.

Wykonano pierwszy lokalny przegląd wybranych części dokumentu użytkownika z kontrolą rysunków. Jest to przegląd techniczny, nie weryfikacja kryptograficzna podpisu, pełna analiza prawna ani potwierdzenie najnowszej wersji. Szczegółowe wyniki pozostają w katalogu prywatnym. Informacje dopowiedziane przez użytkownika mają odrębną proweniencję i nie są przedstawiane jako treść PDF.

Integracja prywatnych obserwacji z aplikacją pozostaje osobnym zadaniem. Wynik oparty choć częściowo na źródle prywatnym powinien dziedziczyć jego ograniczenia dostępu. Nie można wysłać takiego wyniku do ogólnego eksportu wyłącznie dlatego, że usunięto sam PDF. Na razie nie wdrożono mechanizmu kontroli dostępu w aplikacji.


## 16.09.2026 — nowy pakiet mostu i historyczny GIS

Wykonano inwentaryzację nowych materiałów użytkownika, zachowano sumy kontrolne i prywatne przeglądy. Kontrola objęła kluczowe rysunki i wytyczne mostu oraz strukturę, liczebność i podstawowe kontrole GeoPackage. Nie obejmuje pełnego audytu CAD, konstrukcji, podpisów ani geometrycznej dokładności GIS. Szczegółowe parametry, przypisania i rozbieżności pozostają poza ogólnym raportem i aplikacją.

Użytkownik określił zbiór GIS jako kompilację danych publicznych ze stanem na 2024 rok. Zachować oddzielnie deklarowaną datę zbioru, metadane plików i horyzonty prognoz. Potrzeba ustalenia pochodzenia i zasad użycia trafiła do NEED-012; aktualne rewizje dokumentacji do NEED-013. NEED-001 oznaczono jako otrzymany materiał, bez uznawania go za kompletny projekt wykonawczy/powykonawczy.

Odtwarzalny inspektor: `scripts/inspect_private_materials.py ROOT OUTPUT`. Oba katalogi muszą być w `data/private`; OUTPUT musi być nowy i poza ROOT. Oryginały nie są modyfikowane; SQLite otwierany jest tylko do odczytu. Wszystkie wyjścia inspekcji i manifesty prywatnych plików pozostają poza Git. Repozytorium wersjonuje kod i ogólny status prac. Pełna odtwarzalność wymaga prywatnej kopii źródeł i wyników poza komputerem.


## Kontrola geometrii i historycznych pól mocowych

Opcjonalne zależności GIS są przypięte w `requirements-gis.txt`. Instalacja: `python -m venv .venv`, następnie `.venv/Scripts/python.exe -m pip install -r requirements-gis.txt`. Nie są wymagane do aplikacji pilotażowej. Testy GIS wymagają tego środowiska.

Polecenia (OUTPUT musi być nowym katalogiem pod `data/private`, poza ROOT):

```powershell
.venv/Scripts/python.exe scripts/audit_private_gis_geometry.py ROOT OUTPUT
.venv/Scripts/python.exe scripts/normalize_private_gis_capacity.py ROOT OUTPUT --compilation-year 2024
.venv/Scripts/python.exe -m unittest discover -s tests
```

Audyt odczytuje nagłówki GeoPackage i WKB, sprawdza CRS, poprawność geometrii, zakres współrzędnych oraz zgodność XY z KMZ. Brak fid w KMZ uruchamia porównanie multizbioru geometrii bez dowodu tożsamości obiektów. Jeden rekord KMZ może dopasować się tylko raz. Jednoczęściowy MultiLineString i LineString są równoważne wyłącznie w tym porównaniu eksportów. Zbieżne punkty pozostają kandydatami do ręcznej analizy. Kontrola nie dowodzi dokładności terenowej, topologii elektrycznej ani zgodności ze wszystkimi wymaganiami OGC.

Normalizacja zachowuje każdą rozpoznaną kolumnę mocy, nazwę pola, fid, tabelę i hash źródła. REPORTED oznacza przepisanie z kompilacji użytkownika, nie bezpośrednie potwierdzenie operatora. Zero pozostaje zerem, braki pozostają UNKNOWN. Złożone lub nierozpoznane wartości zachowują treść źródłową i trafiają do przeglądu. Nieznana kolumna jest zgłaszana osobno. Nic nie jest automatycznie sumowane. Kierunek mocy i niepotwierdzone daty pozostają nieznane. Rok kolumny jest horyzontem starego zbioru, a nie datą nowej obserwacji.

Grupy stacji, obszary i dzielnice mają oddzielny zakres obowiązywania; diagnostyka powtarzających się wartości nie tworzy rezerwy stacji ani mapowania sekcji szyn. Szczegóły pozostają w `data/private/reviews`. Ogólny raport zawiera postęp i dalsze zadania. Oryginały są tylko odczytywane, a ich hashe sprawdzane ponownie na końcu przetwarzania każdego pliku.


Porównanie atrybutów alternatywnych eksportów: `.venv/Scripts/python.exe scripts/compare_private_gis_tables.py ROOT OUTPUT`. Wymaga także zależności z `requirements-research.txt`. Czyta XLSX tylko do odczytu, odrzuca formuły zamiast ufać nieaktualnym wynikom zapisanym w pliku. Sprawdza nagłówki i porównuje multizbiory pełnych wierszy, więc kolejność i powtórzenia nie powodują automatycznego scalania. Zmiany schematu przerywają porównanie. Diagnostyka możliwej zamiany dwóch kolumn nie naprawia źródła i nie usuwa oryginalnego ostrzeżenia. Wyniki są prywatne.


## 17.09.2026 — uzupełnienie dokumentacji mostu

Rozszerzono prywatny przegląd o przekrój pola, zestawienie szaf oraz cztery arkusze etapowania. Zachowano nowe obserwacje i nierozstrzygniętą rozbieżność przypisań między dokumentami; wcześniejsze dowody pozostają niezmienione. Potwierdzono zgodność hashy całego pakietu ze wcześniejszą inwentaryzacją. Doprecyzowano NEED-013 o spójność schematów, przekrojów i zestawień. Nie zmieniono modelu publicznej aplikacji, nie uznano planowanych wyłączeń za fakty eksploatacyjne ani nie wyliczono wolnej mocy. Szczegółowe źródła, strony i parametry pozostają w prywatnym przeglądzie z 17.09.2026.


Przegląd zapisów wielogrupowych: `scripts/review_private_gis_groups.py ROOT OUTPUT`. Wymaga zgodności kolejności nazw z numerowanym opisem, zgodnej liczby składników i jednostki MW. Porównuje kandydatów wyłącznie z wpisami pojedynczych grup w tej samej warstwie i roku. Zgodność wewnątrz kompilacji nie stanowi niezależnego potwierdzenia; przypisania pozostają INFERRED, bez promocji pierwotnych UNKNOWN do aktualnej mocy. Brak porównania i konflikty są jawne. Wyniki, pełne opisy oraz powiązania fid pozostają prywatne.

## 17.09.2026 — rejestr historycznych wpisów o inwestycjach

Polecenie: `.venv/Scripts/python.exe scripts/normalize_private_gis_investments.py ROOT OUTPUT`. Odczytuje dziewięć jawnie wskazanych warstw inwestycji, modernizacji i planów przestrzennych. Wymaga pełnego zestawu plików oraz oczekiwanych pól; błędy geometrii lub zmienione hashe przerywają budowę wyniku. Nie odczytuje pozostałych katalogów ani sekretów. OUTPUT musi być nowym, prywatnym katalogiem poza wejściem.

Każdy wpis zachowuje wszystkie atrybuty, źródłową tabelę, fid i hash. Stabilny identyfikator odnosi się do wiersza konkretnego snapshotu, nie do rozpoznanej inwestycji. Nazwy podobne, powtórzenia i współrzędne nie powodują scalania. Klasyfikacja historyczna wynika wyłącznie z nazwy warstwy i jest oznaczona INFERRED; nie stanowi potwierdzenia aktualnego statusu. Pole roku normalizowane jest tylko wtedy, gdy zawiera pojedynczy czterocyfrowy rok; zakresy i opisy wielu zadań pozostają do przeglądu. Zachowane deklaracje REPORTED dotyczą kompilacji, nie niezależnie zweryfikowanych dokumentów operatora. Rozbieżność kolumn między eksportami pozostaje widoczna.

Prywatny wynik obejmuje rejestr JSON, przegląd i kolejkę adresów do weryfikacji. Grupowanie identycznych URL służy ograniczeniu przyszłych pobrań; nie jest dopasowaniem inwestycji ani dowodem wiarygodności strony. Pierwotne teksty linków pozostają w atrybutach. Nie wykonywano masowego pobierania adresów. Daty załączenia, bieżące statusy, tożsamość inwestycji i przyrosty dostępnej mocy pozostają nieustalone. Wynik nie zasila publicznego API ani ogólnego raportu szczegółami prywatnego zbioru; raport obejmuje postęp i ograniczenia.

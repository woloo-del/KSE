# Materiały użytkownika i prywatne wyniki

Od 11.09.2026 dokumenty przekazane do analizy mogą być przechowywane w `data/private/`. Ten katalog jest wyłączony z Git. Ogólny raport Excel czyta jawną listę dokumentów i nie obejmuje prywatnych plików ani ich treści. Dane nie stają się publicznym źródłem operatora przez samo przesłanie pliku.

Prywatny przegląd zachowuje niezmieniony dokument, SHA-256, wersję notatki i obserwacji, strony dowodowe, datę odczytu oraz osobną paczkę z manifestem. Zmiana przeglądu wymaga nowej wersji; nie należy nadpisywać poprzedniej. Prywatne archiwum wymaga niezależnej kopii, podobnie jak archiwum publicznych źródeł. Nie potwierdzono jej wykonania.

Wykonano pierwszy lokalny przegląd wybranych części dokumentu użytkownika z kontrolą rysunków. Jest to przegląd techniczny, nie weryfikacja kryptograficzna podpisu, pełna analiza prawna ani potwierdzenie najnowszej wersji. Szczegółowe wyniki pozostają w katalogu prywatnym. Informacje dopowiedziane przez użytkownika mają odrębną proweniencję i nie są przedstawiane jako treść PDF.

Integracja prywatnych obserwacji z aplikacją pozostaje osobnym zadaniem. Wynik oparty choć częściowo na źródle prywatnym powinien dziedziczyć jego ograniczenia dostępu. Nie można wysłać takiego wyniku do ogólnego eksportu wyłącznie dlatego, że usunięto sam PDF. Na razie nie wdrożono mechanizmu kontroli dostępu w aplikacji.


## 16.09.2026 — nowy pakiet mostu i historyczny GIS

Wykonano inwentaryzację nowych materiałów użytkownika, zachowano sumy kontrolne i prywatne przeglądy. Kontrola objęła kluczowe rysunki i wytyczne mostu oraz strukturę, liczebność i podstawowe kontrole GeoPackage. Nie obejmuje pełnego audytu CAD, konstrukcji, podpisów ani geometrycznej dokładności GIS. Szczegółowe parametry, przypisania i rozbieżności pozostają poza ogólnym raportem i aplikacją.

Użytkownik określił zbiór GIS jako kompilację danych publicznych ze stanem na 2024 rok. Zachować oddzielnie deklarowaną datę zbioru, metadane plików i horyzonty prognoz. Potrzeba ustalenia pochodzenia i zasad użycia trafiła do NEED-012; aktualne rewizje dokumentacji do NEED-013. NEED-001 oznaczono jako otrzymany materiał, bez uznawania go za kompletny projekt wykonawczy/powykonawczy.

Odtwarzalny inspektor: `scripts/inspect_private_materials.py ROOT OUTPUT`. Oba katalogi muszą być w `data/private`; OUTPUT musi być nowy i poza ROOT. Oryginały nie są modyfikowane; SQLite otwierany jest tylko do odczytu. Wszystkie wyjścia inspekcji i manifesty prywatnych plików pozostają poza Git. Repozytorium wersjonuje kod i ogólny status prac. Pełna odtwarzalność wymaga prywatnej kopii źródeł i wyników poza komputerem.

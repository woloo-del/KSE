# Materiały użytkownika i prywatne wyniki

Od 11.09.2026 dokumenty przekazane do analizy mogą być przechowywane w `data/private/`. Ten katalog jest wyłączony z Git. Ogólny raport Excel czyta jawną listę dokumentów i nie obejmuje prywatnych plików ani ich treści. Dane nie stają się publicznym źródłem operatora przez samo przesłanie pliku.

Prywatny przegląd zachowuje niezmieniony dokument, SHA-256, wersję notatki i obserwacji, strony dowodowe, datę odczytu oraz osobną paczkę z manifestem. Zmiana przeglądu wymaga nowej wersji; nie należy nadpisywać poprzedniej. Prywatne archiwum wymaga niezależnej kopii, podobnie jak archiwum publicznych źródeł. Nie potwierdzono jej wykonania.

Wykonano pierwszy lokalny przegląd wybranych części dokumentu użytkownika z kontrolą rysunków. Jest to przegląd techniczny, nie weryfikacja kryptograficzna podpisu, pełna analiza prawna ani potwierdzenie najnowszej wersji. Szczegółowe wyniki pozostają w katalogu prywatnym. Informacje dopowiedziane przez użytkownika mają odrębną proweniencję i nie są przedstawiane jako treść PDF.

Integracja prywatnych obserwacji z aplikacją pozostaje osobnym zadaniem. Wynik oparty choć częściowo na źródle prywatnym powinien dziedziczyć jego ograniczenia dostępu. Nie można wysłać takiego wyniku do ogólnego eksportu wyłącznie dlatego, że usunięto sam PDF. Na razie nie wdrożono mechanizmu kontroli dostępu w aplikacji.

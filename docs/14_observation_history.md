# Historia obserwacji — prototyp v1

Data: 2026-09-15. Zakres: dokumentacyjne obserwacje REPORTED / UNKNOWN,
bez bazy produkcyjnej, automatycznej aktualizacji i obliczania mocy.

## Dwa niezależne pytania

`known_at` określa, co było zapisane w tej historii do danego momentu.
`effective_on` określa dzień, którego dotyczy analizowany stan.
`recorded_at` to czas pierwszego wpisania obserwacji do historii, nie data
pobrania dokumentu. Nie cofamy go do daty źródła. `retrieval_date` i
`source_date` pozostają oddzielnie w dowodzie.

Przedziały ważności mają postać `[valid_from, valid_to)` — koniec jest
wyłączony. Brak końca nie oznacza bezterminowej ważności: ta wymaga jawnego
`explicitly_open_ended` oraz dowodu uzasadniającego takie twierdzenie.
Brak rozstrzygniętej ważności powoduje UNKNOWN w odpowiedzi o stan dnia,
ale oryginalne twierdzenie źródła nadal można odczytać.

## Korekty, konflikty i prywatność

Nowy wpis nie zmienia poprzedniego. Korekta wskazuje `supersedes`, podaje
powód i musi pochodzić z tej samej serii źródłowej oraz dotyczyć tego samego
obiektu, pola, scenariusza i jednostki. Łańcuch korekt nie może się rozgałęziać.
Zapytanie sprzed korekty nadal zwraca ówczesną wiedzę. Zwykła zmiana statusu
projektu nie jest automatycznie korektą błędu i wymaga własnego dowodu czasu.

Różne źródła zachowują niezależne obserwacje. Sprzeczne wartości obowiązujące
w tym samym dniu dają CONFLICT, bez wyboru najnowszej i bez uśredniania.
Niepewne daty lub jawny UNKNOWN nie są pomijane dla uzyskania pewnego wyniku.
Prywatny dowód widoczny w historii danego pola nadaje całemu wynikowi PRIVATE,
również po korekcie. Przyszła prywatna obserwacja nie jest ujawniana w zapytaniu
o wcześniejszy stan wiedzy. To kontrola eksportu, nie system uprawnień użytkowników.

## Próba Radkowice na rzeczywistych danych

Zarejestrowano trzy obserwacje statusu z zachowanego wykazu PSE, stan na
2026-07-31, pobranego 2026-09-10. Odtworzenie sprawdza SHA-256 oryginalnego
XLSX. Dokładny URL, data pobrania, hash, arkusz i komórka pozostają w pliku
`data/reference/radkowice_observation_history_v1.json` i katalogu PSE_PIPELINE.
To odtworzenie zachowanego źródła, nie ponowna weryfikacja strony 15 września.

Identyfikatory odnoszą się do wierszy źródła, nie do ostatecznie scalonych
projektów. Wszystkie trzy wpisy dokumentują publikowane umowy przyłączeniowe;
nie dowodzą fizycznego przyłączenia. Jeden snapshot nie pozwala odtworzyć
zmian statusów. Dla pytania o stan na 2026-09-15 wynik pozostaje UNKNOWN,
ponieważ nie potwierdzono ciągłej ważności tych twierdzeń.

Odtworzenie z katalogu repozytorium:

```powershell
python -m scripts.build_radkowice_history --recorded-at 2026-09-15T11:21:36Z
```

Ten znacznik odtwarza istniejącą pierwszą rejestrację. Nowe źródła muszą
otrzymać rzeczywisty czas nowego zapisu. Identyczne odtworzenie jest dozwolone;
zmienione bajty wymagają nowej ścieżki `--output`, bez nadpisania poprzedniej.
Potrzebny jest zachowany surowy XLSX, nie sam URL i hash. Oddzielna kopia
archiwum poza komputerem nadal nie jest potwierdzona.

## Ograniczenia i kolejny krok

Moduł operuje na niezmiennych obiektach w pamięci; przykład zapisuje jawny
snapshot JSON. Nie ma jeszcze transakcyjnego rejestru, automatycznego porównania
kolejnych publikacji ani integracji historii z ewidencją wspólnego przyłącza.
Kolejność czasu jest walidowana, lecz biblioteka nie uwierzytelnia zegara.
Wartości są tekstem normalizowanym na wejściu; jednostki i scenariusze rozdzielają
klucze. CALCULATED / ESTIMATED / INFERRED wymagają osobnego kontraktu metod i wejść.

Następny krok: połączyć historię dowodów z odtwarzaniem ewidencji przypisań,
zachowując daty, scenariusze i dziedziczenie prywatności. Nie wymaga to ekspertyzy
wpływu; nie uprawnia do wyliczania rezerwy MW ani prawdopodobieństwa przyłączenia.

Walidacja 2026-09-15: 64 testy Python i 8 testów generatora raportu — wszystkie
przeszły. Obejmuje to odtworzenie trzech wpisów z zachowanego XLSX, ochronę przed
nadpisaniem, korekty, konflikty, granice dat i prywatność. Kontrola `git diff --check`
nie wykazała błędów. Raport Excel z 12 września pozostaje historycznym snapshotem;
nowy dokument jest już na liście wejść generatora do kolejnego odświeżenia raportu.

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
snapshot JSON. Nie ma jeszcze transakcyjnego rejestru ani automatycznego porównania
kolejnych publikacji. Integracja z ewidencją przypisań jest opisana poniżej.
Kolejność czasu jest walidowana, lecz biblioteka nie uwierzytelnia zegara.
Wartości są tekstem normalizowanym na wejściu; jednostki i scenariusze rozdzielają
klucze. CALCULATED / ESTIMATED / INFERRED wymagają osobnego kontraktu metod i wejść.

Integrację historii z ewidencją przypisań dodano w kolejnym przyroście poniżej.
Nie wymaga to ekspertyzy wpływu; nie uprawnia do wyliczania rezerwy MW ani
prawdopodobieństwa przyłączenia.

Walidacja 2026-09-15: 64 testy Python i 8 testów generatora raportu — wszystkie
przeszły. Obejmuje to odtworzenie trzech wpisów z zachowanego XLSX, ochronę przed
nadpisaniem, korekty, konflikty, granice dat i prywatność. Kontrola `git diff --check`
nie wykazała błędów. Raport Excel z 12 września pozostaje historycznym snapshotem;
nowy dokument jest już na liście wejść generatora do kolejnego odświeżenia raportu.

## Integracja z przypisaniami — 2026-09-15

`grid_engine/historical_assignments.py` łączy zapytanie `as_known` z istniejącym
licznikiem `summarize`. Przyjmuje pełną historię oraz identyfikator przyłącza,
scenariusz CURRENT / PLANNED, moment wiedzy i dzień ocenianego stanu.

Kontrakt wejścia obserwacji: `entity_id` to ID wspólnego przyłącza,
`field = position_project:<position_id>`, `value` to ID przypisanego projektu,
`unit = null`. UNKNOWN pozostaje null. Takie przypisanie musi wynikać z dowodu
dotyczącego konkretnego miejsca. Publikowana nazwa stacji lub bliskość projektu
nie wystarczają. Ten kontrakt opisuje jeden projekt na miejsce; jeden projekt
może zajmować kilka miejsc. Nie mapujemy nieznanych miejsc na sztuczne identyfikatory.

Do licznika trafia tylko rozstrzygnięta wartość z dokumentem i ustaloną ważnością.
Sam USER_PROVIDED zachowuje źródłowe twierdzenie, ale wymaga dokumentacyjnego
potwierdzenia. Wszystkie dowody, również zgodne, sprzeczne, prywatne i skorygowane,
pozostają w `position_history` oraz ogólnej liście `evidence`. Pojedynczy dowód
w strukturze Assignment jest odnośnikiem reprezentatywnym, nie wyborem źródła
rozstrzygającym konflikt. Prywatność dziedziczy cały wynik.

`unresolved_position_histories` liczy historie miejsc niewłączone do potwierdzonych
przypisań. Obejmuje również wpisy wygasłe lub jeszcze nieobowiązujące; przyczyny
można odczytać w danej historii. Ten licznik nie jest liczbą projektów ani wolnych
miejsc. Przyszły, jeszcze niezarejestrowany wpis nie ujawnia nawet ID miejsca.

W tej wersji kompletność pozostaje false, maksimum miejsc i limity MW są null.
Nie przenosimy parametrów bieżącego snapshotu do wcześniejszego dnia.
`as_of` wynikowej ewidencji oznacza tu `effective_on`; `known_at` jest osobnym
polem. Identyfikator `historical_assignment_view` opisuje widok w pamięci, nie
unikalny utrwalony snapshot. Wynik jest deterministyczny dla tej samej historii,
parametrów i wersji kodu; trwały zapis i manifest wymagają dalszej integracji.

Testy integracyjne sprawdzają korekty, konflikty, prywatność, wygasłe wpisy,
rozdział scenariuszy i jednostek oraz różnicę liczby projektów i miejsc.
Test na zachowanych publicznych wpisach Radkowic potwierdza, że nie powstaje
z nich żadne przypisanie do mostu. Syntetyczne przypisania istnieją tylko w testach.

Następny krok: wersjonowany plik wejścia i bezpieczne odtwarzanie wyniku z
manifestem, następnie historia parametrów i jawnych deklaracji kompletności.
Trwała baza, kontrola dostępu aplikacji i weryfikacja realnych przypisań pozostają
otwarte w KSE-033. Excel z 12 września nadal jest historycznym raportem.

Walidacja przyrostu integracyjnego: 76 testów Python (w tym 12 testów nowego
adaptera) oraz 8 testów raportowania przeszło 2026-09-15. `git diff --check`
bez błędów. Nie wprowadzono nowych zależności ani danych prywatnych do repozytorium.

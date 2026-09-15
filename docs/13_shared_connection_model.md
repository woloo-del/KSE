# Wspólne przyłącze — model dokumentacyjny

12.09.2026 (prace rozpoczęte 11.09). Moduł `grid_engine/shared_connection.py` działa bez bazy, internetu i nowych zależności. Jest ograniczonym modelem ewidencji miejsc, nie silnikiem oceny przepływów ani rezerwy mocy.

## Dane wejściowe

`SharedConnectionSnapshot` przechowuje ID przyłącza, ID snapshotu, datę zestawienia, scenariusz CURRENT lub PLANNED, maksymalną liczbę miejsc, przypisania projektów oraz odrębne, opcjonalne limity importu/eksportu w MW. Liczba miejsc nie określa liczby słupów, obciążalności mostu ani limitu mocy pojedynczego projektu.

Każda wartość i przypisanie mają dowód: ID źródła, lokalizator, hash zachowanej wersji, datę źródłową i odczytu, pochodzenie DOCUMENT/USER_PROVIDED oraz PUBLIC/PRIVATE. Oznaczenie DOCUMENT nie weryfikuje podpisu ani autentyczności. Znane parametry są REPORTED; nieznane wartości pozostają null. Decimal jest wymagany dla MW i zapisywany w wyniku jako tekst dziesiętny wraz z jednostką.

Przypisanie dotyczy konkretnego przyłącza i scenariusza. Wpis na poziomie stacji nie jest wystarczający do przypisania do wspólnego mostu. ID miejsca może pozostać nieznane. Potwierdzone wskazanie projektu w scenariuszu PLANNED nie oznacza fizycznego przyłączenia. Model liczy przypisania, nie realizację budowy ani moc zarezerwowaną umową.

## Wynik i reguły

- `known_assigned_positions`: liczba jednoznacznych, potwierdzonych przypisań do zidentyfikowanych miejsc. Zero może oznaczać brak takich danych.
- `known_distinct_projects`: liczba unikalnych ID z potwierdzonym wskazaniem przyłącza, także jeśli numer miejsca jest nieznany. Rozstrzygnięcie tożsamości projektu jest obowiązkiem wcześniejszej warstwy.
- `unassigned_positions`: różnica między maksimum a przypisaniami, wyłącznie przy znanej liczbie miejsc, udokumentowanej deklaracji kompletności i braku nierozstrzygniętych przypisań. W przeciwnym razie null z przyczyną. To liczba miejsc w ewidencji, nie oferta przyłączenia.
- Limity importu i eksportu są niezależnymi wartościami źródłowymi. Zero jest różne od braku danych.
- Dostępna moc importowa/eksportowa i możliwość rozpływu pozostają nieznane niezależnie od liczby miejsc.

Sprzeczne lub powtórzone przypisania do jednego miejsca powodują błąd; nie ma cichej deduplikacji. Ten sam projekt może zajmować więcej niż jedno miejsce: wtedy liczniki projektów i miejsc są różne. Niedozwolone są przypisania do innego przyłącza lub scenariusza, ujemne liczby, niefinitywne MW i brak dowodów.

## Czas i prywatność

Datą zestawienia jest moment wiedzy analityka. Nie dowodzi aktualności każdego dokumentu. Wyboru wersji i oceny kompletności dokonuje wcześniejsza warstwa; moduł nie scala historii ani nie rozstrzyga sprzecznych okresów. Pochodzenie każdej informacji pozostaje dostępne w wyniku.

Każde prywatne wejście, także odrzucone z pewnego licznika, oznacza cały wynik jako PRIVATE. `require_public_result` odmawia eksportu takiego wyniku. Jest to kontrola logiczna biblioteki, nie uwierzytelnianie ani pełny system uprawnień. Produkcyjna integracja, automatyczne dziedziczenie dostępu w całym systemie i trwała historia pozostają otwarte w KSE-033.

## Walidacja i dalsza praca

Testy używają wyłącznie jawnie syntetycznych danych. Sprawdzają brak kompletności, nieznane miejsca, duplikaty, zakres przyłącza/scenariusza, wartości graniczne, rozdzielenie MW i liczby miejsc oraz prywatność wyniku. Nie wprowadzono syntetycznych obiektów do grafu Radkowic.

```powershell
python -m unittest discover -s tests -p test_shared_connection.py -v
```

## Odtwarzanie z zapisanego wejścia

`scripts/analyze_shared_connection.py` odczytuje jeden wskazany JSON odpowiadający polom `SharedConnectionSnapshot`. Dowody mają pola klasy `Evidence`, a przypisania klasy `Assignment`. Nieznane dodatkowe pola są odrzucane. Limity MW można przekazać jako liczby dziesiętne lub tekst dziesiętny; nie używa się binarnego float do ich odczytu.

```powershell
python scripts/analyze_shared_connection.py --input SCIEZKA_WEJSCIA.json --output SCIEZKA_NOWEGO_WYNIKU.json
```

Polecenie nie pobiera danych ani nie przeszukuje folderów. Wskazuje hashe wejścia, modułu i skryptu. Ponowne uruchomienie z tymi samymi bajtami daje identyczny wynik. Istniejący plik wyjściowy nie jest nadpisywany. Wynik prywatny można zapisać wyłącznie w `data/private/`; również samo pochodzenie wejścia z tego katalogu wymusza prywatność. JSON oraz dokumenty źródłowe należy przechowywać jako wersjonowany lokalny snapshot z niezależną kopią. Skrypt nie sprawdza automatycznie treści wszystkich dokumentów wskazanych przez hashe.

## Kontrola wejścia — 15.09.2026

Powtórzone nazwy pól JSON są odrzucane na każdym poziomie, również wewnątrz dowodów i przypisań. Dotyczy to także powtórzenia tej samej wartości. Parser nie wybiera ostatniej wersji liczby miejsc, identyfikatora ani klasy dostępu. Błąd występuje przed utworzeniem pliku wynikowego. Poprawne wejścia zachowują dotychczasową metodę obliczeń; zmiana walidacji jest identyfikowana hashem skryptu w wyniku i wersją Git. Raport Excel z 12.09 pozostaje historycznym snapshotem, bez tej późniejszej aktualizacji.

Można rozwijać tę ewidencję bez ekspertyzy wpływu na KSE. Brak ekspertyzy ogranicza wnioski elektryczne, nie blokuje modelowania dokumentów, statusów i powiązań. Kolejne dane techniczne mogą doprecyzować konstrukcję przyłącza; same nie zastąpią topologii ruchowej, obciążeń, parametrów sieci i niezależnej walidacji.

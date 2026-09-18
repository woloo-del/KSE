# Wersjonowanie i odtwarzalność

**10.09.2026.** Dokumentacja, konfiguracje, katalog, manifesty pobrań i narzędzia są wersjonowane w Git. Niezmieniane źródła PDF/XLSX/JSON/XML oraz kontrolne obrazy są przechowywane w lokalnym archiwum o identyfikatorze zależnym od zawartości. Pełna odtwarzalność wymaga **repozytorium oraz archiwum**.

## Dwa elementy kopii projektu

| Element | Co zachowuje | Gdzie |
|---|---|---|
| Historia Git | Dokumentacja, notatki źródłowe, skrypty, konfiguracja, wersje zależności, hash i lista próbek | Lokalnie `.git`, po push także prywatne GitHub |
| Archiwum badania | Dokładne bajty pobranych plików i kontrolnych podglądów oraz manifesty | `data/archives/`, pomijane przez Git |

[Manifest archiwum](../data/catalog/archive_manifest.json) podaje nazwę ZIP, jego SHA-256 i sumę kontrolną każdego elementu. Należy skopiować ZIP na drugi, prywatny nośnik lub do uzgodnionego magazynu kopii. **Archiwum na tym samym dysku nie chroni przed utratą komputera.** W tym etapie nie wysłano go do zewnętrznego magazynu i nie skonfigurowano Git LFS/DVC. Sam push nie obejmuje tych bajtów.

URL pozwala ponowić pobranie, ale nie gwarantuje identycznej historycznej wersji. Gdy operator podmieni plik, nie wolno zastąpić starego snapshotu nową treścią i twierdzić, że odtworzono stare badanie. Dlatego zachowujemy osobne kopie oraz SHA-256.

## Odtworzenie na komputerze z Pythonem

Badanie sprawdzono na Pythonie 3.12.14. Dokładne użyte pakiety zapisano w `requirements-research.txt`. W PowerShell, w folderze repozytorium:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-research.txt
.\.venv\Scripts\python.exe scripts/research_archive.py restore 'D:\Kopie\NAZWA_ARCHIWUM_Z_MANIFESTU.zip'
.\.venv\Scripts\python.exe scripts/build_research_catalog.py
.\.venv\Scripts\python.exe scripts/validate_research.py
```

Zastąp przykładową ścieżkę rzeczywistą lokalizacją zachowanego ZIP. Skrypt najpierw sprawdza hash archiwum, listę i zawartość plików oraz ich docelowe ścieżki. Nie nadpisuje istniejącego pliku o innej zawartości. Archiwum i manifest muszą odpowiadać tej samej wersji Git.

Odtwarzane są lokalne dane wejściowe i kontrole badania. Nie odtwarzamy zdalnego stanu strony internetowej ani całego indeksu wyszukiwarki. Dla stron przejrzanych wyłącznie przez narzędzie web zachowano URL, datę i wnioski, ale nie pełny snapshot HTML. Ich dokładna historyczna treść nie jest gwarantowana; ten zakres ograniczenia jest jawny.

## Test odtwarzania wykonany 10.09.2026

Polecenie `python -m unittest discover -s tests -v` zakończyło się wynikiem **3 testy OK**. W izolowanym katalogu odtworzono wszystkie 34 elementy rzeczywistego archiwum i porównano ich sumy SHA-256. Sprawdzono też odrzucenie uszkodzonego archiwum oraz zachowanie istniejącego pliku o odmiennej zawartości. Oryginalne źródła nie zostały zmienione. Walidator katalogu zakończył się wynikiem `PASS_WITH_SOURCE_WARNINGS`; ostrzeżenia dotyczą opisanych braków/konfliktów źródeł.

## Budowanie kolejnego archiwum

`python scripts/research_archive.py create` tworzy archiwum konkretnego badania z 10.09.2026; przy niezmienionych danych używa tej samej nazwy. Nie jest ogólnym automatycznym backupem wszystkich przyszłych prac. Następny etap danych powinien otrzymać nową datę, manifest i zachowane źródła. Przed stałą automatyzacją trzeba rozszerzyć mechanizm o wybór snapshotu i politykę retencji.

Wynik walidacji zawiera czas uruchomienia, więc ponowna kontrola może zmienić ten plik w Git, nawet gdy dane wejściowe są identyczne. Katalog z tych samych notatek i manifestów jest generowany deterministycznie. Dużych plików ani danych o nierozstrzygniętych prawach nie publikujemy automatycznie razem z kodem.

## Odtwarzanie kolejnych archiwów — 16.09.2026

Narzędzie obsługuje wybór manifestu przez `--manifest` oraz kontrolę bez zapisu
przez `--verify-only`. Bez wskazania manifestu zachowuje dotychczasowe zachowanie.
Nie pobiera niczego z Internetu. Sprawdza cały ZIP i wszystkie elementy przed
rozpoczęciem zapisu, zachowuje istniejące identyczne pliki i odrzuca konflikt.
Przerwanie procesu w trakcie zapisu może pozostawić część poprawnych plików;
ponowienie dokończy brakujące. Nie jest to transakcja systemu plików.

Pary manifest–archiwum do zachowania (wszystkie manifesty w `data/catalog/`, ZIP w `data/archives/`):

| Manifest | ZIP |
|---|---|
| archive_manifest.json | research_2026-09-10_d143d3c637bc7af3.zip |
| radkowice_archive_manifest.json | radkowice_sources_2026-09-11.zip |
| radkowice_tariff_archive.json | radkowice_tariff_2026-09-11.zip |
| radkowice_wolica_archive.json | radkowice_wolica_2026-09-11.zip |
| radkowice_followup_archive_2026-09-15.json | radkowice_followup_2026-09-15.zip |
| radkowice_decision_archive_2026-09-15.json | radkowice_decision_2026-09-15.zip |

Przykład kontroli kopii zachowanej na innym nośniku:

```powershell
python scripts/research_archive.py restore 'D:\Kopie\radkowice_decision_2026-09-15.zip' --manifest data/catalog/radkowice_decision_archive_2026-09-15.json --verify-only
```

Po poprawnej kontroli usuń `--verify-only`, aby odtworzyć brakujące pliki. Powtórz
operację dla każdej potrzebnej pary. Ścieżka D:\Kopie jest przykładowa, nie oznacza
wykonanej kopii. Na nowym komputerze najpierw odtwórz właściwą wersję repozytorium.
Starszy ZIP może zawierać wersję manifestu pobrań inną niż aktualny checkout;
w takim przypadku skrypt celowo odmówi nadpisania, zamiast mieszać wersje.

Test w izolowanym katalogu odtworzył 34 elementy pierwotnego archiwum i 8 elementów
pięciu archiwów Radkowic. Dla każdego porównano SHA-256. Dla nowych archiwów
sprawdzono też brak zapisów w trybie kontroli. Starszy manifest Wolica nie ma
rozmiaru pliku: integralność nadal sprawdzają hashe ZIP i elementu; rozmiar jest
sprawdzany dodatkowo tam, gdzie został zapisany. Nie zmieniano starych manifestów.

To zakres wskazanych archiwów publicznego badania, nie automatyczna kopia całego
projektu. Dokumenty prywatne i sekrety pozostają poza tym narzędziem. Kopia
zewnętrzna nadal wymaga potwierdzenia użytkownika (NEED-010, KSE-030).
Excel z 15.09 pozostaje historycznym snapshotem sprzed tej aktualizacji narzędzia;
aktualna instrukcja i rejestry zostaną uwzględnione przy kolejnym generowaniu raportu.


### Archiwum dat inwestycji — 17.09.2026

`data/archives/radkowice_investment_dates_2026-09-17.zip` zawiera dwa nowe oryginały: raport PSE i portal inwestycji. Manifest: `data/catalog/radkowice_investment_dates_archive_2026-09-17.json`. Kontrola: `python scripts/research_archive.py restore data/archives/radkowice_investment_dates_2026-09-17.zip --manifest data/catalog/radkowice_investment_dates_archive_2026-09-17.json --verify-only`. Sprawdzono oba elementy. To siódme archiwum publicznych źródeł; niezależna kopia nadal wymaga potwierdzenia.


### Archiwum projektu PRSP — 17.09.2026

Ósme publiczne archiwum: `data/archives/radkowice_prsp_2026-09-17.zip`, jeden oryginalny PDF. Manifest: `data/catalog/radkowice_prsp_archive_2026-09-17.json`. Kontrola: `python scripts/research_archive.py restore data/archives/radkowice_prsp_2026-09-17.zip --manifest data/catalog/radkowice_prsp_archive_2026-09-17.json --verify-only`. Wykonano ją pomyślnie. Kopia niezależna nadal niepotwierdzona. Parser `scripts/build_radkowice_development_plan.py --output NOWY_PLIK.json` odtwarza dwa wpisy i nie nadpisuje wyniku.

Generatory katalogu i kontroli źródeł zapisują końce linii LF także w Windows, zgodnie z .gitattributes. Zapobiega to zmianie hashy wejść raportu wyłącznie przez normalizację Git.

## Dziewiąte archiwum — OSM, 2026-09-17

`data/archives/osm_radkowice_discovery_2026-09-17.zip` przechowuje sześć wejść mapy i OSM. Manifest: `data/catalog/osm_radkowice_archive_2026-09-17.json`. Wszystkie sześć elementów sprawdzono przez `scripts/research_archive.py restore ... --manifest ... --verify-only`. Archiwum wymaga osobnej kopii zapasowej (NEED-010); sam Git przechowuje manifest i publiczny wynik audytu, nie surowe archiwum.

## Dziesiąte archiwum — źródła OZE, 17.09.2026

`data/archives/oze_discovery_2026-09-17.zip`, 12 plików. Manifest: `data/catalog/oze_archive_2026-09-17.json`. Pliki obejmują raport, konfiguracje i próbki API; nie są publiczną paczką do redystrybucji. NEED-010 obejmuje osobną kopię zapasową.

18.09.2026: dodatkowe archiwum `data/archives/radkowice_stages_2026-09-18.zip`, manifest `data/catalog/radkowice_stages_archive_2026-09-18.json`. Odtworzenie wyniku: `python scripts/build_radkowice_stages.py`. Archiwum wymaga niezależnej prywatnej kopii, jak pozostałe.

18.09.2026: `data/archives/tauron_dictionary_discovery_2026-09-18.zip` z manifestem `data/catalog/tauron_dictionary_archive_2026-09-18.json` zachowuje cztery strony/skrypt. Nie zawiera pobranej bazy mapy. Wymaga odrębnej kopii prywatnej.

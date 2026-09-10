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

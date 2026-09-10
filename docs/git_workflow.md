# Git i GitHub — instrukcja dla tego projektu

**Przygotowano 10.09.2026.** Folder: `C:\Users\woloo\Desktop\KSE`. Repozytorium: [woloo-del/KSE](https://github.com/woloo-del/KSE).

Git zapisuje wersje lokalnie. GitHub przechowuje wysłaną kopię historii. **Commit** to zapis wersji na komputerze; **push** wysyła zapisane commity na GitHub. Zapisanie pliku w edytorze samo nie wykonuje żadnej z tych operacji.

## Co już skonfigurowano

- Lokalny Git, gałąź `main` i adres `origin`: `https://github.com/woloo-del/KSE.git`.
- Autor tylko dla tego projektu: `woloo-del`, `323589553+woloo-del@users.noreply.github.com`. Identyfikator konta sprawdzono w publicznym API GitHub. To adres maskujący e-mail, nie hasło.
- Dostęp odczytowy do repozytorium sprawdzono; w chwili kontroli nie miało gałęzi. Dostępu zapisu nie potwierdza sam test odczytu.
- W konfiguracji Git dodano zaufanie do dokładnie tego folderu (`safe.directory`), ponieważ narzędzie tworzące `.git` działało jako inny lokalny użytkownik systemowy. Nie dodano globalnej reguły zaufania do wszystkich folderów.
- `.gitignore` pomija sekrety, środowiska, cache i duże dane źródłowe. `.gitattributes` ustala końce linii plików tekstowych.

## Pierwszy push

Otwórz **PowerShell** i wpisz:

```powershell
Set-Location 'C:\Users\woloo\Desktop\KSE'
git status
git log -1 --oneline
git push -u origin main
```

`git log` powinien pokazać przygotowany pierwszy commit. Jeśli pokaże brak commitów, najpierw wykonaj kroki `add` i `commit` opisane niżej. `-u` zapamiętuje powiązanie lokalnego `main` z `origin/main`; przy kolejnych wysłaniach wystarczy `git push`. Po sukcesie odśwież stronę repozytorium.

Git Credential Manager jest skonfigurowany na tym komputerze. Jeśli pojawi się okno logowania, zaloguj się do właściwego konta GitHub w przeglądarce. Nie wpisuj tokenu do plików projektu lub adresu repozytorium. [GitHub — uwierzytelnienie przez GCM, sprawdzono 10.09.2026](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).

## Kolejne zmiany — zwykły cykl

Po zapisaniu plików i wykonaniu właściwych kontroli:

```powershell
git status
git diff
git add README.md docs scripts config data/catalog requirements-research.txt .gitignore .gitattributes AGENTS.md
git diff --cached --stat
git commit -m "Opisz konkretnie wykonana zmiane"
git push
```

`status` pokazuje zmienione pliki; `diff` — ich treść. `add` wybiera pliki do zapisu wersji. `commit` zapisuje tę wersję lokalnie. `push` ją wysyła. Jeśli pracujemy nad nowym folderem, trzeba dopisać go do `git add` lub po kontroli listy użyć `git add .`. Pliki ignorowane nie trafią do commita bez specjalnego wymuszenia; nie używaj `git add -f` do danych źródłowych.

Gdy Codex informuje, że już wykonał commit, nie musisz ponownie robić `add` i `commit`; sprawdź `git status`, `git log -1 --oneline`, a następnie wykonaj `git push`.

## Praca na drugim komputerze i zmiany na GitHub

Na nowym komputerze pobierz repozytorium przez `git clone https://github.com/woloo-del/KSE.git`. Zależności i archiwum danych odtwórz według [instrukcji odtwarzania](reproducibility.md).

Przed pracą nad istniejącą kopią, gdy drzewo robocze jest czyste, można pobrać nowe commity poleceniem `git pull --ff-only`. Jeśli push zostanie odrzucony, ponieważ na GitHub są dodatkowe zmiany, zatrzymaj się i odczytaj komunikat. Nie używaj `--force`. Synchronizacja i ewentualne konflikty muszą zachować obie historie.

## Co oznaczają typowe komunikaty

| Komunikat | Znaczenie / następny krok |
|---|---|
| `nothing to commit, working tree clean` | Wszystkie śledzone zmiany zapisane lokalnie; nie dowodzi jeszcze wysłania |
| `Everything up-to-date` | Brak nowych commitów do wysłania |
| `Your branch is ahead ...` | Masz lokalne commity oczekujące na push |
| `Repository not found` | Dla repo prywatnego sprawdź konto, dostęp i adres; nie musi oznaczać nieistnienia repo |
| `src refspec main does not match any` | Zwykle brak pierwszego commita lub inna nazwa gałęzi |
| `non-fast-forward` / `fetch first` | Na serwerze jest historia, której nie ma lokalnie; wymagana bezpieczna synchronizacja |

Źródło procedury: [GitHub — wysyłanie istniejącego projektu, sprawdzono 10.09.2026](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github). Prywatność repozytorium nie zmienia warunków licencji cudzych danych.

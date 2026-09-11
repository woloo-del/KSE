# Rejestr TODO i raport projektu w Excelu

Źródłem zadań jest `data/project/todo.json`. Czytelny [TODO.md](../TODO.md) i skoroszyt są generowanymi widokami tego samego rejestru. Codex aktualizuje zadania po kolejnych pracach, zachowuje stałe ID i zapisuje kryteria oraz dowody zakończenia. Zadania zakończone pozostają w historii. Nowe wymaganie produktu powinno otrzymać zadanie lub zostać przypisane do istniejącego.

Statusy przechowywane w rejestrze odpowiadają wybranemu szablonowi: `Not Started` — do zrobienia, `In Progress` — w toku, `At Risk` — zagrożone, `Complete` — zakończone. Nieukończone zależności są odrębnym polem. Termin pozostaje pusty, jeśli nie został ustalony. Liczba zakończonych zadań nie jest procentem gotowości całego produktu.

## Generowanie

W PowerShell, w folderze projektu:

```powershell
.\scripts\generate_project_report.ps1
```

Skrypt korzysta z dołączonego do Codex środowiska Node.js i pakietu `@oai/artifact-tool`. Domyślnie lokalizuje środowisko w profilu Windows; alternatywną instalację można wskazać parametrem `-RuntimeRoot`. Nie instaluje bibliotek do systemu i nie łączy się z operatorami. Tworzy lokalne dowiązanie zależności w ignorowanym `.report_runtime/`.

Wyniki trafiają do `outputs/01a08b04-7ddd-7641-8f44-7d0d6ae13653/`. Nazwa XLSX zawiera datę rejestru i skrót wejść. Manifest obok pliku identyfikuje wejścia przez SHA-256, wersję generatora, szablonu i środowiska oraz czas wytworzenia. Git identyfikuje ostatni commit widoczny podczas generowania; hashe obejmują także bieżące niezacommitowane wejścia. Powtórne generowanie tych samych wejść może zmienić techniczne metadane XLSX, więc porównujemy zawartość i hashe wejść, a nie obiecujemy identyczności bajtowej każdego eksportu.

Na komputerze bez dołączonego środowiska wymagany jest dostęp do kompatybilnego `@oai/artifact-tool`; same pakiety Python z wcześniejszego etapu nie wystarczą. Skrypt zgłasza brak zależności zamiast tworzyć niepełny raport. Szablon Project Tracker jest zachowany w `data/reference/project_tracker_template.xlsx` i pozostaje niezmieniany. Jego fikcyjne dane demonstracyjne są zastępowane przed eksportem.

## Zakres raportu

Po eksporcie skrypt uruchamia kontrolę tylko do odczytu przez Python i openpyxl z tego samego środowiska. Sprawdza kompletność ID, daty, zapisane wyniki formuł, harmonogram, zachowanie szablonu i hashe wejść. Wynik zapisuje obok XLSX jako `.validation.json`; błąd kończy polecenie niepowodzeniem. Sprawdzone środowisko: Node.js 24.19.0, artifact-tool 2.8.59, Python 3.12.14, openpyxl 3.1.5. Podglądy każdej zakładki są zapisywane w ignorowanym folderze `previews`; `-SkipPreviews` pomija tylko renderowanie.

- Plan prac w wybranym szablonie, wraz z osią czasu. Daty nie są wymyślane; brak terminów oznacza brak paska na osi. Plan pokazuje maksymalnie 30 zadań, a pełny rejestr jest zawsze w zakładce TODO. Przy większym rejestrze najpierw pokazywane są zadania otwarte według priorytetu.
- Podsumowanie wykonalności produktu, stan badań i najważniejsze niewiadome.
- Pełny TODO: status, etap, priorytet, zależności, następna czynność, kryterium zakończenia, odpowiedzialność i dowody.
- Macierz wykonalności, katalog wszystkich źródeł i szczegółowe karty pól, w tym daty, interfejsy, ograniczenia i licencje.
- Rejestr ryzyk ze źródeł i zadań oraz komplet wyjaśnień z dokumentów projektu wskazanych w generatorze.
- Zapis wyników wcześniejszej walidacji i prób dostępu, z datą ich wykonania. Generowanie raportu nie wykonuje ponownie tych zdalnych prób ani nie odświeża dat źródeł.
- Informacje o wersji, odtwarzaniu i sposobie aktualizacji raportu.

Raport jest snapshotem wiedzy projektowej. Nie zawiera nieistniejących wyników dla GPZ, sztucznych MW ani scoringu. Nie zastępuje szczegółowych surowych plików operatorów; ich lokalne archiwum i manifest pozostają osobno.

## Bezpieczeństwo i aktualizacja

Generator odczytuje tylko jawną listę plików wejściowych. Nie skanuje całego folderu projektu, nie czyta `_secrets`, nie pobiera zmiennych środowiskowych z kluczami ani nie umieszcza poświadczeń w arkuszu. Aktualizacje źródeł należy najpierw zapisać w katalogu i dokumentacji.

Edycja komórek wygenerowanego Excela nie synchronizuje się z repozytorium. Do trwałej zmiany należy zaktualizować JSON lub właściwy dokument, ponownie wygenerować raport i wykonać commit. Listy i wskaźniki arkusza odzwierciedlają rekordy z danego generowania; nie jest to połączenie na żywo z operatorami.

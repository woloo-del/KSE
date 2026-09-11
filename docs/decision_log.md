# Decision log

## 2026-09-10 — Zakres etapu 1

**Date:** 2026-09-10  
**Decision:** Badanie źródeł i wykonalności bez aplikacji produkcyjnej.  
**Context:** Użytkownik uzależnił decyzję o MVP od oceny dostępnych danych.  
**Options considered:** Dashboard od początku; model syntetyczny; badanie źródeł i próby dostępu.  
**Selected option:** Badanie źródeł, katalog, niezmieniane próbki i dokumentacja.  
**Reason:** Poprawność danych i możliwość audytu poprzedzają analitykę/UI.  
**Trade-offs:** Nie ma demonstracji aplikacji ani punktowego score.  
**Consequences:** Wybór pilota, właściwa architektura i PoC pozostają kolejnymi etapami.

## 2026-09-10 — Proweniencja i status weryfikacji

**Date:** 2026-09-10  
**Decision:** Oddzielić znaleziony adres, odczyt dokumentacji, próbę pobrania i poprawną treść próbki.  
**Context:** PGE zwróciło stronę blokady z HTTP 200; ENEA udostępnia viewer bez potwierdzonego API.  
**Options considered:** Binarne „dostępne/niedostępne”; wielowymiarowy status.  
**Selected option:** Jawne statusy i manifesty HTTP/bytes/hash/time.  
**Reason:** Status transportu nie dowodzi dostępności danych.  
**Trade-offs:** Rejestr wymaga więcej metadanych.  
**Consequences:** Brak promocji blokady lub dokumentacji do statusu gotowego źródła danych.

## 2026-09-10 — Brak sztucznej dokładności i scoringu

**Date:** 2026-09-10  
**Decision:** Nie ustalać wag Grid Connection Score ani procentowej pewności.  
**Context:** Brak wystarczającego publicznego pokrycia lokalnych parametrów i zbioru kalibracyjnego.  
**Options considered:** Heurystyczny wynik liczbowy z arbitralnymi wagami; raport przesłanek i niewiadomych.  
**Selected option:** Raport faktów i ograniczeń; score/probability/quality_score pozostają null.  
**Reason:** Zachowanie zgodności z AGENTS.md i zakazem pozornej precyzji.  
**Trade-offs:** Trudniejsza prezentacja jednego rankingu.  
**Consequences:** Metodologia scoringu wymaga odrębnego projektu i walidacji.

## 2026-09-10 — Daty i grupy raportowania są częścią danych

**Date:** 2026-09-10  
**Decision:** Zachować konflikty dat oraz modelować jednostkę raportowania mocy odrębnie od fizycznej stacji.  
**Context:** Energa: nazwa pliku 31.08, nagłówek 30.06; PSE/Stoen: moce zależne od grupy, wariantu i horyzontu.  
**Options considered:** Jedna data z nazwy; swobodne przypisanie mocy każdej stacji; jawne dowody i kontekst.  
**Selected option:** Nierozstrzygnięta data stanu tam, gdzie występuje konflikt; wymagany reporting_group, direction, horizon, assumptions w przyszłym modelu.  
**Reason:** Zapobieganie fałszywej aktualności i wielokrotnemu liczeniu tej samej dostępności.  
**Trade-offs:** Część danych nie nadaje się jeszcze do agregacji.  
**Consequences:** Rozstrzygnięcie konfliktu i interpretacja tabel są warunkami normalizacji.

## 2026-09-10 — Architektura pozostaje propozycją

**Date:** 2026-09-10  
**Decision:** Rekomendować do rozważenia PostgreSQL/PostGIS bez instalowania dodatkowych baz.  
**Context:** Model wymaga historii, relacji i GIS; nie wykazano potrzeby drugiego magazynu grafowego.  
**Options considered:** PostgreSQL/PostGIS, rozszerzenie pgRouting, Neo4j, hybryda.  
**Selected option:** W etapie 1 lokalny katalog i pliki; kandydat MVP opisany w dokumencie 03.  
**Reason:** Prostota operacyjna i nieprzesądzanie etapu 2.  
**Trade-offs:** Nie wykonano benchmarku zapytań i baz.  
**Consequences:** Właściwa decyzja wdrożeniowa po określeniu zakresu pilota; nie dodano zależności produkcyjnych.

## 2026-09-10 — Git i odtwarzalne snapshoty

**Date:** 2026-09-10  
**Decision:** Wersjonować pracę w Git i zachować osobne archiwum źródeł z manifestem.  
**Context:** Użytkownik utworzył prywatne `woloo-del/KSE` i poprosił o wersjonowanie, odtwarzalność oraz instrukcję push.  
**Options considered:** Same adresy URL; zwykły Git z dużymi plikami; Git + lokalne archiwum z hashami; zewnętrzny LFS/DVC.  
**Selected option:** Git dla dokumentacji/kodu/manifestów, dokładne źródła w ZIP poza zwykłą historią Git, instrukcja osobnego backupu.  
**Reason:** Same URL nie zachowują zmieniających się dokumentów; duże źródła i ich prawa wymagają odrębnego traktowania.  
**Trade-offs:** Do pełnego odtworzenia potrzebny jest także zachowany ZIP; nie skonfigurowano zewnętrznego magazynu danych.  
**Consequences:** Autor z adresem GitHub noreply, lokalne commity po sprawdzeniu, push odrębny od zapisu lokalnego; zależności badawcze przypięte do wersji.

## 2026-09-10 — Lokalne sekrety i widok pipeline GPZ

**Date:** 2026-09-10

**Decision:** Wykluczyć `_secrets/` z Git i opisać trzy grupy projektów wybranego GPZ.

**Context:** Użytkownik dodał lokalne poświadczenie ENTSO-E oraz wskazał potrzebę rozróżnienia projektów przyłączonych, planowanych i wniosków bez odpowiedzi.

**Options considered:** Sam status projektu; odrębne wykonanie przyłączenia, eksploatacja i procedury wniosków. Interpretowanie pustej daty odpowiedzi jako oczekiwania albo jawne UNKNOWN.

**Selected option:** Specyfikacja `gpz_pipeline.md`, odrębne wnioski i dowody statusu; brak potwierdzenia odpowiedzi nie jest potwierdzonym oczekiwaniem. Folder sekretów ignorowany rekurencyjnie, bez odczytu zawartości.

**Reason:** Użyteczność raportu GPZ przy zachowaniu poprawnych statusów, deduplikacji i ochrony poświadczeń.

**Trade-offs:** Nie każdy publiczny rekord pozwala wypełnić jedną z trzech grup; potrzebna kategoria nieznana/konfliktowa.

**Consequences:** Rozszerzono wymagania pilota i modelu danych; nie wdrożono jeszcze funkcji ani nie użyto klucza API.

## 2026-09-10 — Stały TODO i generowany raport Excel

**Date:** 2026-09-10

**Decision:** Utrzymywać jeden strukturalny rejestr zadań i generować z plików projektu szczegółowy raport XLSX.

**Context:** Użytkownik poprosił o prowadzenie TODO oraz skrypt do pełnego raportowania projektu; wybrał szablon Project Tracker.

**Options considered:** Ręcznie aktualizowany Excel; osobne niesynchronizowane listy; JSON jako źródło i generowane widoki Markdown/Excel.

**Selected option:** `data/project/todo.json`, stałe ID, zależności i kryteria; generator Node.js z dołączonym artifact-tool oraz zachowanym szablonem. Pełny raport obejmuje wszystkie źródła, wykonalność, ryzyka, dokumentację i zapisane kontrole.

**Reason:** Utrzymanie historii w Git i odtwarzalnego powiązania raportu z konkretnymi wejściami. Brak podwójnej ręcznej edycji statusów.

**Trade-offs:** Raport jest snapshotem, nie synchronizuje zmian z Excela do repo. Generator wymaga kompatybilnego środowiska artifact-tool. Oś planu pokazuje do 30 zadań, pełny rejestr nie ma tego ograniczenia. Brak terminów nie jest uzupełniany fikcyjnym harmonogramem.

**Consequences:** Dodano walidację zależności, dowodów zakończenia, schematu wykonalności oraz manifest raportu z hashami wejść. Sekrety pozostają poza raportem. Nie rozpoczęto implementacji analitycznej aplikacji.

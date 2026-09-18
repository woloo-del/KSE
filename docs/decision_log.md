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

## 2026-09-11 — kwarantanna sprzecznej daty pipeline

**Decision / Context:** Publikacja Energi wskazuje różne daty w nazwie pliku i nagłówku. Ponowny odczyt oficjalnej strony nie dostarczył rozstrzygnięcia.

**Options considered:** Data z nazwy; data z nagłówka; zachowanie wszystkich twierdzeń i kwarantanna.

**Selected option / Reason:** Ostatni wariant, `source_date=null`, `DATE_CONFLICT`. Nie ma podstaw do wyboru jednej daty dla całego zbioru. KSE-008 kończy się kontrolą ryzyka, a nie usunięciem sprzeczności u operatora.

**Trade-offs / Consequences:** Mniejsze pokrycie pewnego bieżącego pipeline; dokument pozostaje dowodem badawczym. Nowy moduł bada wyłącznie daty, nie rekordy projektów. Zgodne daty nie zastępują kontroli licencji, aktualności i poprawności ekstrakcji. Zakres pilota nadal jest propozycją w `docs/09_pilot_scope.md`.

## 2026-09-11 — Radkowice jako obszar pilota dokumentacyjnego

**Decision / Context:** Użytkownik zaproponował Radkowice 220/110 kV i dopuścił lepiej udokumentowaną alternatywę.

**Options considered:** Radkowice; Kościerzyna z publikacji Energi; dalsze poszukiwanie stacji bez wskazania użytkownika.

**Selected option / Reason:** Radkowice do dalszych prac badawczych: trzy konkretne BESS w zachowanym XLSX PSE, portal inwestycji, lokalny plan energetyczny. Alternatywa Energi ma konflikt dat. To dobór obszaru, nie ranking technicznej zdolności przyłączeniowej.

**Trade-offs / Consequences:** Granice PSE/PGE, pipeline 110 kV i prawa źródeł pozostają otwarte. KSE-013 jest w toku do spełnienia pełnych kryteriów i zależności; wybranie stacji nie kończy licencjonowania. Model ma oddzielać miejsce stacji, poziomy napięcia, granice operatorów i grupy publikowanych mocy. Nie zakładamy, że projekty 220 kV konkurują o jeden transformator 220/110 kV.

## 2026-09-11 — eksperymentalny graf dowodów, bez bazy produkcyjnej

**Decision / Context:** Dostępne źródła pozwalają przetestować część relacji przed pełnym modelem pilota; brak granic własności i parametrów elektrycznych.

**Options considered:** Czekać na komplet źródeł; uruchomić pełną bazę; przetestować niewielki graf dokumentacyjny w JSON z walidacją.

**Selected option / Reason:** JSON i walidator Python, bez nowych zależności. Każde twierdzenie ma dowód, daty i hash. To odtwarzalny eksperyment reprezentacji danych; nie zmienia otwartych warunków produkcyjnego wykorzystania źródeł.

**Trade-offs / Consequences:** Brak zapytań przestrzennych, trwałej bazy historii i modelu rozpływowego. Pełne KSE-014/018 pozostają otwarte. Powiązanie PGE z miejscem dostarczania z taryfy nie jest relacją własności. Nowe KSE-031 obejmuje wyłącznie wykonany eksperyment i jego testy.

## 11.09.2026 — graf v2 i prywatne materiały

Decision: zachować v1, utworzyć v2 z dodatkowym źródłem publicznym; dokumenty użytkownika i pochodne wyniki przechowywać oddzielnie.
Options considered: nadpisanie grafu; wspólny katalog bez ograniczeń; jawne wersje i rozdział dostępu.
Selected option: jawne wersje grafu i lokalny katalog prywatny z wersjami przeglądu oraz hashami.
Reason: nie mieszać parametrów planowanych z istniejącymi ani materiałów użytkownika z publiczną bazą źródeł.
Trade-offs: prywatne wyniki nie są objęte Git ani ogólnym Excelem; wymagają oddzielnej kopii.
Consequences: pełna integracja prywatnych danych pozostaje KSE-033; obecna aplikacja nie ma jeszcze kontroli dostępu.

## 11.09.2026 — niezależna ewidencja wspólnego przyłącza

Decision: rozwijać model dokumentacyjny mimo niedostępności ekspertyzy wpływu od użytkownika.
Options considered: oczekiwanie na ekspertyzę; heurystyczne MW; ewidencja miejsc z jawnymi brakami.
Selected option: ewidencja w osobnym, czystym module Python bez dodatkowych zależności.
Reason: przypisania i status kompletności dają sprawdzalne informacje bez udawania modelu rozpływowego.
Trade-offs: można obliczyć liczbę nieprzypisanych miejsc dopiero z kompletnych wejść; nie obliczamy dostępnych MW ani prawdopodobieństwa.
Consequences: prywatny dowód oznacza prywatny wynik, również gdy nie wchodzi do pewnego licznika. KSE-033 pozostaje w toku, ponieważ nie ukończono historii i integracji aplikacyjnej.

## 2026-09-15 — oddzielny czas wiedzy i ważności obserwacji

Decision / Context: odtwarzać historyczną wiedzę bez nadpisywania korekt i bez uznawania daty publikacji za bezterminową ważność.
Options considered: ostatni wpis wygrywa; pełna baza temporalna; czysty moduł obserwacji i wersjonowane snapshoty.
Selected option: moduł Python z dwiema osiami czasu, jawnymi korektami i konfliktami.
Reason: pozwala przetestować semantykę przed integracją bazy; nie wymaga dodatkowych zależności.
Trade-offs: UNKNOWN przy nierozstrzygniętej ważności; brak trwałego dziennika transakcyjnego i automatycznej historii całego pipeline.
Consequences: pierwsza rejestracja lipcowego źródła w nowym rejestrze ma rzeczywisty czas 15 września. Prywatność dziedziczy cały wynik widocznej historii pola. KSE-033 pozostaje w toku. Szczegóły: docs/14_observation_history.md.

## 2026-09-15 — odtwarzanie przypisań z historii dowodów

Decision / Context: połączyć historię z licznikiem miejsc bez dopisywania niepotwierdzonych relacji.
Options considered: kopiowanie bieżącego snapshotu do historii; osobny licznik historyczny; adapter wykorzystujący dotychczasową walidację i licznik.
Selected option: adapter dla jawnych obserwacji projektu na konkretnym miejscu, z datami i scenariuszem.
Reason: zachowuje korekty, konflikty i wszystkie źródła; nie duplikuje reguł liczenia miejsc.
Trade-offs: brak udokumentowanej ważności albo tylko twierdzenie użytkownika wyklucza potwierdzony licznik. Maksimum, kompletność i MW wymagają osobnej historii i pozostają nieznane.
Consequences: trzy publiczne wpisy projektów przy Radkowicach nie stają się przypisaniami do mostu. Integracja jest biblioteką, bez trwałego magazynu i bez nowych faktów sieciowych. KSE-033 nadal w toku.

## 2026-09-15 — plikowy replay historii z manifestem

Decision / Context: umożliwić ponowne uruchomienie historycznej analizy ze wskazanego wejścia.
Options considered: osobny manifest i wynik; manifest osadzony; baza danych.
Selected option: manifest osadzony w jednym wersjonowanym JSON, wyłączny zapis nowego pliku.
Reason: nie tworzy pary plików wymagającej synchronizacji; obejmuje wejście, zapytanie, kod i środowisko bez nowych zależności.
Trade-offs: nie ma transakcyjnego magazynu ani automatycznej weryfikacji źródłowych dokumentów; przerwanie zapisu może pozostawić niepełny plik.
Consequences: prywatny rekord w całym wejściu wymusza prywatność zapisanego wyniku z manifestem, także poza czasem zapytania. Dekoder JSON jest wspólny dla obu runnerów, jego hash jest zachowany. KSE-033 pozostaje otwarte do dalszej integracji i historii parametrów.

## 2026-09-15 — jawnie wybierana wersja parametrów historycznych v2

Decision / Context: dodać historię maksimum miejsc, kierunkowych limitów MW i deklaracji kompletności.
Options considered: zmiana zachowania żądań v1; osobny duplikat całego silnika; adapter v2 wykorzystujący istniejącą historię i licznik.
Selected option: adapter v2 wybierany nową wersją żądania, z zachowaniem metody v1.
Reason: nie reinterpretować wcześniejszych żądań; rozpatrywać wszystkie parametry dla tych samych dat i scenariusza.
Trade-offs: kompletność pozostaje twierdzeniem źródła wymagającym kuracji. Każda nierozstrzygnięta historia miejsca blokuje liczbę nieprzypisanych miejsc; brak automatycznej normalizacji odmiennych tekstów liczbowych.
Consequences: jawne jednostki i dowody są obowiązkowe; raportowane limity nie są dostępnymi MW. Nie dodano parametrów Radkowic bez dowodów. Kod i testy bez nowych zależności; manifest obejmuje nowy moduł. KSE-033 nadal w toku.

## 2026-09-15 — rejestr potrzeb użytkownika w raporcie

Decision / Context: użytkownik prosi o wskazywanie brakujących dokumentów i informacji w stałym rejestrze trafiającym do raportu.
Options considered: uwagi w rozmowie; dodatkowe zadania TODO dla każdego dokumentu; odrębny rejestr potrzeb powiązany z dokumentacją i Excelem.
Selected option: information_requests.json oraz zakładka Potrzebne informacje.
Reason: dokument może być otrzymany, ale nadal niewystarczający; stan pozyskania nie jest stanem zadania implementacyjnego.
Trade-offs: potrzebna regularna aktualizacja i kuracja tekstu; arkusz jest generowanym widokiem, nie formularzem zapisującym automatycznie do repozytorium.
Consequences: pozycje niedostępne i otrzymane pozostają widoczne. Bez ponawiania prośby o ekspertyzę lub już dostarczone WP. Prywatna treść nie trafia do rejestru ani ogólnego raportu.

## 2026-09-15 — walidacja katalogu obejmująca wiele dat pobrań

Decision / Context: pierwotny walidator ograniczał ścieżki do 10 września i pomijał manifesty pilota, mimo rozwoju katalogu.
Options considered: osobne kontrole bez pełnego pokrycia; rozszerzenie istniejącej kontroli historii.
Selected option: istniejący walidator obejmuje wszystkie daty pod data/raw/research i jawne dodatkowe manifesty pilota. Unikalność dotyczy snapshotu, nie źródła.
Reason: kolejne pobranie tego samego źródła jest poprawną historią, a każdy surowy plik nadal musi mieć manifest i zgodny hash.
Trade-offs: kontrola wymaga wszystkich zachowanych plików; nie jest testem aktualności stron operatorów. Starsze kontrole semantyczne nadal dotyczą swoich datowanych próbek.
Consequences: 35 plików objętych kontrolą, bez włączania data/private i _secrets. Nowe źródła nie oznaczają nowych parametrów sieci w grafie.

## 2026-09-16 — odtwarzanie jawnie wybranego archiwum

Decision / Context: nowe snapshoty Radkowic mają osobne manifesty o historycznie różnych strukturach; pierwotny restore obsługiwał tylko pierwszy ZIP.
Options considered: przepisać historyczne manifesty; osobne skrypty; adapter w istniejącym narzędziu.
Selected option: --manifest i --verify-only w research_archive.py, wspólna walidacja przed zapisem.
Reason: zachować niezmienione manifesty i kompatybilność dotychczasowego polecenia.
Trade-offs: trzeba wskazać właściwą parę ZIP–manifest; brak automatycznej kopii zewnętrznej i transakcyjności zapisu. Brak rozmiaru w historycznym manifeście Wolica nie pomija kontroli hash.
Consequences: sprawdzono wszystkie sześć istniejących archiwów, 42 elementy. Nie poszerzono zakresu o prywatne dane ani sekrety. Zewnętrzna kopia nadal niepotwierdzona.

## 2026-09-16 — widok pipeline ograniczony do zachowanej próbki

Decision / Context: udostępnić użyteczne zestawienie trzech wpisów Radkowic bez sugerowania kompletności stacji.
Options considered: sumować jako pełny pipeline projektów; poczekać na pełną deduplikację; jawny widok wierszy jednej publikacji.
Selected option: generator wersjonowanego widoku wierszy PSE, korzystający z istniejącego ekstraktora.
Reason: dostępne dowody potwierdzają umowy, ale nie wykonane przyłączenia ani kompletność ewidencji PGE/PSE.
Trade-offs: obsługiwana interpretacja statusu dotyczy wyłącznie zweryfikowanego tekstu umowy; inne statusy pozostają UNKNOWN. Brak deduplikacji między źródłami.
Consequences: sumy kierunkowych mocy są CALCULATED, liczą rekordy, nie przepływy ani rezerwę MW. Brak podstaw do zamknięcia KSE-021 i przypisywania wpisów do mostu.


## 2026-09-16 — pierwsza lokalna aplikacja oceny przesłanek

Date: 2026-09-16.
Decision / Context: użytkownik zatwierdził aplikację na częściowych dowodach oraz jakościową ocenę przesłanek i ryzyk; porównanie stacji później.
Options considered: czekać na pełny model; wdrożyć pełny stack od razu; ograniczony lokalny adapter i osobna metoda analityczna.
Selected option: lokalny serwer biblioteki standardowej Python, statyczny frontend i metoda documentary_screening_v1 w grid_engine.
Reason: udostępnić zachowane dowody do oceny użytkownika bez nowych zależności i nieuzasadnionego scoringu.
Trade-offs: jeden obszar, brak mapy geograficznej, kont, bazy użytkowników i automatycznych aktualizacji; nie jest serwerem produkcyjnym.
Consequences: scope pilota opisany w docs/17_local_application.md. Pełne zadania KSE-023/024 pozostają osobne. Wolna moc, score i prawdopodobieństwo null. Dane prywatne poza aplikacją. Eksport zachowuje parametry, czas, metodę i zestaw dowodów.


## 2026-09-16 — lokalna kontrola geometrii i pól historycznych

Date: 2026-09-16.
Decision / Context: sprawdzić przekazany historyczny GIS przed integracją analityczną.
Options considered: własny pełny parser WKB; GDAL/GeoPandas; SQLite i Shapely jako opcjonalna zależność badawcza.
Selected option: SQLite tylko do odczytu, minimalny dekoder nagłówka GeoPackage oraz Shapely 2.1.2 do WKB i kontroli geometrii; przypięte zależności w requirements-gis.txt.
Reason: dojrzała walidacja geometrii bez dodatkowego serwera i bez własnej implementacji operacji geometrycznych.
Trade-offs: osobne środowisko GIS; Shapely BSD-3-Clause korzysta z GEOS LGPL-2.1, co wymaga zachowania informacji licencyjnych przy dystrybucji. Lokalna analiza nie nadaje praw do publikacji danych.
Consequences: prywatne wyniki i jawne hashe, bez modyfikacji źródeł. Zgodność XY eksportów nie dowodzi topologii. Historyczne wartości grupowe nie stają się bieżącą mocą stacji. Nierozpoznane zapisy pozostają UNKNOWN i wymagają przeglądu.
Sources checked 2026-09-16: https://shapely.readthedocs.io/en/stable/ oraz https://www.geopackage.org/spec131/#gpb_format .


## 2026-09-17 — rozbieżne daty inwestycji w ocenie aplikacji

Date: 2026-09-17.
Decision / Context: dwie oficjalne publikacje opisują podobnie nazwane zadanie z różnymi latami zakończenia.
Options considered: wybrać nowsze wskazanie; automatycznie połączyć jako jedno zadanie; zachować obie deklaracje i nierozstrzygnięty zakres.
Selected option: wersjonowany przegląd źródeł i jakościowa przesłanka w documentary_screening_v2.
Reason: brak identyfikatora jednostki i dowodu tożsamości zakresu nie pozwala arbitralnie wybrać daty ani wyprowadzać dodatkowych MW.
Trade-offs: nie rozstrzyga daty eksploatacji; potrzebna dalsza weryfikacja operatora.
Consequences: piąty jawny snapshot API, historia i hashe; bez nowego scoringu, zmiany grafu lub danych prywatnych.

## 2026-09-17 — historyczny rekord inwestycji oddzielony od obiektu sieci

Date: 2026-09-17.
Decision / Context: historyczny GIS zawiera warstwy planów, realizacji i modernizacji z datami oraz odsyłaczami do publikacji.
Options considered: bezpośredni import do bieżącego grafu; automatyczne scalanie po nazwie; prywatny rejestr wierszy źródłowych.
Selected option: rejestr wierszy, oryginalne atrybuty, hash i fid; identyfikator kanonicznej inwestycji pozostaje null.
Reason: jeden wiersz może obejmować kilka zadań, a daty i historyczne nazwy warstw nie potwierdzają aktualnej eksploatacji.
Trade-offs: dodatkowa weryfikacja źródeł i rozpoznanie obiektów przed wykorzystaniem w scenariuszach sieci.
Consequences: metoda historical_investment_records_v1, osobna kolejka linków bez pobierania, brak automatycznego dodawania infrastruktury lub MW. Kod i ogólny postęp wersjonowane; dane i ich szczegółowe wyniki pozostają prywatne.


## 17.09.2026 — projekt planu jako osobny dowód przyszłych inwestycji

Date: 2026-09-17.
Decision / Context: pozyskano wydanie PRSP po konsultacjach z terminami dwóch zadań pilota.
Options considered: nadpisać dotychczasowy stan; dopasować automatycznie do mostu; zachować odrębne wpisy projektu planu.
Selected option: odrębny snapshot, status w dokumencie i jawne znaczenie roku zakończenia.
Reason: termin obejmuje także rozliczenie i formalności; zakresy zadań nie mają potwierdzonej tożsamości z innymi wpisami.
Trade-offs: brak automatycznego prognozowania dostępnych MW.
Consequences: dodatkowy widok i materiał w eksporcie; brak zmiany scoringu, grafu ruchowego lub publikowania źródeł prywatnych.

## 2026-09-17 — OSM jako dowód geometrii i kandydatów topologii

Decision: zachować oddzielny, wersjonowany audyt OSM z klasyfikacją źródła G. Context: użytkownik wskazał szczegółową mapę ebin.josm.pl. Options considered: bezpośrednie uznanie mapy za model elektryczny; audyt geometrii przed budową grafu. Selected option: audyt. Reason: brak potwierdzonego układu pracy, parametrów i własności urządzeń. Trade-offs: dodatkowa weryfikacja kosztem szybkości integracji. Consequences: przecięcia przestrzenne nie tworzą potwierdzonych krawędzi; brak nowej punktacji lub MW; dane ODbL pozostają odrębne od prywatnej kompilacji. Główne API OSM wykorzystano jednorazowo do rozpoznania, nie jako planowane zaplecze produkcyjne. Szczegóły: docs/18_gis_osm_integration.md.

## 17.09.2026 — produkt informacyjny bez szacowania przyłączenia

Date: 2026-09-17.
Decision: na wyraźne polecenie użytkownika wyłączyć szacowanie możliwości przyłączenia, rezerwy MW, prawdopodobieństwa WP, obciążenia i Grid Connection Score.
Context: użytkownik nie zakłada uzyskania danych przepływowych operatorów; chce faktów oraz pozytywnych i negatywnych przesłanek do własnej oceny.
Options considered: dalsze dążenie do heurystycznego oszacowania; produkt wspierający decyzję przez wyjaśnione dowody.
Selected option: produkt oparty na faktach i przesłankach, z kategoriami korzystne / ryzyko / neutralne / nieznane.
Reason: decyzja użytkownika i brak podstaw do wiarygodnego rozstrzygania możliwości przyłączenia.
Trade-offs: brak jednego werdyktu lub liczby; użytkownik ocenia znaczenie jawnych dowodów i ograniczeń.
Consequences: dane przepływowe i power-flow poza aktywnym planem. KSE-028/029 zachowane jako historyczne zadania poza zakresem; jakość danych pozostaje aktywna w KSE-023. Nie ponawiać próśb o telemetrię i ekspertyzę. Cytowanie raportowanych przez operatora wartości pozostaje dozwolone z pełnym kontekstem. Nie zmieniono bieżącego API ani historycznych wyników; ustawienie w config/product_policy.json jest specyfikacją, nie flagą wykonawczą.

## 17.09.2026 — agregacja dowodów przed scalaniem obiektów

Date: 2026-09-17.
Decision: wspólny rejestr źródłowych rekordów pilota, z odrębnymi rodzajami i pochodzeniem.
Options considered: łączenie po nazwach; zachowanie oddzielnych zestawów; wspólny rejestr dowodów bez automatycznego scalania.
Selected option: rejestr dowodów.
Reason: umożliwia przegląd danych i późniejsze powiązania, zachowując niepewność tożsamości i różnice źródeł.
Trade-offs: wynik nie jest jeszcze rejestrem unikalnych obiektów.
Consequences: stabilne ID dowodów, cztery snapshoty, jawne OSM G i publikacje B, brak sumowania MW lub oceny możliwości przyłączenia. Szczegóły: docs/20_station_data_aggregation.md.

## 2026-09-18 — Rozpoznawanie ponownie użytych dowodów

- Decision: odróżniać identyczny rekord źródłowy od niezależnego potwierdzenia i od tożsamości urządzenia.
- Options considered: scalanie po nazwie; zgodność identyfikatora; zgodność ID, źródła i snapshotu.
- Selected option: zgodność wszystkich trzech pól dla wpisów projektowych.
- Reason: nie zwiększać pozornie liczby potwierdzeń przez dwa widoki tej samej publikacji.
- Trade-offs: wiele wpisów pozostaje nierozstrzygniętych; potrzebny dalszy przegląd dokumentacyjny.
- Consequences: trzy powiązania SAME_SOURCE_RECORD; bez nowych relacji fizycznych, ocen wpływu ani automatycznego scalania OSM.

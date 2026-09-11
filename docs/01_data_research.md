# Publiczne dane dla Grid Connection Intelligence w Polsce

**Etap 1 — raport badawczy. Data sprawdzenia źródeł: 10 września 2026 r.**

Zakres: PSE, pięciu głównych OSD, przykładowi operatorzy lokalni, źródła administracyjne, GIS, dane europejskie i modele otwarte. Raport dotyczy możliwości zbudowania systemu na podstawie źródeł dostępnych publicznie. Nie zastępuje studium przyłączeniowego operatora. Nie powstał jeszcze model konkretnej stacji, aplikacja ani wynik Grid Connection Score.

## 1. Executive summary

**Tak — można zbudować wiarygodny system rozpoznania sytuacji przyłączeniowej, pod warunkiem ograniczenia jego obietnicy do tego, co potwierdzają źródła.** Dostępne są informacje o projektach, ich etapach, wskazanych miejscach przyłączenia, publikowane przez operatorów moce przyłączeniowe, inwestycje sieciowe oraz część danych systemowych. Można je połączyć z geometrią infrastruktury i uwarunkowaniami przestrzennymi. Wynik powinien wyjaśniać fakty, konflikty i niewiadome dla konkretnego projektu.

**Nie ma podstaw do obietnicy dokładnej wolnej mocy dowolnego GPZ ani liczbowego prawdopodobieństwa uzyskania WP.** W sprawdzonych publicznych źródłach nie znaleziono kompletnego, aktualnego zestawu topologii ruchowej, parametrów elektrycznych, lokalnych profili obciążenia i ograniczeń niezbędnych do takiej oceny. Brak ten jest szczególnie dotkliwy na SN. Nie należy zamieniać niepełnej listy projektów i mocy znamionowej transformatora w pozornie dokładny bilans.

| Poziom sieci | Realistyczny produkt z danych publicznych | Granica dokładności |
|---|---|---|
| **SN** | Rozpoznanie GPZ i udokumentowanych projektów; lokalne warunki/ograniczenia opublikowane przez OSD; analiza przestrzenna kandydatów | Zwykle brak pewnego przypisania do odpływu, aktualnego układu przełączeń, impedancji i profilu obciążenia. Ocena jakościowa, miejscami konkretna informacja operatora; bez wiarygodnej ogólnej estymacji dostępnych MW |
| **110 kV** | Częściowy graf stacji i korytarzy, wskazane miejsca przyłączeń, znany pipeline, ograniczenia obszarowe i plany inwestycji | Możliwe użyteczne analizy lokalne. Niepełna topologia i parametry uniemożliwiają zagwarantowanie przepustowości linii lub transformatora. Moce dla grup stacji nie są niezależnymi mocami każdej stacji |
| **220/400 kV PSE** | Najlepsza podstawa do identyfikacji węzłów, planów rozbudowy, pipeline i interpretacji raportowanych mocy dla wskazanych horyzontów | Nadal nie jest to aktualny model operacyjny. Dane systemowe i transgraniczne nie dostarczają obciążeń wszystkich wewnętrznych elementów. Ocena techniczna konkretnego przyłączenia wymaga danych/studium operatora |

Nie podajemy procentowej „dokładności” dla tych poziomów. Do jej zmierzenia potrzebny jest zbiór referencyjny rzeczywistych obiektów, połączeń i wyników analiz operatora. Dokładność odczytu dokumentu, kompletność pokrycia sieci i trafność oceny przyłączenia to trzy różne miary.

W przeprowadzonych próbach **PSE ma najsilniejszą podstawę do automatyzacji**: otwarte API z dokumentacją oraz rzeczywisty plik XLSX dotyczący przyłączeń. Energa i Stoen udostępniają rozdzielone publikacje dla poboru i wytwarzania; ENEA oferuje przydatne mapy i kryteria SN; TAURON — obszerny wykaz przyłączeń. Dostęp do PGE był blokowany, dlatego jego pokrycia nie można uczciwie ocenić na równi z pobranymi dokumentami. Podstawy tych ocen opisano w rozdziałach 3–4 i w [katalogu źródeł](data_sources.md).

Rekomendacja: przejść następnie do wąskiego pilota dokumentacyjnego, poprzedzonego zamknięciem kwestii licencyjnych i wyborem stacji na podstawie kompletności dowodów. Na tym etapie raportować przesłanki i ryzyka; **Grid Connection Score oraz prawdopodobieństwo pozostawić nieokreślone**, dopóki nie powstanie uzasadniona i sprawdzona metodologia.

## 2. Jak wykonano badanie i jak czytać jego wyniki

Sprawdzono zawartość repozytorium i reguły AGENTS.md. Następnie wyszukiwano źródła pierwotne oraz interfejsy API, REST, WMS, WFS, WMTS, ArcGIS REST, GeoJSON, JSON, CSV, XLSX, XML, HTML, PDF, BIP i repozytoria GitHub. Preferowano dokumenty operatorów i instytucji oraz dokumentację autorów narzędzi. Wynik wyszukiwarki traktowano jako wskazówkę; źródła, których treści nie udało się otworzyć, mają odrębny status.

Badanie obejmuje trzy różne rodzaje dowodu:

1. **Przegląd treści:** odczyt strony, dokumentu lub dokumentacji; nie dowodzi działania pobierania masowego.
2. **Próba techniczna:** lokalne pobranie dokumentu, GetCapabilities lub odpowiedzi API; manifest zachowuje URL, czas UTC, status HTTP, liczbę bajtów i SHA-256.
3. **Kontrola semantyczna próbki:** sprawdzenie, czy odpowiedź rzeczywiście zawiera spodziewane dane, oraz odczyt nagłówków, dat, pól i ograniczeń. Nie jest to walidacja wszystkich wierszy dokumentu.

Katalog rozróżnia `SAMPLE_VERIFIED`, `CONTENT_REVIEWED`, `DOCUMENTATION_REVIEWED`, `DISCOVERED` i `BLOCKED`. `last_verified` oznacza datę sprawdzenia, także nieudanego; `last_successful_verification` pozostaje pusty dla źródeł nieodczytanych. `UNKNOWN` przy API oznacza „nie potwierdzono w tym badaniu”, a nie „nie istnieje”.

W `data/catalog/probe_results_*.json` zachowano wyniki **29 żądań: 28 odpowiedzi HTTP 200 i jedną 404**. Jedna odpowiedź 200 była blokadą PGE. Część pozostałych to dokumentacja lub plik interfejsu, a nie zbiór danych. Nie wolno interpretować tej liczby jako liczby działających connectorów. Kontrola lokalna obejmuje również próbki PDF, XLSX, JSON i XML; wynik znajduje się w `data/catalog/research_validation.json`.

Datę publikacji strony, datę w nazwie pliku, datę stanu wewnątrz dokumentu, okres obserwacji i datę pobrania zapisujemy osobno. Bieżąca strona może prowadzić do wcześniejszego zestawienia. Próbka API bez filtra czasu może zwrócić najstarsze rekordy.

## 3. PSE — najważniejsze źródła i ich rzeczywista użyteczność

### 3.1. Dane o podmiotach i etapach przyłączenia

Pobrany XLSX ma w nagłówku **stan na 31.07.2026**. Zawiera identyfikację obiektu i wnioskodawcy, miejsce/napięcie przyłączenia, kierunki mocy oraz etapy procedury. Pole pojemności MWh nie zostało potwierdzone. Nagłówki są wielowierszowe; puste pola i „-” wymagają jawnego mapowania do braku danych. Wymiary arkusza nie są liczbą unikalnych projektów. Plik jest dobrym kandydatem na pierwszy parser po etapie badań. [PSE — XLSX, sprawdzono 10.09.2026](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx).

Strona wykazu była oznaczona jako zaktualizowana 1 września. Rozbieżność z okresem arkusza trzeba zachować; nie jest automatycznie błędem źródła. [PSE — strona wykazu, sprawdzono 10.09.2026](https://www.pse.pl/obszary-dzialalnosci/wymiana-miedzysystemowa/informacje-ogolne/-/asset_publisher/L3RZBt9EkXoj/content/wykaz-podmiotow-ubiegajacych-sie-o-przylaczenie-do-krajowej-sieci-przesylowej/pop_up).

### 3.2. Publikowane moce przyłączeniowe

PDF ma stan **31.08.2026**, rozróżnia horyzonty i warianty uwzględniania WP OSD. Metodyka obejmuje ograniczenia sieciowe i bilansowe. Wartości dotyczą wskazanych obszarów/stacji oraz założeń publikacji, nie niezależnych rezerw do dowolnego sumowania. Nie należy ponownie odejmować pipeline już uwzględnionego w danym wariancie. Szczególnie ważne: tabela odbiorcza na s. 12 dotyczy **nowych planowanych stacji w perspektywie kolejnych lat**, a nie bieżącej rezerwy importowej wszystkich istniejących stacji. Przejrzano tekst i obraz odpowiedniej strony. [PSE — informacja o dostępności, s. 3–4 i 12–13; sprawdzono 10.09.2026](https://www.pse.pl/documents/20182/51490/informacja_o_dostepnosci_mocy_przylaczeniowej_do_sieci_przesylowej.pdf/81835e70-c6bb-4ed1-8154-1959a45b44f1).

### 3.3. API raportowe

Dokumentacja OpenAPI 2.0.9 i anonimowe zapytania potwierdzają dostęp do specyfikacji węzłów (`specwezlow`), redysponowania (`poze-redoze`) i przepływów (`przeplywy-mocy`). Pierwszy zbiór zawiera m.in. nazwy stacji, napięcia rozdzielni i kody szyn; nie dostarcza sam pełnych krawędzi sieci. Drugi rozdziela przyczyny bilansowe i sieciowe. Trzeci w pobranej próbce dotyczy przekrojów transgranicznych. Dostępne są filtrowanie, wybór kolumn i stronicowanie. Nie ustalono gwarantowanego limitu żądań ani praw do redystrybucji wszystkich serii. [PSE — schemat API, sprawdzono 10.09.2026](https://api.raporty.pse.pl/api/openapi).

Próby `$first=2` sprawdzały interfejs, nie bieżący stan KSE. Zwróciły starsze obserwacje, a pola ograniczeń w próbce miały `null`. Takie wartości nie oznaczają zerowego redysponowania. API udostępnia dane raportowane; określenie `MEASURED` wymaga dodatkowej wiedzy o pochodzeniu konkretnego pola. [PSE — próbka węzłów](https://api.raporty.pse.pl/api/specwezlow?$first=2), [próbka redysponowania](https://api.raporty.pse.pl/api/poze-redoze?$first=2), [próbka przepływów](https://api.raporty.pse.pl/api/przeplywy-mocy?$first=2), sprawdzono 10.09.2026.

### 3.4. Topologia i przyszła sieć

Plan rozwoju 2027–2036 dostępny w badaniu jest oznaczony jako **projekt po konsultacjach**. Należy przechowywać status dokumentu i osobno etapy realizacji inwestycji. Nie daje on podstaw do traktowania wszystkich zamierzeń jako istniejącej infrastruktury. [PSE — projekt PRSP, sprawdzono 10.09.2026](https://www.pse.pl/documents/20182/7102190804/PRSP_2027-2036-dokument_glowny_projekt_po_konsultacji.pdf/de2f004f-8a80-4264-907a-a38d52c5d50f).

Publiczna dokumentacja wymiany strukturalnej B2B nie jest dowodem anonimowego dostępu do operacyjnego modelu sieci. Nie potwierdzono takiego dostępu. Otwarty adres dokumentacji `grid-struct-api` zapisano jako wskazówkę do weryfikacji uprawnień, nie jako działający connector. [PSE — dokumentacja interfejsu strukturalnego; próba dostępu 10.09.2026](https://polskie-sieci-elektroenergetyczne.github.io/grid-struct-api/).

## 4. Operatorzy dystrybucyjni

### 4.1. Energa-Operator

Oficjalna strona prowadzi do osobnych publikacji dotyczących mocy wytwórczej, odbiorczej i procesu przyłączeń. To pozwala od początku rozdzielić ocenę eksportu i importu BESS. Pobrane dwa dokumenty mocy mają nagłówki z 31.08.2026. Automatyzacja: śledzenie linków HTML, archiwizacja PDF, parser tabel zachowujący nagłówki i jednostki. Nie potwierdzono otwartego API ani GIS z operacyjną topologią. [Energa — stan przyłączeń, sprawdzono 10.09.2026](https://energa-operator.pl/przylaczenie-do-sieci/informacje-o-stanie-przylaczen).

Publikowane moce należy wiązać z dokładną jednostką raportowania i wariantem źródłowym. Zestawienia nie są pomiarem chwilowego wykorzystania linii czy transformatorów. [Energa — moce wytwórcze](https://cdn-netpr.pl/file/mediakit/3063621/4a/informacja_o_wartosci_lacznej_dostepnej_wytworczej_mocy_przylaczeniowej_31_08_2026.pdf), [moce odbiorcze](https://cdn-netpr.pl/file/mediakit/3063619/5c/informacja_o_wartosci_lacznej_dostepnej_odbiorczej_mocy_przylaczeniowej_31_08_2026.pdf), sprawdzono 10.09.2026.

**Konflikt do wyjaśnienia:** nazwa pliku pipeline wskazuje 31.08.2026, ale nagłówek pierwszej strony i metadane odwołują się do 30.06.2026. Zachowano oba dowody. Do czasu wyjaśnienia nie wolno prezentować danych jako pewnego stanu sierpniowego. [Energa — wykaz wniosków i odmów, s. 1; sprawdzono wizualnie 10.09.2026](https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf).

Plan 2026–2031 jest opisany jako uzgodniony. Może zasilać rejestr przyszłych inwestycji, lecz planowana data nie jest potwierdzeniem oddania do ruchu. [Energa — plan rozwoju i status, sprawdzono 10.09.2026](https://energa-operator.pl/raporty-i-liczby/plan-rozwoju).

### 4.2. ENEA Operator

Strona przyłączeń zawiera aktualizowane wykazy i kryteria SN, w tym informacje dla wybranych GPZ. Nie należy przenosić lokalnych kryteriów na całą sieć. Linki do najnowszych części wykazu odnaleziono, ale w tym etapie nie wykonano pełnej walidacji ich wierszy. [ENEA — informacje o przyłączeniach, sprawdzono 10.09.2026](https://www.operator.enea.pl/przylaczenie-do-sieci/informacje-o-przylaczeniach).

Na stronie map potwierdzono osadzenia Power BI. Operator deklarował w styczniu 2026 codzienną aktualizację. Jest to przydatny interfejs analityczny, ale osadzenie nie jest udokumentowanym publicznym API ani WFS. Nie potwierdzono trwałego, dozwolonego interfejsu eksportu całego zbioru. Nie należy utożsamiać codziennej aktualizacji z telemetrią. [ENEA — mapy](https://www.operator.enea.pl/przylaczone-i-dostepne-moce-oze), [komunikat o aktualizacji](https://media.enea.pl/pr/863306/enea-operator-codziennie-publikuje-aktualne-dane-dotyczace-oze-dla-inwestorow), sprawdzono 10.09.2026.

Plan 2026–2031 jest przedstawiony jako uzgodniony z URE. To źródło inwestycji, nie dynamicznych przepływów. [ENEA — plan rozwoju, sprawdzono 10.09.2026](https://www.operator.enea.pl/plan-rozwoju-enea-operator-na-lata-2026-2031).

### 4.3. TAURON Dystrybucja

Pobrano rzeczywisty 99-stronicowy PDF wykazu. W próbce występują zanonimizowane oznaczenia wnioskodawców i miejsca przyłączenia jeszcze nieokreślone. Nie ma więc podstaw do obietnicy pełnej identyfikacji wszystkich SPV ani automatycznego przypisania każdego wniosku do stacji. Rozmiar dokumentu uzasadnia sprawdzanie zmian i cache zamiast wielokrotnych pobrań. [TAURON — wykaz, sprawdzono 10.09.2026](https://www.tauron-dystrybucja.pl/-/media/offer-documents/dystrybucja/przylaczenie/dostepne-moce/informacja-o-przylaczanych-obiektach-i-wydanych-odmowach.ashx).

Portal dostępnych mocy i strona planu są dodatkowymi źródłami. Nie potwierdzono publicznego API do pełnego pobierania danych portalu. Wyświetlane możliwości i inwestycje wymagają odczytania właściwego scenariusza oraz zastrzeżeń operatora. [TAURON — portal](https://dostepnemoce.tauron-dystrybucja.pl/), [plan rozwoju](https://www.tauron-dystrybucja.pl/plan-rozwoju), sprawdzono 10.09.2026.

### 4.4. Stoen Operator

Strona sieci udostępnia moce eksportowe i odbiorcze, wykazy procedur, rejestr magazynów oraz plan rozwoju. Pobrano PDF eksportowy III kwartału 2026 i odbiorczy z 31.08.2026. Pozostałe linki zapisano w katalogu ze słabszym statusem weryfikacji. [Stoen — sieć, sprawdzono 10.09.2026](https://www.stoen.pl/pl/strona/siec).

Eksport jest opisany m.in. dla dzielnic/grup stacji i poziomów 110/15 kV. Dokument zawiera założenia dotyczące pracy źródła oraz starszych danych o małych instalacjach. Data wydania nie gwarantuje tej samej świeżości wszystkich wejść do obliczeń operatora. [Stoen — eksport III kw. 2026, s. 3–5; sprawdzono 10.09.2026](https://www.stoen.pl/files/2026-07/wielkosc-dostepnej-mocy-przylaczeniowej-zrodel-w-sieci-stoen-operator-iii-kw-2026.pdf).

Występuje konkretna kwestia prawna: §6 regulaminu zastrzega komercyjne wykorzystanie informacji poza wskazanymi wyjątkami i wymaga uprzedniej zgody. Przed produkcyjnym pobieraniem/redystrybucją trzeba wyjaśnić zakres zastosowania do wybranych publikacji i ustawowego ponownego wykorzystania. W badaniu nie uzyskano takiej zgody. [Stoen — regulamin, sprawdzono 10.09.2026](https://www.stoen.pl/strona/regulamin).

### 4.5. PGE Dystrybucja

Adres strony dostępnych mocy odpowiadał HTTP 200, ale treścią była krótka informacja o odrzuceniu działania. Zachowano ją jako dowód blokady. Wyszukiwanie wskazało PDF mocy z I kwartału 2026 i projekt planu rozwoju, lecz treści tych dokumentów nie udało się wiarygodnie odczytać. **Nie potwierdzamy ich parametrów, aktualności ani możliwości automatycznego pobierania.** Nie próbowano obchodzić zabezpieczeń. Następny krok to zwykły dostęp przeglądarkowy albo uzgodnienie oficjalnego kanału danych. [PGE — badana strona, próba 10.09.2026](https://pgedystrybucja.pl/przylaczenia/procedury-przylaczeniowe/dostepne-moce-dla-zrodel-wytworczych).

### 4.6. Mniejsi operatorzy i pokrycie projektów odbiorczych

KGHM publikuje informacje o swojej działalności OSD, dostępnych mocach, przyłączeniach, odmowach i magazynach. To wartościowy przykład sieci przemysłowej, którą trzeba wiązać z nadrzędnym OSD/OSP. Nie można zakładać, że pięciu dużych OSD obejmuje wszystkie przyłączenia przemysłowe. [KGHM — OSD, sprawdzono 10.09.2026](https://kghm.com/pl/biznes/strefa-energetyczna/osd-dla-systemu-elektroenergetycznego).

Data center, elektrolizery i duże odbiory należy poszukiwać w wykazach odbiorczych, dokumentach administracyjnych oraz publikacjach inwestora. Anonimizacja i brak jednoznacznego pola technologii ograniczają rozpoznawalność. Brak projektu w publicznym wykazie nie dowodzi braku konkurencji o sieć.

## 5. Rejestry administracyjne i odkrywanie projektów

[BIP URE — rejestry i bazy, sprawdzono 10.09.2026](https://bip.ure.gov.pl/bip/rejestry-i-bazy) daje punkty wejścia do rejestrów regulacyjnych, w tym małych instalacji OZE. Mogą potwierdzać podmiot lub określony status działalności. Nie są kompletną mapą połączeń projekt–GPZ. Różne progi i zakresy rejestrów wymagają zachowania ich definicji. Raporty o odmowach nie stanowią automatycznie zbioru niezależnych obserwacji do wyliczania szans pojedynczego projektu.

BIP gmin, RDOŚ i dokumenty środowiskowe mogą dostarczyć lokalizację, działki, nazwę inwestora i parametry zamierzenia. Obwieszczenie o wszczęciu postępowania nie potwierdza pozwolenia, WP ani realizacji. Jeden projekt może występować pod kilkoma nazwami i numerami spraw. Potrzebny jest parser konkretnego serwisu oraz ręczna kontrola dopasowań. W tym etapie nie zbudowano kompletnego indeksu BIP ani nie potwierdzono krajowego API całego pipeline. [Ekoportal — punkt wejścia, dostęp w badaniu niepełny; sprawdzono 10.09.2026](https://ekoportal.gov.pl/).

Publiczna dokumentacja KRS jest potencjalnym uzupełnieniem identyfikacji SPV, ale nie dowodzi związku spółki z projektem ani beneficjentem sieciowym. W tym badaniu nie wykonano zapytań o podmioty. [KRS — punkt wejścia OpenAPI, sprawdzono 10.09.2026](https://prs.ms.gov.pl/krs/openApi).

Nowelizacja Prawa energetycznego opublikowana w Dz.U. 2026 poz. 516 rozróżnia w treści dotyczącej aktualizacji publikacji co najmniej miesięczną częstotliwość OSP i kwartalną OSD. Nie należy wpisywać w katalogu wszystkim operatorom identycznego ustawowego cyklu miesięcznego; dodatkowo trzeba badać faktyczną praktykę. To ustalenie zakresu źródła, nie pełna opinia prawna o wszystkich obowiązkach operatorów. [Dziennik Ustaw — tekst, s. 15; sprawdzono 10.09.2026](https://dziennikustaw.gov.pl/D2026000051601.pdf).

## 6. Dane przestrzenne

Warstwa GIS może wykluczać ewidentnie problematyczne korytarze i wspierać wybór kandydatów. Nie wyznacza samodzielnie możliwej do uzyskania służebności, warunków przekroczenia drogi ani wykonalności przyłącza.

| Źródło i data kontroli | Potwierdzony interfejs / zawartość | Ograniczenie |
|---|---|---|
| [GUGiK EGiB WFS](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza?SERVICE=WFS&REQUEST=GetCapabilities), 10.09.2026 | Pobrany i poprawny XML GetCapabilities WFS 2.0; geometria i identyfikacja działek/budynków w zintegrowanym zasobie | Nie potwierdzono w tej próbie GetFeature ani pełnego krajowego pobrania. Publiczna geometria nie daje informacji o właścicielu i tytule prawnym |
| [BDOT10k](https://www.geoportal.gov.pl/pl/dane/baza-danych-obiektow-topograficznych-bdot10k/), 10.09.2026 | Pakiety danych i usługa WMS do pobierania; drogi, kolej, obiekty topograficzne | Parametry sieci elektrycznej i stan łączników nie wynikają z topografii |
| [BDOT10k — GeoParquet](https://www.geoportal.gov.pl/aktualnosci/nowy-sposob-udostepniania-danych-bdot10k-w-geoportalu/), 10.09.2026 | Oficjalnie udostępniony format od kwietnia 2026, podział na klasy | Nie pobierano wielkich paczek; schemat, aktualność i kompletność poszczególnych klas wymagają sprawdzenia |
| [Ortofotomapa](https://www.geoportal.gov.pl/pl/dane/ortofotomapa-orto/), 10.09.2026 | WMS/WMTS i pobieranie; strona opisuje bezpłatne wykorzystanie | Data zdjęcia różna od daty pobrania; widoczny przewód nie potwierdza napięcia ani połączenia elektrycznego |
| [NMT](https://www.geoportal.gov.pl/pl/dane/numeryczny-model-terenu-nmt/), 10.09.2026 | Pliki wysokościowe/usługi opisane przez GUGiK | Rozdzielczość, pionowy układ odniesienia i aktualność wymagają zachowania w metadanych |
| [Integracja MPZP](https://mapy.geoportal.gov.pl/wss/ext/KrajowaIntegracjaMiejscowychPlanowZagospodarowaniaPrzestrzennego?lang=pol), 10.09.2026 | Zintegrowane prezentowanie planów | Obraz mapy nie zastępuje tekstu uchwały i ustaleń konkretnej gminy |
| [Rejestr Urbanistyczny](https://rejestr-urbanistyczny.gov.pl/published), 10.09.2026 | Otwarty interfejs strony | Nie potwierdzono kompletności, eksportu i stabilnego publicznego API; nie uznano go za gotowy krajowy connector |
| [GDOŚ WFS](https://sdi.gdos.gov.pl/wfs?SERVICE=WFS&REQUEST=GetCapabilities), 10.09.2026 | Potwierdzone GetCapabilities; chronione obszary i Natura 2000 | Usługa nie zastępuje aktów ustanawiających ochronę; nie przeprowadzono walidacji wszystkich geometrii |
| [Wody Polskie — SIGW](https://www.gov.pl/web/wody-polskie/udostepnianie-danych-z-systemu-informacyjnego-gospodarowania-wodami), 10.09.2026 | Przeglądanie map/usługi i procedura uzyskania danych, w tym zagrożenie powodziowe | Dostęp do przeglądania nie oznacza dowolnego bezpłatnego pobierania każdego produktu; zakres i odpłatność zależą od sposobu udostępnienia |
| [Bank Danych o Lasach — OGC](https://www9.bdl.lasy.gov.pl/portal/uslugi-ogc?v=1), 10.09.2026 | Dokumentacja WFS, WMS i WMTS, także adresy usług ArcGIS | Nie wykonano próby masowego pobierania; własność i możliwość wyłączenia gruntu z produkcji wymagają osobnych ustaleń |

Trzeba zachować CRS oryginału i jawnie transformować współrzędne; w Polsce występuje m.in. EPSG:2180. EPSG:4326 może być wspólnym układem wymiany, ale pomiar odległości należy wykonywać w odpowiednim układzie metrycznym. Kolejność osi WMS/WFS zależy od wersji protokołu i CRS. WMS/WMTS prezentują obraz, WFS może udostępniać obiekty; nie są zamienne jako źródła grafu.

## 7. Źródła europejskie, otwarte modele i biblioteki

### 7.1. Dane systemowe

ENTSO-E Transparency Platform oferuje dane systemowe o generacji, zapotrzebowaniu, wymianie i innych zdarzeniach. REST API wymaga tokenu; nie wykonano uwierzytelnionego zapytania. Dokumentacja z kwietnia 2026 wskazuje limit 400 żądań/minutę na token w opisanej wersji platformy. Zastosowanie: kontekst krajowy/strefowy i kontrola zgodności szeregów, nie lokalna telemetria GPZ. [ENTSO-E — platforma](https://www.entsoe.eu/data/transparency-platform/), [token](https://transparencyplatform.zendesk.com/hc/en-us/articles/12845911031188-How-to-get-security-token), [limit](https://transparencyplatform.zendesk.com/hc/en-us/articles/12783148966036-API-Rate-Limit-Part-1), sprawdzono 10.09.2026.

Warunki prawne odsyłają do listy danych dopuszczonych do ponownego wykorzystania. Nie wolno rozciągać licencji określonej kategorii na całą platformę ani na osobną mapę sieci. [ENTSO-E — warunki](https://transparencyplatform.zendesk.com/hc/en-us/articles/40921911218961-Legal-Terms-and-Conditions), sprawdzono 10.09.2026.

Energy-Charts udostępnia OpenAPI i działające anonimowe zapytanie `v2/public_power` dla `country=pl`; pobrano próbkę dobową. Odpowiedź v2 zawiera `series` i obserwacje `data.timestamp/values`, a także metadane CC BY 4.0 z atrybucją energy-charts.info. Nie należy przenosić tej informacji automatycznie na wszystkie pozostałe produkty. Ember ma interfejs API i rejestrację, lecz nie wykonano zapytania z kluczem. Żadne z tych źródeł nie rozwiązuje braków lokalnych przepływów. [Energy-Charts — próbka z metadanymi](https://api.energy-charts.info/v2/public_power?country=pl&start=2026-09-01&end=2026-09-01), [schemat](https://api.energy-charts.info/openapi.json), [Ember — dokumentacja](https://api.ember-energy.org/v1/docs), sprawdzono 10.09.2026.

Open Power System Data ma użyteczne historyczne szeregi, ale przejrzana paczka `time_series` jest wydaniem z 2020 r. JRC IDEES-2023 obejmuje historyczną strukturę zużycia energii, nie aktualną sieć przyłączeniową. Nie należy traktować świeżej daty publikacji metadanych jako świeżości wszystkich obserwacji. [OPSD — time series](https://data.open-power-system-data.org/time_series/), [JRC IDEES](https://data.jrc.ec.europa.eu/dataset/1f0b480c-6d21-4d95-897d-20c7ca33df6f), sprawdzono 10.09.2026.

Copernicus może wspomóc analizę terenu, pokrycia ziemi i przyszłe modele profili, ale nie publikuje parametrów transformatorów. Dokumentacja opisuje OData i inne kanały; autoryzacja i limity zależą od usługi. Licencja produktu Sentinel, DEM i treści samego portalu nie musi być identyczna. [Copernicus — OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html), [warunki](https://dataspace.copernicus.eu/terms-and-conditions), [limity](https://documentation.dataspace.copernicus.eu/Quotas.html), sprawdzono 10.09.2026.

### 7.2. Czy istnieje gotowy model topologii Polski?

Istnieją materiały do zbudowania **grafu referencyjnego**, ale w badaniu nie potwierdzono gotowego publicznego modelu odpowiadającego bieżącej polskiej sieci operacyjnej i wszystkim potrzebom przyłączeniowym.

| Źródło, sprawdzone 10.09.2026 | Możliwe zastosowanie | Czego nie dowodzi |
|---|---|---|
| [ENTSO-E Grid Map](https://www.entsoe.eu/data/map/downloads/) | Mapa przeglądowa sieci przesyłowej; dostępne wydanie opisane jako aktualizowane w 2024 r. | Układu ruchowego i parametrów każdego elementu w 2026 r. |
| [OpenStreetMap](https://www.openstreetmap.org/copyright), [Geofabrik Polska](https://download.geofabrik.de/europe/poland.html) | Geometria obiektów i tagi; regionalny PBF zamiast agresywnego odpytywania publicznego Overpass | Kompletności, poprawności napięć, mocy transformacji lub stanu łączników; ODbL nakłada obowiązki |
| [OpenInfraMap](https://openinframap.org/about) | Czytelny podgląd warstwy energetycznej OSM | Niezależnego potwierdzenia OSM — to wizualizacja tych samych danych |
| [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur), [publikacja o budowie modelu z OSM](https://arxiv.org/abs/2408.17178) | Powtarzalne przygotowanie modelu europejskiego; wzorce budowania topologii i przypisywania parametrów | Że estymowane parametry są danymi polskiego operatora; zgodność agregatów nie waliduje pojedynczego GPZ |
| [MATPOWER case2383wp](https://github.com/MATPOWER/matpower/blob/master/data/case2383wp.m) | Testy algorytmów na historycznym przypadku polskiej sieci | Aktualności: opis dotyczy zimy 1999/2000, zawiera uproszczenia i agregacje; nie nadaje się na bieżącą mapę konkurencji o przyłączenie |

Łączenie tych danych wymaga przechowywania źródłowych identyfikatorów i pochodzenia każdej krawędzi. Geometria przecinających się linii nie oznacza ich elektrycznego połączenia. Połączenie stacji przez OSM, skorygowane na podstawie mapy operatora, nadal wymaga jawnego poziomu pewności i wskazania dowodów.

### 7.3. Biblioteki — ocena przydatności, bez dodawania zależności

| Narzędzie, sprawdzone 10.09.2026 | Zastosowanie po spełnieniu warunków | Decyzja etapu 1 |
|---|---|---|
| [pandapower](https://github.com/e2nIEE/pandapower) | Analiza rozpływów przy kompletnych parametrach i założeniach | Kandydat do późniejszej walidacji; wbudowane przykłady nie są aktualnym modelem Polski |
| [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) | Scenariusze systemowe i przygotowanie modeli | Przeanalizować metody, zachować licencje poszczególnych danych niezależnie od kodu |
| [GridCal / VeraGrid](https://github.com/SanPen/VeraGrid) | Narzędzia analizy sieci; repozytorium obecnie pod nazwą VeraGrid, licencja MPL-2.0 | Alternatywa do porównania dopiero z rzeczywistym przypadkiem testowym |
| [MATPOWER](https://github.com/MATPOWER/matpower) | Referencyjne obliczenia i przypadki testowe | Benchmark, nie źródło aktualnego KSE |
| [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) | Formułowanie problemów optymalizacji sieci | Dodatkowy stos Julia nie jest uzasadniony dla etapu dokumentacyjnego |

Dobór solvera nie usuwa braku danych wejściowych. Warunki licencyjne kodu należy sprawdzać dla przypiętej wersji, a danych — osobno. Nie instalowano tych bibliotek ani nie uruchamiano obliczeń rozpływowych.

## 8. Czy można odtworzyć project → feeder → GPZ → 110 kV → SE PSE?

**Częściowo, dla wybranych projektów i odcinków. Nie wykazano możliwości kompletnego odtworzenia tego łańcucha w całej Polsce.**

| Relacja | Dostępny dowód | Zasada modelowania |
|---|---|---|
| Projekt → punkt wskazany w wykazie | Nazwa stacji/linii, napięcie, etap procedury | Relacja `confirmed` wyłącznie w zakresie treści dokumentu; WP nie oznacza fizycznego przyłączenia działającego projektu |
| Projekt → odpływ SN | Niekiedy dokument lokalny lub techniczne warunki | Przy braku dokumentu `unknown`; najbliższy przewód nie wystarcza |
| Odpływ → GPZ | Lokalne schematy i dane operatora, jeśli dostępne | Sam przebieg linii na mapie zwykle nie rozstrzyga układu zasilania |
| GPZ → sieć 110 kV | Dokumenty operatora, mapy i OSM jako pomoc | Rozdzielić dowód przebiegu od połączenia elektrycznego i od bieżącego stanu łączników |
| Sieć 110 kV → SE PSE | Wskazane stacje i transformacja, dokumenty inwestycji | Nie przypisywać wszystkich projektów do najbliższej SE PSE; możliwe wiele dróg zasilania |

Każda krawędź powinna posiadać typ, status pewności, źródło, daty ważności i rozróżnienie obecnego/planu. Nieznana krawędź może pozostać nieznana; graf nie musi sztucznie stać się spójny. Mapowanie nazw GPZ/SE wymaga operatora, napięcia, lokalizacji i identyfikatorów. Dopasowanie rozmyte nazwy może podpowiedzieć kandydatów, lecz nie może samo scalić obiektów.

## 9. Obciążenie, wolna moc i konkurencja

### Co można policzyć odpowiedzialnie

Można agregować **znaną, udokumentowaną** moc projektów według potwierdzonego punktu/grupy, daty, statusu i kierunku. Warunkiem jest deduplikacja oraz rozdzielenie mocy zainstalowanej od limitu PCC. Taki agregat opisuje zakres publikacji, nie pełny rzeczywisty pipeline i nie jednoczesny przepływ. Wnioski, WP i umowy są etapami tego samego projektu, a nie zawsze osobnymi projektami do dodania.

Można odczytać raportowaną dostępność operatora razem z horyzontem i definicją. Gdy brak kompletnego modelu, **nie można niezależnie odtworzyć tej wartości** prostym odejmowaniem mocy. Znane odmowy są sygnałem historycznym z określonym powodem; nie dowodzą uniwersalnego zakazu przyłączenia wszystkich technologii w okolicy.

### Czego brakuje do modelu elektrycznego

Nie znaleziono kompletnego publicznego pokrycia impedancji, limitów sezonowych, rzeczywistych profili lokalnego poboru/generacji, nastaw regulacji, układów przełączeń i listy ograniczeń N-1. Dlatego nie potwierdzono możliwości wiarygodnego wyznaczania rzeczywistego obciążenia każdego transformatora GPZ, linii 110 kV ani lokalnego marginesu napięciowego.

Nawet przy znanej mocy znamionowej MVA nie wolno utożsamiać jej z dostępnymi MW. Wpływ mają moc bierna, napięcie, warunki pracy, pozostała sieć i scenariusz awaryjny. Suma przyłączeń nie jest pomiarem obciążenia. Systemowy curtailment może wynikać z bilansowania KSE; nie należy przypisywać go konkretnemu GPZ bez dowodu lokalizacji i przyczyny.

### Estymacje i ich warunki dopuszczenia

Modele profili OZE, zastępcze profile poboru czy orientacyjne parametry linii mogą być badane jako `ESTIMATED`. Muszą mieć jawne wejścia, metodę, zakres zastosowania i analizę wrażliwości. Nie znaleziono podstaw do narzucenia jednego błędu procentowego takiego modelu dla całej Polski. Jeśli brakuje danych pozwalających ograniczyć wynik, poprawną odpowiedzią jest `UNKNOWN`, a nie arbitralnie szeroki przedział MW.

Warianty `CONSERVATIVE` i `OPTIMISTIC` muszą różnić się uzasadnionymi założeniami, nie dowolnym mnożnikiem wyniku. Planowana inwestycja może być scenariuszem przyszłym z datą i statusem realizacji; nie powiększa obecnej dostępności. Na tym etapie nie policzono żadnego wyniku mocy ani scoringu dla rzeczywistej stacji.

### BESS i hybrydy

BESS wymaga osobnych `P_export_MW`, `P_import_MW`, `energy_capacity_MWh`, limitów PCC oraz scenariuszy ładowania i rozładowania. Publiczne wykazy coraz lepiej rozdzielają kierunki, lecz nie potwierdzono kompletnego pokrycia MWh ani strategii pracy. MWh nie można wywnioskować z samych MW. Hybryda z ograniczeniem PCC nie ma automatycznie eksportu równego sumie mocy wszystkich urządzeń. Potencjalna elastyczność BESS jest warunkowa: wymaga akceptowalnego sposobu sterowania i warunków przyłączenia, nie uzasadnia automatycznej premii punktowej.

## 10. Licencje i możliwość automatyzacji

**Potwierdzono działanie części kanałów technicznych; nie potwierdzono kompletnego prawa do komercyjnego wykorzystania wszystkich potrzebnych danych.** To dwa niezależne warunki wejścia do MVP.

| Grupa źródeł | Stan ustaleń prawnych | Konsekwencja |
|---|---|---|
| PSE i OSD | Publiczne publikacje nie mają w każdym przypadku znalezionej jawnej licencji otwartych danych; Stoen zawiera konkretne zastrzeżenie regulaminowe | Ustalić podstawę ponownego wykorzystania wybranych faktów/zbiorów, automatyzacji i redystrybucji; zachować ograniczenia w rejestrze |
| OSM / OpenInfraMap / Geofabrik | ODbL, obowiązki atrybucji i warunki dla baz pochodnych | Zaprojektować rozdzielenie pochodzenia; nie zakładać, że połączenie z własnymi danymi usuwa zobowiązania |
| ENTSO-E | Lista dopuszczonych danych i wyjątków | Sprawdzić konkretny typ danych oraz dostawcę; mapa i API nie mają automatycznie wspólnej licencji |
| GUGiK / GDOŚ / Wody Polskie / BDL | Zróżnicowane zasady produktu i dostępu; ortofotomapa ma jasny opis swobodnego użycia | Nie przenosić licencji jednej warstwy na EGiB, wszystkie produkty wodne lub dane właścicielskie |
| Copernicus | Warunki produktu i usługi, osobne warunki treści portalu | Sprawdzać wybrany produkt; dostęp do konta i limit usługi nie określają same praw do danych |
| Biblioteki i modele | Licencja kodu odrębna od wejściowych danych oraz konkretnego przypadku sieci | Przypiąć wersję i licencję przed zależnością produkcyjną |

Nie wysyłano wniosków o zgodę ani wiadomości do operatorów. Nie obchodzono blokad i nie wykonano masowego scrapingu. Dla źródeł bez jasnej podstawy `commercial_use=UNKNOWN` jest świadomą, nierozstrzygniętą pozycją rejestru, a nie dorozumianą zgodą. Przed stałym scraperem trzeba jeszcze sprawdzić regulamin, `robots.txt`, limity i preferowany oficjalny kanał dla konkretnej ścieżki; ten etap nie stanowi pełnego audytu prawnego.

## 11. Jak często aktualizować dane

Poniższe okresy to **proponowana polityka przyszłego systemu**, a nie pomiar częstotliwości każdego źródła. Rzeczywista częstotliwość publikacji jest opisana osobno w katalogu.

| Rodzaj | Proponowane sprawdzanie | Zasada |
|---|---|---|
| Wykazy przyłączeń i dostępności | Raz dziennie lekka kontrola strony/wersji, pobranie tylko po zmianie | Snapshot także wtedy, gdy nazwa pliku jest stała; nie zmieniać daty obserwacji przy samym ponownym pobraniu |
| PSE / ENTSO-E szeregi | Według faktycznej rozdzielczości i potrzeb analizy, z oknem na korekty | Stronicowanie, filtry czasu, cache, retry z backoff i limity; zachować wersje skorygowanych obserwacji |
| Plany rozwoju i inwestycje | Co tydzień oraz przy publikacji zmian | Osobno projekt, plan uzgodniony i potwierdzenie realizacji |
| BIP dla pilota | Ostrożna kontrola wybranych serwisów, np. dzienna po uzgodnieniu dostępu | Nowe obwieszczenie nie zmienia automatycznie zaawansowania całego projektu |
| OSM/GIS topografia | Według wersji dostawcy i potrzeb, zwykle okresowe snapshoty | Nie pobierać ponownie całego kraju do każdego raportu |

System historyczny można wiarygodnie rozpocząć od własnych snapshotów. Nie wolno obiecać rekonstrukcji stanu sprzed trzech miesięcy, jeżeli źródło nie zachowało tamtej wersji. Manifest pobrania i wersja metody pozwalają odtworzyć „co wiedzieliśmy”, co nie musi być identyczne z rzeczywistym stanem sieci w tej dacie.

## 12. Największe luki i sposoby ich zamykania

1. **Topologia i telemetria SN/110 kV.** Najważniejsza droga to dane operatora lub dokumenty konkretnego inwestora. Geometria otwarta może wspierać hipotezy, lecz nie zastąpi tych danych.
2. **Kompletność pipeline i tożsamość projektów.** Potrzebne łączenie wykazów, dokumentów administracyjnych i publikacji inwestorów, z zachowaniem anonimizacji i niejednoznaczności.
3. **Definicje raportowanych mocy.** Przed agregacją trzeba modelować wspólne grupy ograniczeń, kierunki, warianty WP i horyzonty. Brak definicji blokuje obliczenie, nie usprawiedliwia uproszczenia.
4. **Daty i aktualność.** Konflikt Energi oraz różnica dat strony/arkusza PSE pokazują konieczność kontroli treści. Nie wystarczy monitorować nazwy pliku.
5. **Prawa i stabilność dostępu.** PGE pozostaje blokadą techniczną; Stoen ma zastrzeżenia komercyjne; brak licencji wielu publikacji wymaga wyjaśnienia przed produkcją.
6. **Dane referencyjne do walidacji wyniku.** Bez nich nie da się obronić procentowej pewności, prawdopodobieństwa WP ani wag wyniku 0–100.

## 13. Rekomendacja po etapie 1

Aktualizacja 11.09.2026: użytkownik wskazał Radkowice. [Analiza pilota](10_radkowice_pilot.md) dokumentuje trzy wiersze BESS z zachowanego XLSX PSE oraz nowe źródła: [portal inwestycji PSE](https://inwestycje.pse.pl/) i [BIP Chęcin](https://checiny.biuletyn.net/fls/bip_pliki/2026_03/BIPF64CD10561EC15Z/PZCEEPG_2025-2027.pdf), odczytane 11.09.2026. Rejestr rozszerzono do 58 źródeł. Wcześniejsza walidacja 56 źródeł jest historycznym wynikiem etapu 1, nie kontrolą nowych pozycji. Rekomendujemy Radkowice do dalszej pracy dokumentacyjnej; granice PSE/PGE i prawa źródeł pozostają do wyjaśnienia.

Zasadne jest przygotowanie pilota **evidence-based screening**: wybór punktu, parametry projektu, odczyt źródeł, znane projekty według kierunku i etapu, planowane inwestycje, graf tylko z uzasadnionymi relacjami i lista braków. PSE jest dobrym początkiem warstwy pobierania; do lokalnego rozszerzenia warto rozważyć obszar Energi lub ENEA po ocenie konkretnej stacji i wyjaśnieniu dostępu/licencji. Nie wybrano jeszcze regionu na podstawie samej atrakcyjności mapy.

Warunek wyboru pilota: co najmniej jedna jednoznacznie zidentyfikowana stacja, udokumentowane relacje z siecią 110 kV/PSE, kilka rzeczywistych projektów z czytelnym statusem, źródło inwestycji oraz możliwość kontroli przynajmniej części danych u źródła. Jeśli brakuje danych elektrycznych, raport nie wyświetli obliczonej rezerwy MW.

Wstępne rozdzielenie możliwości zawiera [macierz wykonalności](02_feasibility_matrix.md). Dalszy zakres MVP, wybór architektury i ewentualny PoC wymagają kolejnego etapu uzgodnionego z użytkownikiem. Pierwsze badanie nie uzasadnia budowy ogólnopolskiego kalkulatora prawdopodobieństwa przyłączenia. Uzasadnia budowę systemu, który rzetelnie pokazuje **co wiadomo, skąd to wiadomo i czego jeszcze trzeba się dowiedzieć**.

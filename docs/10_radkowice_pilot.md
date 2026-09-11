# Pilot: SE Radkowice 220/110 kV

Weryfikacja: **11.09.2026**. Rekomendacja: przyjąć wskazane przez użytkownika Radkowice jako stację pilota dokumentacyjnego. Istnieją konkretne dowody projektów BESS, inwestycji i połączeń przesyłowych. Nie ma obecnie podstaw do zmiany na inną stację tylko ze względu na łatwiejszą mapę.

## Tożsamość i granice

PSE opisuje obiekt jako **stację 220/110 kV Radkowice** ([źródło PSE](https://inwestycje.pse.pl/), sekcja Radkowice). Nie utożsamiamy go automatycznie z transformatorem 110/SN. Nazwy „GPZ Radkowice”, „SE Radkowice” i „Grupa Radkowice” należy rozróżniać według źródła i typu obiektu.

Informację użytkownika o współdzieleniu stacji przez PSE/PGE zapisujemy jako wskazówkę do dalszej weryfikacji. Udział PGE w regionalnej sieci jest udokumentowany, ale **granice własności pól, rozdzielni i transformatorów pozostają UNKNOWN**. Nie przypisujemy całej części 110 kV jednemu operatorowi bez dokumentu. Przegląd nie znalazł dotąd pierwotnego schematu granic eksploatacji.

## Pierwsze znane projekty

Zachowany [wykaz PSE, stan 31.07.2026](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx), pobrany 10.09.2026; arkusz `Wykaz wspólny`. Kierunki mocy sprawdzono w nagłówkach kolumn I/J. Dane REPORTED, bez estymacji.

| Wiersz | Projekt | Podmiot | Punkt | Eksport MW | Import MW | Status |
|---|---|---|---|---:|---:|---|
| 787 | MEE Chałupki | Grand Solar 23 Sp. z o.o. | Radkowice 220 kV | 96,96 | 98,8992 | Obowiązująca umowa przyłączeniowa |
| 843 | MEE Radkowice | RSE 10 Sp. z o.o. | Radkowice 220 kV | 50 | 50 | Obowiązująca umowa przyłączeniowa |
| 847 | MEE Chęciny | Qair Polska S.A. | Radkowice 220 kV | 100 | 102 | Obowiązująca umowa przyłączeniowa |

To trzy pasujące wiersze jednego snapshotu, nie kompletna liczba projektów na stacji. Należą do grupy B według statusu publikacji. Nie są dowodem wykonania przyłączenia. Wskazane w kolumnie Y daty roku 2029 pozostają terminami źródłowymi, nie potwierdzonym uruchomieniem. Nie znamy MWh.

Projektów na 220 kV nie przypisujemy automatycznie do obciążenia transformacji 220/110 kV. Nie odejmujemy ich mocy od znamionowej mocy transformatorów. Grupy A i C oraz projekty PGE wymagają osobnego przeglądu; brak w tym wycinku nie oznacza zera. Starsze publikacje PSE o oczekiwaniu nie dowodzą oczekiwania w 2026 r.

## Infrastruktura i inwestycje

[BIP Chęcin — założenia energetyczne](https://checiny.biuletyn.net/fls/bip_pliki/2026_03/BIPF64CD10561EC15Z/PZCEEPG_2025-2027.pdf), PDF s.21–25, opisuje SE i relacje 220 kV do Kielc, Połańca i Kielc Piaski, powołując się na PSE. Dokument wskazuje także GPZ Wolica 110/15 kV i regionalne dane PGE. To podstawa do grafu referencyjnego, nie aktualny schemat ruchowy.

Ten sam dokument wymienia plan montażu autotransformatora 160 MVA oraz rozbudowy pod magazyn Chałupki. Sam plan nie potwierdza aktualnej obsady i mocy wszystkich transformatorów. Zawiera również starsze opisy planistyczne, dlatego daty poszczególnych ustaleń trzeba zachować oddzielnie; katalog w URL z 2026 r. nie odmładza wszystkich treści.

[Portal inwestycji PSE](https://inwestycje.pse.pl/), odczyt 11.09.2026: rozbudowa/modernizacja etap I jest opisana jako w budowie, etap II w przygotowaniu; wymiana transformatora jako zakończona w 2025 r., wcześniejsza rozbudowa w 2020 r. Nie scalono tych zadań z opisem planowanego 160 MVA bez potwierdzenia tożsamości inwestycji.

## Porównanie z alternatywą

| Kryterium | Radkowice — wybór główny | Kościerzyna — kandydat rezerwowy |
|---|---|---|
| Preferencja użytkownika | Wskazane wprost | Nie wskazana |
| Konkretne projekty | Trzy wskazane BESS w XLSX PSE | W dokumencie Energi jest m.in. wpis GPZ Kościerzyna i status obiektu przyłączonego |
| Jakość czasu publikacji | Jawny stan XLSX 31.07.2026 | Konflikt dat sierpień/czerwiec; kwarantanna |
| Inwestycje i topologia | Portal PSE i lokalny BIP | W tym porównaniu nie zweryfikowano kompletu dowodów |
| Przewaga | Bezpośredni test BESS i styku 220/110 kV | Możliwy późniejszy test innych statusów i OSD |

Źródło alternatywy: [Energa PDF](https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf), strona 1, pozycja 3; konflikt opisany w kontroli z 11.09.2026. Nie jest to pełny ranking stacji Polski.

## Odtwarzanie i dalsze prace

`scripts/research_radkowice.py` odczytuje wyłącznie zachowany XLSX, sprawdza hash, datę, kluczowe nagłówki i dokładną nazwę stacji. Wynik: `data/reference/radkowice_pse_projects_2026-07-31.json`, z komórkami źródłowymi. To skrypt badawczy, nie kompletny connector. Oryginalny XLSX nie jest zapisywany przez openpyxl; ostrzeżenie o rozszerzeniu walidacji nie oznacza zmiany oryginału.

Nowe kopie HTML/PDF mają manifest `data/catalog/radkowice_snapshot_manifest.json`. Zapisano je osobno w lokalnym `data/archives/radkowice_sources_2026-09-11.zip`; hash archiwum i jego dwóch sprawdzonych elementów zawiera `data/catalog/radkowice_archive_manifest.json`. Nie należą do wcześniejszego archiwum z 10.09 i wymagają osobnej zewnętrznej kopii. Przy odtwarzaniu rozpakować do pustego folderu i sprawdzić hashe przed przeniesieniem plików. Licencje komercyjnego użycia i redystrybucji tych konkretnych źródeł pozostają niewyjaśnione.

Najbliższe prace: granice PSE/PGE, źródła projektów po stronie 110 kV, dowody istniejących przyłączeń i aktualnych wniosków, źródła o parametrach transformacji oraz uprawnienia do wykorzystania. Wybór stacji nie oznacza obietnicy pełnego pipeline, telemetrii ani policzalnej wolnej mocy.

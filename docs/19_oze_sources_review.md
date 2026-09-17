# Trzy źródła wskazane przez użytkownika — 17.09.2026

## Wniosek

Źródła są przydatne w dwóch osobnych modułach: ocena przestrzenna lokalizacji oraz rozpoznawanie istniejących źródeł wytwórczych. Nie dostarczają potwierdzonej rezerwy GPZ, aktualnego obciążenia ani pełnego pipeline przyłączeniowego. Nie zmieniono scoringu i nie dodano ich rekordów do grafu elektrycznego.

## Raport GRID — GRID_OZE_REPORT

[Raport potencjału OZE](https://gridw.home.pl/pub/Raport_potencjal_OZE.pdf): 15 stron; metadane pliku wskazują utworzenie 26.06.2025, co nie jest datą wszystkich danych. Projekt trwał od października 2024 do czerwca 2025. [Komunikat autora z 20.08.2025](https://www.gridw.pl/pl/aktualnosci/mamy-przestrzen-dla-oze-wyniki-analiz-potencjalu-energetyki-odnawialnej-w-gminach) potwierdza publikację.

Strony 4–10 opisują kryteria terenowe dla PV i wiatru; strona 11 zawiera wyniki dla 18 gmin. Potencjał w ha i procentach powierzchni nie jest mocą przyłączeniową. Opracowanie usuwa obszary poniżej 1 ha; tego założenia nie przenosimy do BESS. Parametry obejmują m.in. bufor 500 m od zabudowy dla wiatru (strona 9), który traktujemy jako historyczne założenie autorów wymagające niezależnej weryfikacji prawnej, nie obowiązującą regułę aplikacji.

Raport wskazuje przekazanie wektorów GPKG/SHP; nie potwierdzono publicznej paczki do pobrania. Przydatność: metodyka i lista źródeł dla odrębnego modułu przestrzennego. Nie jest studium sieciowym ani potwierdzeniem przeznaczenia działki. Sprawdzono wizualnie tabele stron 9 i 11 oraz tekst dokumentu.

## Geoportal GRID — GRID_OZE_PORTAL

[Adres użytkownika](https://geoportal-oze.gridw.pl/) prowadzi do ArcGIS Instant Apps, appid `f6e44953d693416e83473bcbb59aae2d`, webmap `c3be596d51d846d2a7b90ca007a4879c`. Zachowano konfigurację, metadane i próbki.

Konfiguracja wskazuje warstwy gmin, obszarów preferencyjnych, wykluczeń i buforów GPZ 30/40 km. Bufor odległości nie potwierdza topologii, zdolności przesyłowej, wykonalności trasy ani przypisania projektu. Geometria GPZ wywodząca się z OSM nie jest niezależnym potwierdzeniem OSM.

[Metadane warstwy PV](https://services8.arcgis.com/TG6EwIH3KnV3ncxM/arcgis/rest/services/analiza_pv_1ha/FeatureServer/0?f=pjson) potwierdzają `Query`, CRS EPSG:3857 (wkid 102100), pola powierzchni i limit 2000 rekordów odpowiedzi. Serwis deklaruje JSON, GeoJSON i PBF; sprawdzono JSON, bez pobierania pełnej geometrii. Limit rekordów nie oznacza dozwolonej częstotliwości zapytań. Próbka jednego rekordu PV ma `exceededTransferLimit`, więc nie jest całym zbiorem.

Zapytanie do warstwy gmin pilotażowych zwróciło 18 gmin, bez Chęcin. Nie należy rozszerzać tego stwierdzenia na wszystkie warstwy geoportalu: ich zasięgi są różne. Metadane warstwy PV wskazują edycję w czerwcu 2025; edycja nie ustala aktualności poszczególnych danych wejściowych.

`licenseInfo` webmapy jest puste, a warstwy PV nie podają warunków ponownego wykorzystania. Dostęp bez konta nie dowodzi zgody na komercyjną redystrybucję. Potrzeba NEED-015 obejmuje licencję, aktualność, dane źródłowe i zasady dostępu. Nie stwierdzono gwarantowanego cyklu aktualizacji ani SLA. Nie testowano WMS/WFS; znaleziono działający ArcGIS REST.

## Energetyczna Mapa Polski — EMP_PW

[EMP](https://emp.pw.edu.pl/mapa) jest projektem KNE Politechniki Warszawskiej; [PW opisuje autorstwo i cel](https://www.pw.edu.pl/aktualnosci/nasi-studenci-stworzyli-energetyczna-mape-polski). To katalog źródeł wytwórczych, a nie oficjalna ewidencja całej topologii KSE.

Kod klienta ujawnia używany odczyt [GET /api/v1/units](https://emp.pw.edu.pl/api/v1/units). Jedno zapytanie bez konta zwróciło 173 rekordy: 81 coal, 28 on_shore_wind, 17 photovoltaics, 16 biogas, 9 hydro, 7 lignite, 6 pumped_storage, 5 ccgt, 4 off_shore_wind. Są to liczby rekordów odpowiedzi, nie statystyka wszystkich polskich instalacji. Nie znaleziono wzmianki o Radkowicach w tej odpowiedzi.

Pola obejmują ID, slug, nazwę, typ, współrzędne, `power_installed`, właściciela, lata, opis, bibliografię i relację do nadrzędnego obiektu. Brak pola GPZ/PCC oraz jawnej daty aktualizacji rekordu. W odpowiedzi jest 165 kodów statusu 1 i 8 kodów 0; nie mapujemy ich automatycznie na operational/planned. Wymagają potwierdzenia semantyki. Relacje rodzic–dziecko wymagają kontroli przed agregacją mocy. Jednostki liczb trzeba potwierdzić przed normalizacją; sama nazwa pola nie wystarcza.

Kod klienta zawiera eksport CSV szczegółów obiektu, lecz nie sprawdzano pobrania CSV w przeglądarce. WMS/WFS ani stabilnego kontraktu publicznego API nie potwierdzono. Nie ustalono otwartej licencji, limitów i cyklu aktualizacji. NEED-016 zapisuje te braki. Źródło klasy G służy odkrywaniu obiektów i odnośników do publikacji pierwotnych. Nie przypisujemy instalacji do najbliższego GPZ ani nie kopiujemy całej bazy do aplikacji.

## Dodatkowy trop krajowy

Podczas badania znaleziono [komunikat GUGiK z 15.06.2026](https://www.geoportal.gov.pl/aktualnosci/nowe-uslugi-potencjalu-oze-dane-szczegolowe/) o szczegółowych usługach WMS potencjału OZE, także magazynowania energii elektrycznej. Wpis GUGIK_OZE_DETAIL_2026 jest przeglądem komunikatu; endpointy, licencje i zawartość warstw wymagają osobnego testu. To nie dowód dostępnej mocy dla BESS.

## Dalsze działania i odtwarzalność

Pierwszeństwo ma próbka danych przestrzennych obejmująca pilot z potwierdzonymi zasadami użycia. EMP może uzupełniać kolejkę weryfikacji projektów po ustaleniu praw i semantyki. Kontakty z właścicielami nie zostały wysłane; użytkownik może pomóc w NEED-015 i NEED-016.

Zachowano 12 plików w dziesiątym archiwum `data/archives/oze_discovery_2026-09-17.zip`, z SHA-256 i URL w `data/catalog/probe_results_oze_2026-09-17.json` oraz `data/catalog/oze_archive_2026-09-17.json`. Surowe pliki pozostają poza Git; osobna kopia zapasowa jest wymagana. Nagłówki HTTP nie zostały zachowane, etykiety formatu wynikają ze sprawdzonej treści. Nie implementowano connectora produkcyjnego ani nowych modeli oceny.

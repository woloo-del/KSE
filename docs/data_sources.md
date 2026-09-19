# Rejestr źródeł danych

Stan badania: **2026-09-19**. Źródła: **83**.

Widok generowany z `data/catalog/source_notes.json`. Pełne pola i manifesty: `data/catalog/data_sources.json`. Raport: [01_data_research.md](01_data_research.md).

`SAMPLE_VERIFIED` oznacza odczytaną próbkę, nie walidację całego zbioru; `CONTENT_REVIEWED` — treść strony/dokumentu; `DOCUMENTATION_REVIEWED` — opis interfejsu; `DISCOVERED` — tylko wskazanie; `BLOCKED` — nieudany odczyt. GetCapabilities nie jest testem GetFeature. `UNKNOWN` oznacza brak rozstrzygnięcia, nie brak interfejsu.

A–H opisuje autorytet/proweniencję według AGENTS.md; dla bibliotek i modeli H nie jest oceną jakości oprogramowania. `data_quality_score=null` dla wszystkich źródeł: nie skalibrowano liczbowej miary jakości. Daty źródłowe pozostają puste, jeśli nie zostały rozstrzygnięte.

| ID | Źródło | Weryfikacja | Priorytet | Użycie komercyjne |
|---|---|---|---|---|
| PSE_API | [API raportów PSE — OpenAPI](https://api.raporty.pse.pl/api/openapi) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| PSE_PIPELINE | [Podmioty ubiegające się o przyłączenie — XLSX](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| PSE_CAPACITY | [Dostępność mocy przyłączeniowej do sieci przesyłowej](https://www.pse.pl/documents/20182/51490/informacja_o_dostepnosci_mocy_przylaczeniowej_do_sieci_przesylowej.pdf/81835e70-c6bb-4ed1-8154-1959a45b44f1) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| PSE_PLAN | [PRSP 2027–2036 — projekt po konsultacjach](https://www.pse.pl/documents/20182/7102190804/PRSP_2027-2036-dokument_glowny_projekt_po_konsultacji.pdf/de2f004f-8a80-4264-907a-a38d52c5d50f) | CONTENT_REVIEWED | P1 | UNKNOWN |
| PSE_STRUCT_B2B | [Dokumentacja grid-struct-api](https://polskie-sieci-elektroenergetyczne.github.io/grid-struct-api/) | DISCOVERED | P3 | UNKNOWN |
| ENERGA_LANDING | [Informacje o stanie przyłączeń](https://energa-operator.pl/przylaczenie-do-sieci/informacje-o-stanie-przylaczen) | CONTENT_REVIEWED | P1 | UNKNOWN |
| ENERGA_EXPORT | [Dostępna moc wytwórcza — 31.08.2026](https://cdn-netpr.pl/file/mediakit/3063621/4a/informacja_o_wartosci_lacznej_dostepnej_wytworczej_mocy_przylaczeniowej_31_08_2026.pdf) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| ENERGA_IMPORT | [Dostępna moc odbiorcza — 31.08.2026](https://cdn-netpr.pl/file/mediakit/3063619/5c/informacja_o_wartosci_lacznej_dostepnej_odbiorczej_mocy_przylaczeniowej_31_08_2026.pdf) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| ENERGA_PIPELINE | [Wnioski i odmowy — konflikt dat dokumentu](https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| ENERGA_PLAN | [Uzgodniony plan rozwoju 2026–2031](https://energa-operator.pl/raporty-i-liczby/plan-rozwoju) | CONTENT_REVIEWED | P1 | UNKNOWN |
| ENEA_PIPELINE | [Informacje o przyłączeniach i kryteria SN](https://www.operator.enea.pl/przylaczenie-do-sieci/informacje-o-przylaczeniach) | CONTENT_REVIEWED | P1 | UNKNOWN |
| ENEA_MAP | [Mapy przyłączonych i dostępnych mocy OZE](https://www.operator.enea.pl/przylaczone-i-dostepne-moce-oze) | CONTENT_REVIEWED | P1 | UNKNOWN |
| ENEA_PLAN | [Plan rozwoju 2026–2031](https://www.operator.enea.pl/plan-rozwoju-enea-operator-na-lata-2026-2031) | CONTENT_REVIEWED | P1 | UNKNOWN |
| TAURON_PIPELINE | [Przyłączane obiekty i wydane odmowy](https://www.tauron-dystrybucja.pl/-/media/offer-documents/dystrybucja/przylaczenie/dostepne-moce/informacja-o-przylaczanych-obiektach-i-wydanych-odmowach.ashx) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| TAURON_MAP | [Portal dostępnych mocy](https://dostepnemoce.tauron-dystrybucja.pl/) | CONTENT_REVIEWED | P2 | UNKNOWN |
| TAURON_PLAN | [Plan rozwoju — indeks operatora](https://www.tauron-dystrybucja.pl/plan-rozwoju) | CONTENT_REVIEWED | P2 | UNKNOWN |
| STOEN_LANDING | [Sieć — indeks dokumentów](https://www.stoen.pl/pl/strona/siec) | CONTENT_REVIEWED | P2 | REQUIRES_PERMISSION_REVIEW |
| STOEN_EXPORT | [Dostępna moc źródeł — III kwartał 2026](https://www.stoen.pl/files/2026-07/wielkosc-dostepnej-mocy-przylaczeniowej-zrodel-w-sieci-stoen-operator-iii-kw-2026.pdf) | SAMPLE_VERIFIED | P2 | REQUIRES_PERMISSION_REVIEW |
| STOEN_IMPORT | [Dostępna moc odbiorców — 31.08.2026](https://www.stoen.pl/files/2026-09/wielkosc-dostepnej-mocy-przylaczeniowej-dla-odbiorcow-w-sieci-stoen-operator-31.08.2026r.pdf) | SAMPLE_VERIFIED | P2 | REQUIRES_PERMISSION_REVIEW |
| STOEN_PIPELINE | [Wykaz podmiotów powyżej 1 kV — link do PDF](https://www.stoen.pl/files/2026-08/1788176873_zestawienie-informacji-dot.-podmiotow-ubiegajacych-sie-o-przylaczenie-pow.-1kv-stan-na-30.06.2026-r.pdf) | DISCOVERED | P2 | REQUIRES_PERMISSION_REVIEW |
| STOEN_STORAGE | [Rejestr magazynów — link do PDF](https://www.stoen.pl/files/2026-01/rejestr-magazynow-energii-stoen-operator-sp.-z-o.o.pdf) | DISCOVERED | P2 | REQUIRES_PERMISSION_REVIEW |
| STOEN_PLAN | [Plan rozwoju 2026–2031](https://stoen.pl/strona/plan-rozwoju-w-zakresie-zaspokojenia-obecnego-i-przyszlego-zapotrzebowania-na-energie-elektryczna-na-lata-2026-2031) | DISCOVERED | P2 | REQUIRES_PERMISSION_REVIEW |
| PGE_LANDING | [Dostępne moce dla źródeł wytwórczych](https://pgedystrybucja.pl/przylaczenia/procedury-przylaczeniowe/dostepne-moce-dla-zrodel-wytworczych) | BLOCKED | P1 | UNKNOWN |
| PGE_EXPORT_DISCOVERY | [Dostępne moce I kwartał 2026 — wskazanie wyszukiwarki](https://pgedystrybucja.pl/content/download/71691b9fb622cdf89306ec0dc0c1ac3d/file/dostepne-moce-pge-i-kw-2026.pdf?contentId=2208&inLanguage=pol-PL&version=6) | BLOCKED | P2 | UNKNOWN |
| PGE_PLAN_DISCOVERY | [Konsultacje planu rozwoju — wskazanie strony](https://pgedystrybucja.pl/o-spolce/dzialalnosc/konsultacje-spoleczne-projektu-planu-rozwoju) | BLOCKED | P2 | UNKNOWN |
| KGHM_OSD | [OSD dla systemu elektroenergetycznego](https://kghm.com/pl/biznes/strefa-energetyczna/osd-dla-systemu-elektroenergetycznego) | CONTENT_REVIEWED | P2 | UNKNOWN |
| URE_REGISTERS | [BIP URE — rejestry i bazy](https://bip.ure.gov.pl/bip/rejestry-i-bazy) | CONTENT_REVIEWED | P1 | UNKNOWN |
| ENERGY_LAW_516 | [Dz.U. 2026 poz. 516 — zmiana Prawa energetycznego](https://dziennikustaw.gov.pl/D2026000051601.pdf) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| BIP_ENV_DISCOVERY | [Ekoportal — punkt wejścia do informacji środowiskowej](https://ekoportal.gov.pl/) | BLOCKED | P2 | UNKNOWN |
| KRS_API_DOCS | [Portal Rejestrów Sądowych — OpenAPI](https://prs.ms.gov.pl/krs/openApi) | DOCUMENTATION_REVIEWED | P2 | UNKNOWN |
| GUGIK_EGIB | [GUGiK — zbiorcza usługa WFS EGiB](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza?SERVICE=WFS&REQUEST=GetCapabilities) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| GUGIK_BDOT | [BDOT10k — dane topograficzne](https://www.geoportal.gov.pl/pl/dane/baza-danych-obiektow-topograficznych-bdot10k/) | DOCUMENTATION_REVIEWED | P1 | UNKNOWN |
| GUGIK_BDOT_PARQUET | [Nowe udostępnianie BDOT10k jako GeoParquet](https://www.geoportal.gov.pl/aktualnosci/nowy-sposob-udostepniania-danych-bdot10k-w-geoportalu/) | DOCUMENTATION_REVIEWED | P1 | UNKNOWN |
| GUGIK_ORTHO | [Ortofotomapa GUGiK](https://www.geoportal.gov.pl/pl/dane/ortofotomapa-orto/) | DOCUMENTATION_REVIEWED | P2 | PERMITTED_AS_DESCRIBED |
| GUGIK_NMT | [Numeryczny model terenu](https://www.geoportal.gov.pl/pl/dane/numeryczny-model-terenu-nmt/) | DOCUMENTATION_REVIEWED | P2 | UNKNOWN |
| GUGIK_MPZP | [Krajowa Integracja MPZP](https://mapy.geoportal.gov.pl/wss/ext/KrajowaIntegracjaMiejscowychPlanowZagospodarowaniaPrzestrzennego?lang=pol) | CONTENT_REVIEWED | P2 | UNKNOWN |
| URBAN_REGISTER | [Rejestr Urbanistyczny — publikacje](https://rejestr-urbanistyczny.gov.pl/published) | CONTENT_REVIEWED | P2 | UNKNOWN |
| GDOS_GIS | [GDOŚ — WFS form ochrony przyrody](https://sdi.gdos.gov.pl/wfs?SERVICE=WFS&REQUEST=GetCapabilities) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| WODY_SIGW | [SIGW — udostępnianie danych Wód Polskich](https://www.gov.pl/web/wody-polskie/udostepnianie-danych-z-systemu-informacyjnego-gospodarowania-wodami) | DOCUMENTATION_REVIEWED | P2 | PRODUCT_SPECIFIC |
| BDL_GIS | [Bank Danych o Lasach — usługi OGC](https://www9.bdl.lasy.gov.pl/portal/uslugi-ogc?v=1) | DOCUMENTATION_REVIEWED | P2 | UNKNOWN |
| ENTSOE_TP | [Transparency Platform](https://www.entsoe.eu/data/transparency-platform/) | DOCUMENTATION_REVIEWED | P2 | DATASET_SPECIFIC |
| ENTSOE_MAP | [Grid Map — downloads](https://www.entsoe.eu/data/map/downloads/) | CONTENT_REVIEWED | P2 | UNKNOWN |
| OSM_LICENSE | [OpenStreetMap — dane i warunki ODbL](https://www.openstreetmap.org/copyright) | DOCUMENTATION_REVIEWED | P2 | CONDITIONAL |
| GEOFABRIK_PL | [Geofabrik — Poland OSM extract](https://download.geofabrik.de/europe/poland.html) | CONTENT_REVIEWED | P2 | CONDITIONAL |
| OPENINFRAMAP | [OpenInfraMap — opis źródła](https://openinframap.org/about) | CONTENT_REVIEWED | P2 | CONDITIONAL |
| PYPSA_EUR | [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) | CONTENT_REVIEWED | P2 | CONDITIONAL |
| MATPOWER_POLAND | [MATPOWER case2383wp — historyczny przypadek Polski](https://github.com/MATPOWER/matpower/blob/master/data/case2383wp.m) | CONTENT_REVIEWED | P3 | UNKNOWN |
| PANDAPOWER | [pandapower](https://github.com/e2nIEE/pandapower) | CONTENT_REVIEWED | P3 | UNKNOWN |
| VERAGRID | [GridCal / VeraGrid](https://github.com/SanPen/VeraGrid) | CONTENT_REVIEWED | P3 | CONDITIONAL |
| MATPOWER_LIBRARY | [MATPOWER](https://github.com/MATPOWER/matpower) | CONTENT_REVIEWED | P3 | UNKNOWN |
| POWERMODELS | [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) | CONTENT_REVIEWED | P3 | UNKNOWN |
| OPSD_TIMESERIES | [Open Power System Data — time series](https://data.open-power-system-data.org/time_series/) | CONTENT_REVIEWED | P3 | DATASET_SPECIFIC |
| ENERGY_CHARTS | [Energy-Charts API](https://api.energy-charts.info/openapi.json) | SAMPLE_VERIFIED | P2 | CONDITIONAL_FOR_VERIFIED_SAMPLE |
| EMBER_API | [Ember Energy API — dokumentacja](https://api.ember-energy.org/v1/docs) | DOCUMENTATION_REVIEWED | P3 | UNKNOWN |
| JRC_IDEES | [JRC IDEES-2023](https://data.jrc.ec.europa.eu/dataset/1f0b480c-6d21-4d95-897d-20c7ca33df6f) | CONTENT_REVIEWED | P3 | UNKNOWN |
| COPERNICUS | [Copernicus Data Space — OData i produkty](https://documentation.dataspace.copernicus.eu/APIs/OData.html) | DOCUMENTATION_REVIEWED | P3 | PRODUCT_SPECIFIC |
| GRID_OZE_REPORT | [Mamy przestrzeń dla OZE — raport metodyczny](https://gridw.home.pl/pub/Raport_potencjal_OZE.pdf) | CONTENT_REVIEWED | P1 | UNKNOWN |
| GRID_OZE_PORTAL | [Geoportal OZE GRID — ArcGIS WebMap i FeatureServer](https://geoportal-oze.gridw.pl/) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| EMP_PW | [Energetyczna Mapa Polski — katalog źródeł wytwórczych](https://emp.pw.edu.pl/mapa) | SAMPLE_VERIFIED | P1 | UNKNOWN |
| GUGIK_OZE_DETAIL_2026 | [Geoportal krajowy — szczegółowe usługi potencjału OZE](https://www.geoportal.gov.pl/aktualnosci/nowe-uslugi-potencjalu-oze-dane-szczegolowe/) | CONTENT_REVIEWED | P1 | UNKNOWN |
| PSE_INVESTMENTS_RADK | [Portal inwestycji PSE — sekcja Radkowice](https://inwestycje.pse.pl/mapa_inwestycji_pse/) | CONTENT_REVIEWED | P0 | UNKNOWN |
| CHECINY_ENERGY_PLAN | [BIP Chęcin — założenia energetyczne 2025–2027 z perspektywą 2040](https://checiny.biuletyn.net/fls/bip_pliki/2026_03/BIPF64CD10561EC15Z/PZCEEPG_2025-2027.pdf) | CONTENT_REVIEWED | P0 | UNKNOWN |
| PSE_TARIFF_2026 | [Taryfa PSE 2026 — odbiorcy i miejsca dostarczania](https://www.pse.pl/documents/20182/7005343691/20260116_Tekst_Taryfy_na_2026_tekst_jednolity.pdf) | CONTENT_REVIEWED | P0 | UNKNOWN |
| PGE_RADK_CAPACITY_ATTEMPT | [Próba dostępu do pliku mocy PGE I kw.2026](https://pgedystrybucja.pl/content/download/71691b9fb622cdf89306ec0dc0c1ac3d/file/dostepne-moce-pge-i-kw-2026.pdf?contentId=2208&inLanguage=pol-PL&version=6) | BLOCKED | P0 | UNKNOWN |
| SUW_RADK_WOLICA_3_2024 | [Decyzja 3/2024 — przebudowa odcinka Radkowice–Wolica](https://bip.kielce.uw.gov.pl/download/2/33548/decprzesylnr324.pdf) | CONTENT_REVIEWED | P0 | UNKNOWN |
| PSE_RADK_BRIDGE_NOTICE_2025 | [PSE — ogłoszenie 205815-2025, pole 220 kV i most Radkowice](https://www.pse.pl/documents/20182/5928746423/OKRESOWE_OGLOSZENIE_ROBOTY_BUDOWLANE.pdf/883a7669-eb9a-4650-84f4-cd67502fd545?safeargs=76657273696f6e3d312e31) | CONTENT_REVIEWED | P0 | UNKNOWN |
| RDOS_RADK_PIASKI_NOTICE_2025 | [RDOŚ Kielce — obwieszczenie dotyczące Radkowice–Kielce Piaski](https://www.gov.pl/web/rdos-kielce/obwieszczenie-regionalnego-dyrektora-ochrony-srodowiska-w-kielcach-z-dnia-04122025-r-znak-woo-i42072025pjpp16) | CONTENT_REVIEWED | P0 | REQUIRES_PERMISSION_REVIEW |
| RDOS_RADK_PIASKI_DECISION_2025 | [RDOŚ Kielce — pełna decyzja dla przebudowy linii Radkowice–Kielce Piaski](https://www.gov.pl/attachment/27ef7a8e-5094-4391-be1c-7e23cb1038b2) | CONTENT_REVIEWED | P0 | REQUIRES_PERMISSION_REVIEW |
| PSE_IMPACT_REPORT_2023 | [PSE — raport wpływu za 2023 rok, edycja 2024](https://api-raport.pse.pl/uploads/PSE-Zintegrowany_Raport_Wplywu_2023.pdf) | CONTENT_REVIEWED | P0 | UNKNOWN |
| PSE_PRSP_2027_2036_POST_CONSULTATION | [Projekt PRSP 2027–2036 po konsultacjach — kwiecień 2026](https://www.pse.pl/documents/20182/7102190804/PRSP_2027-2036-dokument_glowny_projekt_po_konsultacji.pdf/de2f004f-8a80-4264-907a-a38d52c5d50f?safeargs=76657273696f6e3d312e30) | CONTENT_REVIEWED | P0 | UNKNOWN |
| EBIN_ELECTRICITY | [ebin.josm.pl — mapa sieci i konfiguracja warstw](https://ebin.josm.pl/electricity/) | CONTENT_REVIEWED | P0 | CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate |
| OSM_RADK_STATION_OBJECT | [OSM — obiekt stacji Radkowice, way 199098055](https://www.openstreetmap.org/api/0.6/way/199098055/full) | SAMPLE_VERIFIED | P0 | CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate |
| OSM_RADK_STATION_AREA | [OSM — próbka obszaru stacji Radkowice](https://www.openstreetmap.org/api/0.6/map?bbox=20.516927,50.783155,20.527321,50.792370) | SAMPLE_VERIFIED | P0 | CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate |
| PSE_RADK_STAGES | [Portal inwestycji PSE — etapy modernizacji Radkowic](https://inwestycje.pse.pl/) | SAMPLE_VERIFIED | P0 | UNKNOWN |
| TAURON_MAP_HOME | [TAURON — portal biznesowy z mapą](https://dostepnemoce.tauron-dystrybucja.pl/) | CONTENT_REVIEWED | P0 | NOT_CLEARED |
| TAURON_MAP_SCRIPT | [TAURON — interfejs i zastrzeżenia mapy](https://dostepnemoce.tauron-dystrybucja.pl/wp-content/plugins/tauron-maps/mapy.js?ver=1788435768) | CONTENT_REVIEWED | P0 | NOT_CLEARED |
| TAURON_PENDING_MAP | [TAURON — regionalny wykaz obiektów planowanych](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace) | CONTENT_REVIEWED | P0 | NOT_CLEARED |
| TAURON_GPZ_LODZKIE | [TAURON — publikacja GPZ województwa łódzkiego](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace/gpz-lodzkie) | CONTENT_REVIEWED | P0 | NOT_CLEARED |
| GUGIK_OWNERSHIP_GROUPS | [Mapa własności — grupy rejestrowe](https://www.gov.pl/web/gugik/nowa-usluga-mapa-wlasnosci---grupy-rejestrowe-dostepna-w-modulach-geoportal-krajowy-i-geodezja-i-kartografia-w-serwisie-wwwgeoportalgovpl) | CONTENT_REVIEWED | P1 | NOT_CLEARED |
| KIELCE_EGIB_OWNERSHIP_DISCOVERY | [Powiat kielecki — schematy publicznych usług WFS](https://geoportal.powiat.kielce.pl/map/geoportal/wfse.php) | CONTENT_REVIEWED | P1 | NOT_CLEARED |
| GUGIK_EGIB_OWNERSHIP_PROBE | [GUGiK — próba grupy rejestrowej w zbiorczym WFS](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza) | SAMPLE_VERIFIED | P1 | NOT_CLEARED |
| GUGIK_OWNERSHIP_MAP | [GUGiK — WMS Mapa własności i kompletność powiatowa](https://mapy.geoportal.gov.pl/wss/ext/MapaWlasnosci) | SAMPLE_VERIFIED | P1 | NOT_CLEARED |
| PYPROJ_TRANSFORMER | [pyproj 3.7.2 — Transformer i licencja](https://pyproj4.github.io/pyproj/stable/api/transformer.html) | DOCUMENTATION_REVIEWED | P1 | YES_UNDER_LICENSE |

## Karty źródeł

### PSE_API — API raportów PSE — OpenAPI

[Źródło](https://api.raporty.pse.pl/api/openapi)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** system_data_and_node_dictionary
- **Napięcie:** SN; 110 kV; 220 kV; 400 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** REST; JSON; OpenAPI
- **API:** YES
- **GIS:** UNKNOWN
- **Aktualizacja:** Zależna od raportu i pola czasu; niejednolita.
- **Historia:** YES; próbki obejmują wcześniejsze obserwacje.
- **Uwierzytelnienie:** Anonimowe próby działały; brak gwarancji dla każdego endpointu.
- **Licencja:** UNKNOWN — nie potwierdzono ogólnej licencji ponownego wykorzystania wszystkich serii.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** A
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** business_date; publication_ts; station_name; switching_station_voltage; busbar_code; pv_red_balance; pv_red_network
- **Zastosowanie:** Słownik węzłów i kontekst systemowy; rozdzielenie przyczyn redysponowania.
- **Ograniczenia:** Nie jest pełnym grafem operacyjnym.; Próba przepływów dotyczy przekrojów transgranicznych.; Pierwsze rekordy bez filtra czasu nie są najnowszym stanem; null nie oznacza zera.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** OpenAPI info.version 2.0.9
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Filtrować czas, stronicować po nextLink; $first, $after, $filter, $select, $orderby. Nie ustalono gwarantowanego limitu żądań.
- **Próba PSE_API_DOCS:** HTTP 200; 2026-09-10T11:18:09.4508686Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/pse_api_index.html`.
- **Próba PSE_API_JS:** HTTP 200; 2026-09-10T11:19:33.2503384Z; `data/catalog/probe_results_20260910T111959000Z.json`; próbka `data/raw/research/2026-09-10/pse_api_frontend.js`.
- **Próba PSE_OPENAPI:** HTTP 200; 2026-09-10T11:21:02.8835007Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/pse_openapi.json`.
- **Próba PSE_NODES_SAMPLE:** HTTP 200; 2026-09-10T11:22:46.5004479Z; `data/catalog/probe_results_20260910T112248796Z.json`; próbka `data/raw/research/2026-09-10/pse_nodes_sample.json`.
- **Próba PSE_REDISPATCH_SAMPLE:** HTTP 200; 2026-09-10T11:22:47.0745732Z; `data/catalog/probe_results_20260910T112248796Z.json`; próbka `data/raw/research/2026-09-10/pse_redispatch_sample.json`.
- **Próba PSE_FLOWS_SAMPLE:** HTTP 200; 2026-09-10T11:22:47.3529270Z; `data/catalog/probe_results_20260910T112248796Z.json`; próbka `data/raw/research/2026-09-10/pse_flows_sample.json`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_PIPELINE — Podmioty ubiegające się o przyłączenie — XLSX

[Źródło](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** connection_pipeline
- **Napięcie:** 110 kV; 220 kV; 400 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** XLSX
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** Wykaz aktualizowany okresowo; częstotliwość minimalna OSP miesięczna według badanej nowelizacji.
- **Historia:** PARTIAL — wymagane własne snapshoty.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** YES
- **Scraping:** HTML_LINK_DISCOVERY_ONLY
- **Pola:** ID Obiektu; wnioskodawca; miejsce przyłączenia; napięcie; export_MW; import_MW; technologia; etap; daty procedury
- **Zastosowanie:** Pierwszy kandydat do parsera pipeline i relacji projekt–punkt przyłączenia.
- **Ograniczenia:** Braki identyfikatorów i wartości; wielopoziomowy nagłówek.; Nie potwierdzono pola MWh.; Rozmiar arkusza nie jest liczbą unikalnych projektów.
- **Data stanu źródła:** 2026-07-31
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Daty — uwagi:** Strona wskazywała aktualizację 01.09.2026; nagłówek arkusza 31.07.2026. Zachować osobno.
- **Powiązane źródło/interfejs:** [link](https://www.pse.pl/obszary-dzialalnosci/wymiana-miedzysystemowa/informacje-ogolne/-/asset_publisher/L3RZBt9EkXoj/content/wykaz-podmiotow-ubiegajacych-sie-o-przylaczenie-do-krajowej-sieci-przesylowej/pop_up)
- **Próba PSE_PIPELINE_XLSX:** HTTP 200; 2026-09-10T11:21:03.1201767Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/pse_pipeline_url_2026-07-31.xlsx`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_CAPACITY — Dostępność mocy przyłączeniowej do sieci przesyłowej

[Źródło](https://www.pse.pl/documents/20182/51490/informacja_o_dostepnosci_mocy_przylaczeniowej_do_sieci_przesylowej.pdf/81835e70-c6bb-4ed1-8154-1959a45b44f1)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** reported_connection_capacity
- **Napięcie:** 110 kV; 220 kV; 400 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** stacja lub obszar; horyzont; wariant WP OSD; dostępna moc MW; założenia
- **Zastosowanie:** Odczyt dostępności operatora z warunkami i scenariuszem.
- **Ograniczenia:** Nie sumować współdzielonych grup ani powtórnie odejmować uwzględnionego pipeline.; Tabela importowa s.12 dotyczy nowych planowanych stacji; nie obecnej rezerwy wszystkich stacji.
- **Data stanu źródła:** 2026-08-31
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 3–4, 12–13
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba PSE_CAPACITY:** HTTP 200; 2026-09-10T11:18:09.9988780Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/pse_capacity_retrieved_2026-09-10.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_PLAN — PRSP 2027–2036 — projekt po konsultacjach

[Źródło](https://www.pse.pl/documents/20182/7102190804/PRSP_2027-2036-dokument_glowny_projekt_po_konsultacji.pdf/de2f004f-8a80-4264-907a-a38d52c5d50f)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 110 kV; 220 kV; 400 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** Cykl planowania i rewizje; nie dane bieżące.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** inwestycja; stacja; linia; horyzont; status dokumentu
- **Zastosowanie:** Przyszła sieć i rejestr inwestycji.
- **Ograniczenia:** Projekt po konsultacjach; nie utożsamiać z uzgodnieniem i oddaniem do ruchu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_STRUCT_B2B — Dokumentacja grid-struct-api

[Źródło](https://polskie-sieci-elektroenergetyczne.github.io/grid-struct-api/)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** topology_interface_documentation
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; API documentation
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — kanał B2B wymaga odrębnej weryfikacji uprawnień.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** schemat wymiany strukturalnej
- **Zastosowanie:** Ustalenie przyszłego dostępu partnerskiego do danych strukturalnych.
- **Ograniczenia:** Nie potwierdzono anonimowego dostępu do danych; dokumentacja B2B nie oznacza otwartego API topologii.; Bezpośredni odczyt dokumentacji nie powiódł się.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGA_LANDING — Informacje o stanie przyłączeń

[Źródło](https://energa-operator.pl/przylaczenie-do-sieci/informacje-o-stanie-przylaczen)

- **Operator:** Energa-Operator
- **Właściciel:** Energa-Operator S.A.
- **Kraj:** PL
- **Kategoria:** source_index
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** HTML_LINK_DISCOVERY_ONLY
- **Pola:** link; tytuł; data
- **Zastosowanie:** Odkrywanie nowych wersji publikacji.
- **Ograniczenia:** Nie potwierdzono publicznego API ani operacyjnego GIS.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba ENERGA_LANDING:** HTTP 200; 2026-09-10T11:18:12.9671305Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/energa_landing.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGA_EXPORT — Dostępna moc wytwórcza — 31.08.2026

[Źródło](https://cdn-netpr.pl/file/mediakit/3063621/4a/informacja_o_wartosci_lacznej_dostepnej_wytworczej_mocy_przylaczeniowej_31_08_2026.pdf)

- **Operator:** Energa-Operator
- **Właściciel:** Energa-Operator S.A.
- **Kraj:** PL
- **Kategoria:** reported_export_capacity
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** jednostka raportowania; moc MW; okres; warunki
- **Zastosowanie:** Screening eksportu, z zachowaniem poziomu agregacji.
- **Ograniczenia:** Nie jest telemetrią lokalnych elementów; konieczna interpretacja tabel i założeń.
- **Data stanu źródła:** 2026-08-31
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba ENERGA_EXPORT:** HTTP 200; 2026-09-10T11:18:12.2132448Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/energa_export_2026-08-31.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGA_IMPORT — Dostępna moc odbiorcza — 31.08.2026

[Źródło](https://cdn-netpr.pl/file/mediakit/3063619/5c/informacja_o_wartosci_lacznej_dostepnej_odbiorczej_mocy_przylaczeniowej_31_08_2026.pdf)

- **Operator:** Energa-Operator
- **Właściciel:** Energa-Operator S.A.
- **Kraj:** PL
- **Kategoria:** reported_import_capacity
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** jednostka raportowania; moc odbiorcza MW; okres
- **Zastosowanie:** Osobna analiza ładowania BESS i dużego poboru.
- **Ograniczenia:** Nie przenosić wartości eksportowych na importowe; brak walidacji wszystkich wierszy.
- **Data stanu źródła:** 2026-08-31
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba ENERGA_IMPORT:** HTTP 200; 2026-09-10T11:18:11.9085689Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/energa_import_2026-08-31.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGA_PIPELINE — Wnioski i odmowy — konflikt dat dokumentu

[Źródło](https://cdn-netpr.pl/file/mediakit/3063617/fa/2026_08_31_pusop_wnioski_i_odmowy_eop.pdf)

- **Operator:** Energa-Operator
- **Właściciel:** Energa-Operator S.A.
- **Kraj:** PL
- **Kategoria:** connection_pipeline
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** projekt; miejsce przyłączenia; moc; etap; data
- **Zastosowanie:** Pipeline z ograniczeniem czasowym i ostrzeżeniem o konflikcie.
- **Ograniczenia:** Nazwa pliku 31.08.2026, nagłówek strony 1 i metadane 30.06.2026; nie uznano za pewny stan sierpniowy.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 1
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Konflikt dat:** `{"filename_date": "2026-08-31", "document_header_date": "2026-06-30", "resolution": "UNRESOLVED"}`
- **Próba ENERGA_PIPELINE:** HTTP 200; 2026-09-10T11:18:11.5286327Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/energa_pipeline_2026-08-31.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGA_PLAN — Uzgodniony plan rozwoju 2026–2031

[Źródło](https://energa-operator.pl/raporty-i-liczby/plan-rozwoju)

- **Operator:** Energa-Operator
- **Właściciel:** Energa-Operator S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** inwestycja; horyzont; status planu
- **Zastosowanie:** Rejestr przyszłych wzmocnień.
- **Ograniczenia:** Plan nie potwierdza wykonania inwestycji.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://cdn-netpr.pl/file/mediakit/2972639/30/uzgodniony_plan_rozwoju_2026_2031_energa_operator_sa.pdf)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENEA_PIPELINE — Informacje o przyłączeniach i kryteria SN

[Źródło](https://www.operator.enea.pl/przylaczenie-do-sieci/informacje-o-przylaczeniach)

- **Operator:** ENEA Operator
- **Właściciel:** ENEA Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** connection_pipeline_and_criteria
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** HTML_LINK_DISCOVERY_ONLY
- **Pola:** wykazy podmiotów; kryteria SN; wybrane GPZ; daty publikacji
- **Zastosowanie:** Pipeline i lokalne techniczne ograniczenia SN.
- **Ograniczenia:** Nie przeprowadzono pełnego odczytu wierszy najnowszych załączników.; Kryteria dotyczące wybranych GPZ nie są uniwersalne.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba ENEA_PIPELINE_HTML:** HTTP 200; 2026-09-10T11:19:57.8537807Z; `data/catalog/probe_results_20260910T111959000Z.json`; próbka `data/raw/research/2026-09-10/enea_pipeline_landing.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENEA_MAP — Mapy przyłączonych i dostępnych mocy OZE

[Źródło](https://www.operator.enea.pl/przylaczone-i-dostepne-moce-oze)

- **Operator:** ENEA Operator
- **Właściciel:** ENEA Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** connection_capacity_map
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; Power BI
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** Operator deklaruje codzienną aktualizację w komunikacie z 16.01.2026.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** lokalizacja; obszar; moce OZE
- **Zastosowanie:** Eksploracja i weryfikacja lokalnych kandydatów.
- **Ograniczenia:** Pięć osadzeń Power BI w HTML; nie potwierdzono publicznego API, WFS lub dozwolonego eksportu całej bazy.; Poprzednio sprawdzana ścieżka /oze/ zwróciła 404.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://media.enea.pl/pr/863306/enea-operator-codziennie-publikuje-aktualne-dane-dotyczace-oze-dla-inwestorow)
- **Próba ENEA_MAP:** HTTP 200; 2026-09-10T11:21:03.6443935Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/enea_maps.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENEA_PLAN — Plan rozwoju 2026–2031

[Źródło](https://www.operator.enea.pl/plan-rozwoju-enea-operator-na-lata-2026-2031)

- **Operator:** ENEA Operator
- **Właściciel:** ENEA Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** inwestycja; okres; status uzgodnienia
- **Zastosowanie:** Planowane wzmocnienia.
- **Ograniczenia:** Nie potwierdza oddania do ruchu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://www.operator.enea.pl/media/4501/inwestycje/plan-rozwoju-enea-operator-na-lata-2026-2031pdf.pdf)
- **Próba ENEA_PLAN:** HTTP 200; 2026-09-10T11:21:03.8528543Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/enea_plan_landing.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_PIPELINE — Przyłączane obiekty i wydane odmowy

[Źródło](https://www.tauron-dystrybucja.pl/-/media/offer-documents/dystrybucja/przylaczenie/dostepne-moce/informacja-o-przylaczanych-obiektach-i-wydanych-odmowach.ashx)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** connection_pipeline
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** wnioskodawca; obiekt; miejsce przyłączenia; moc; status; daty
- **Zastosowanie:** Pipeline i odmowy; kontrola zmian.
- **Ograniczenia:** 99 stron; nie zwalidowano wszystkich rekordów.; W próbce anonimizacja podmiotów i nieokreślone miejsca przyłączeń.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** 2026-08-31
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Daty — uwagi:** Data opisu publikacji na stronie; nie przypisywać automatycznie wszystkim rekordom.
- **Powiązane źródło/interfejs:** [link](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/podmioty-ubiegajace-sie)
- **Próba TAURON_PIPELINE:** HTTP 200; 2026-09-10T11:18:12.5881143Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/tauron_pipeline_landing.html`.
- **Próba TAURON_PIPELINE_PDF:** HTTP 200; 2026-09-10T11:19:38.2544804Z; `data/catalog/probe_results_20260910T111959000Z.json`; próbka `data/raw/research/2026-09-10/tauron_pipeline_retrieved_2026-09-10.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_MAP — Portal dostępnych mocy

[Źródło](https://dostepnemoce.tauron-dystrybucja.pl/)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** connection_capacity_map
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; web application
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** obszar; dostępna moc; inwestycje; wariant
- **Zastosowanie:** Eksploracja opublikowanych możliwości.
- **Ograniczenia:** Nie potwierdzono stabilnego otwartego API eksportu; dane wymagają interpretacji scenariusza.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_PLAN — Plan rozwoju — indeks operatora

[Źródło](https://www.tauron-dystrybucja.pl/plan-rozwoju)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** dokument; horyzont; inwestycja
- **Zastosowanie:** Odkrywanie planów sieci.
- **Ograniczenia:** Nie zwalidowano pełnego wykazu inwestycji ani wszystkich dat realizacji.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_LANDING — Sieć — indeks dokumentów

[Źródło](https://www.stoen.pl/pl/strona/siec)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** source_index
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Regulamin §6: zastrzeżenia komercyjnego użycia i wyjątki; zastosowanie do zbiorów wymaga wyjaśnienia.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** moce; wykazy; rejestr magazynów; plan
- **Zastosowanie:** Odkrywanie aktualizacji publikacji.
- **Ograniczenia:** Nie wszystkie załączniki odczytano; warunki komercyjne wymagają wyjaśnienia.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)
- **Próba STOEN_NETWORK_HTML:** HTTP 200; 2026-09-10T11:19:57.4147344Z; `data/catalog/probe_results_20260910T111959000Z.json`; próbka `data/raw/research/2026-09-10/stoen_network_landing.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_EXPORT — Dostępna moc źródeł — III kwartał 2026

[Źródło](https://www.stoen.pl/files/2026-07/wielkosc-dostepnej-mocy-przylaczeniowej-zrodel-w-sieci-stoen-operator-iii-kw-2026.pdf)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** reported_export_capacity
- **Napięcie:** 15 kV; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** Publikacja kwartalna.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** dzielnica/grupa stacji; napięcie; moc MW; założenia
- **Zastosowanie:** Screening eksportu w jednostce raportowania operatora.
- **Ograniczenia:** Grupy nie są niezależnymi rezerwami wszystkich GPZ.; Część danych wejściowych o małych źródłach z IV kw.2025.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** III kwartał 2026
- **Strona źródła:** 3–5
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)
- **Próba STOEN_EXPORT:** HTTP 200; 2026-09-10T11:21:04.0528357Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/stoen_export_2026_q3.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_IMPORT — Dostępna moc odbiorców — 31.08.2026

[Źródło](https://www.stoen.pl/files/2026-09/wielkosc-dostepnej-mocy-przylaczeniowej-dla-odbiorcow-w-sieci-stoen-operator-31.08.2026r.pdf)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** reported_import_capacity
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** moc odbiorcza; jednostka raportowania; data
- **Zastosowanie:** Scenariusz poboru i ładowania BESS.
- **Ograniczenia:** Potwierdzono format i nagłówek, nie pełną poprawność wszystkich tabel.
- **Data stanu źródła:** 2026-08-31
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)
- **Próba STOEN_IMPORT:** HTTP 200; 2026-09-10T11:21:04.2488455Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/stoen_import_2026-08-31.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_PIPELINE — Wykaz podmiotów powyżej 1 kV — link do PDF

[Źródło](https://www.stoen.pl/files/2026-08/1788176873_zestawienie-informacji-dot.-podmiotow-ubiegajacych-sie-o-przylaczenie-pow.-1kv-stan-na-30.06.2026-r.pdf)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** connection_pipeline
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — nie odczytano tabel
- **Zastosowanie:** Uzupełnienie lokalnego pipeline po walidacji.
- **Ograniczenia:** Link znaleziony na oficjalnej stronie; data 30.06.2026 z nazwy, bez walidacji treści.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_STORAGE — Rejestr magazynów — link do PDF

[Źródło](https://www.stoen.pl/files/2026-01/rejestr-magazynow-energii-stoen-operator-sp.-z-o.o.pdf)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** storage_register
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — nie odczytano tabel
- **Zastosowanie:** Weryfikacja istniejących BESS po sprawdzeniu zakresu rejestru.
- **Ograniczenia:** Nie ustalono pól, progów wpisu ani aktualnej daty stanu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### STOEN_PLAN — Plan rozwoju 2026–2031

[Źródło](https://stoen.pl/strona/plan-rozwoju-w-zakresie-zaspokojenia-obecnego-i-przyszlego-zapotrzebowania-na-energie-elektryczna-na-lata-2026-2031)

- **Operator:** Stoen Operator
- **Właściciel:** Stoen Operator sp. z o.o.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** dokument planu
- **Zastosowanie:** Przyszłe inwestycje po odczycie załącznika.
- **Ograniczenia:** Indeks sieci opisuje plan jako uzgodniony; pełny dokument nie został zwalidowany.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.stoen.pl/strona/regulamin)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PGE_LANDING — Dostępne moce dla źródeł wytwórczych

[Źródło](https://pgedystrybucja.pl/przylaczenia/procedury-przylaczeniowe/dostepne-moce-dla-zrodel-wytworczych)

- **Operator:** PGE Dystrybucja
- **Właściciel:** PGE Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** connection_capacity
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN
- **Zastosowanie:** Ważne pokrycie OSD po rozwiązaniu dostępu.
- **Ograniczenia:** HTTP 200 zawierał 346-bajtową stronę odrzucenia, nie dane.; Nie wnioskować o jakości datasetu z samej blokady.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Nie obchodzić WAF; potwierdzić zwykły dostęp lub oficjalny kanał.
- **Próba PGE_LANDING:** HTTP 200; 2026-09-10T11:18:12.5181247Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/pge_capacity_landing.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PGE_EXPORT_DISCOVERY — Dostępne moce I kwartał 2026 — wskazanie wyszukiwarki

[Źródło](https://pgedystrybucja.pl/content/download/71691b9fb622cdf89306ec0dc0c1ac3d/file/dostepne-moce-pge-i-kw-2026.pdf?contentId=2208&inLanguage=pol-PL&version=6)

- **Operator:** PGE Dystrybucja
- **Właściciel:** PGE Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** reported_export_capacity
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN
- **Zastosowanie:** Sprawdzenie po uzyskaniu dostępu.
- **Ograniczenia:** Treść i aktualność niepotwierdzone; nazwa sugeruje historyczny kwartał.; 16.09.2026 bezpośredni dokument zwrócił HTTP 200 i 346 bajtów HTML zamiast PDF; brak odczytu treści. Metadane: data/catalog/pge_radkowice_access_2026-09-16.json.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-16
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Pobieranie niepotwierdzone: odpowiedź HTML zamiast PDF. Nie wyprowadzono danych z fragmentów wyszukiwarki. Pomoc użytkownika: NEED-011.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PGE_PLAN_DISCOVERY — Konsultacje planu rozwoju — wskazanie strony

[Źródło](https://pgedystrybucja.pl/o-spolce/dzialalnosc/konsultacje-spoleczne-projektu-planu-rozwoju)

- **Operator:** PGE Dystrybucja
- **Właściciel:** PGE Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN
- **Zastosowanie:** Przyszłe inwestycje po zweryfikowaniu treści.
- **Ograniczenia:** Nie potwierdzono pełnego tekstu ani aktualnego statusu uzgodnienia.; 16.09.2026 bezpośredni dokument zwrócił HTTP 200 i 346 bajtów HTML zamiast PDF; brak odczytu treści. Metadane: data/catalog/pge_radkowice_access_2026-09-16.json.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-16
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Pobieranie niepotwierdzone: odpowiedź HTML zamiast PDF. Nie wyprowadzono danych z fragmentów wyszukiwarki. Pomoc użytkownika: NEED-011.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### KGHM_OSD — OSD dla systemu elektroenergetycznego

[Źródło](https://kghm.com/pl/biznes/strefa-energetyczna/osd-dla-systemu-elektroenergetycznego)

- **Operator:** KGHM
- **Właściciel:** KGHM Polska Miedź S.A.
- **Kraj:** PL
- **Kategoria:** local_operator_publications
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Obszar sieci przemysłowej KGHM
- **Format:** HTML; PDF; XLS
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** moce; przyłączenia; odmowy; rejestr magazynów; plany
- **Zastosowanie:** Pokrycie OSDn i dużych odbiorów przemysłowych.
- **Ograniczenia:** Nie jest źródłem ogólnopolskim; nie znormalizowano załączników.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### URE_REGISTERS — BIP URE — rejestry i bazy

[Źródło](https://bip.ure.gov.pl/bip/rejestry-i-bazy)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Urząd Regulacji Energetyki
- **Kraj:** PL
- **Kategoria:** regulatory_registers
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; linked registers
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** podmiot; zakres rejestru; status regulacyjny
- **Zastosowanie:** Kontrola podmiotów i wybranych aktywów OZE.
- **Ograniczenia:** Progi i zakresy różnią się; brak kompletnego mapowania projekt–GPZ.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGY_LAW_516 — Dz.U. 2026 poz. 516 — zmiana Prawa energetycznego

[Źródło](https://dziennikustaw.gov.pl/D2026000051601.pdf)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Dziennik Ustaw / RCL
- **Kraj:** PL
- **Kategoria:** legal_publication_requirements
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Oficjalny akt normatywny; nie stanowi licencji na dane operatorów.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** zakres publikacji; częstotliwość aktualizacji; przepisy przejściowe
- **Zastosowanie:** Interpretacja cykli publikacji OSP/OSD.
- **Ograniczenia:** Przegląd wybranych przepisów, nie pełny audyt prawny wszystkich obowiązków i praw ponownego użycia.
- **Data stanu źródła:** 2026-03-13
- **Publikacja:** 2026-04-15
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 15
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba LAW_2026_516:** HTTP 200; 2026-09-10T11:21:04.3613547Z; `data/catalog/probe_results_20260910T112104907Z.json`; próbka `data/raw/research/2026-09-10/prawo_energetyczne_zmiana_2026_516.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### BIP_ENV_DISCOVERY — Ekoportal — punkt wejścia do informacji środowiskowej

[Źródło](https://ekoportal.gov.pl/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Administracja środowiskowa
- **Kraj:** PL
- **Kategoria:** administrative_project_discovery
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; BIP; PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — potrzebna weryfikacja aktualnego systemu
- **Zastosowanie:** Odkrywanie postępowań środowiskowych; preferować aktualne BIP właściwych organów.
- **Ograniczenia:** Odczyt nie powiódł się; wskazania migracji wymagają sprawdzenia.; Nie potwierdzono aktualnego krajowego API ani kompletności pipeline.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### KRS_API_DOCS — Portal Rejestrów Sądowych — OpenAPI

[Źródło](https://prs.ms.gov.pl/krs/openApi)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Ministerstwo Sprawiedliwości
- **Kraj:** PL
- **Kategoria:** company_identification
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; API documentation
- **API:** DOCUMENTED_NOT_TESTED
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** identyfikatory spółki — do sprawdzenia w schemacie
- **Zastosowanie:** Weryfikacja SPV po znalezieniu udokumentowanego związku z projektem.
- **Ograniczenia:** Odczyt strony ograniczony przez aplikację JS; bez zapytań o podmioty.; KRS nie potwierdza sam związku spółki z punktem przyłączenia.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_EGIB — GUGiK — zbiorcza usługa WFS EGiB

[Źródło](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza?SERVICE=WFS&REQUEST=GetCapabilities)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK / właściwe organy EGiB
- **Kraj:** PL
- **Kategoria:** cadastral_geometry
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Polska; pokrycie usług zależne od dostawców
- **Format:** WFS; XML
- **API:** YES
- **GIS:** WFS_CAPABILITIES_VERIFIED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** typy obiektów; CRS; operacje usługi
- **Zastosowanie:** Działki i budynki jako warstwa przestrzenna.
- **Ograniczenia:** Sprawdzono GetCapabilities, nie pobranie i kompletność wszystkich obiektów.; Nie daje prawa własności ani pełnego zakresu ewidencji.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GUGIK_EGIB_CAPABILITIES:** HTTP 200; 2026-09-10T11:18:13.0680137Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/gugik_egib_capabilities.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_BDOT — BDOT10k — dane topograficzne

[Źródło](https://www.geoportal.gov.pl/pl/dane/baza-danych-obiektow-topograficznych-bdot10k/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK / PZGiK
- **Kraj:** PL
- **Kategoria:** topography_transport_infrastructure
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** GML; WMS; downloads
- **API:** UNKNOWN
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** klasa obiektu; geometria; atrybuty topograficzne
- **Zastosowanie:** Drogi, kolej, obiekty i bariery trasowe.
- **Ograniczenia:** Nie jest modelem elektrycznym ani świadectwem legalnego dostępu do gruntu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://mapy.geoportal.gov.pl/wss/service/PZGIK/BDOT/WMS/PobieranieBDOT10k)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_BDOT_PARQUET — Nowe udostępnianie BDOT10k jako GeoParquet

[Źródło](https://www.geoportal.gov.pl/aktualnosci/nowy-sposob-udostepniania-danych-bdot10k-w-geoportalu/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK
- **Kraj:** PL
- **Kategoria:** structured_topography_download
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** GeoParquet
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** klasa obiektu; geometria; schemat2021
- **Zastosowanie:** Wydajne pobieranie klas zamiast parsowania mapy.
- **Ograniczenia:** Nie pobierano i nie walidowano krajowych paczek.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** 2026-04-16
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_ORTHO — Ortofotomapa GUGiK

[Źródło](https://www.geoportal.gov.pl/pl/dane/ortofotomapa-orto/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK / PZGiK
- **Kraj:** PL
- **Kategoria:** orthophoto
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** raster; WMS; WMTS
- **API:** UNKNOWN
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Oficjalna strona opisuje bezpłatne pobieranie i dowolne wykorzystanie ortofotomapy.
- **Użycie komercyjne:** PERMITTED_AS_DESCRIBED
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** data zdjęcia; rozdzielczość; CRS
- **Zastosowanie:** Kontrola przestrzenna obiektów i korytarzy.
- **Ograniczenia:** Obraz nie potwierdza parametrów elektrycznych ani połączenia.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.geoportal.gov.pl/pl/dane/ortofotomapa-orto/)
- **Powiązane źródło/interfejs:** [link](https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WMS/StandardResolution)
- **Powiązane źródło/interfejs:** [link](https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WMTS/StandardResolution)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_NMT — Numeryczny model terenu

[Źródło](https://www.geoportal.gov.pl/pl/dane/numeryczny-model-terenu-nmt/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK / PZGiK
- **Kraj:** PL
- **Kategoria:** terrain
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** raster; downloads; WCS documentation
- **API:** UNKNOWN
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** wysokość; rozdzielczość; CRS poziomy i pionowy
- **Zastosowanie:** Nachylenie i wstępna analiza trasy.
- **Ograniczenia:** Nie jest geotechniką ani dokumentacją projektową.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_MPZP — Krajowa Integracja MPZP

[Źródło](https://mapy.geoportal.gov.pl/wss/ext/KrajowaIntegracjaMiejscowychPlanowZagospodarowaniaPrzestrzennego?lang=pol)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** GUGiK / gminy
- **Kraj:** PL
- **Kategoria:** spatial_planning
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; WMS integration
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** obszar planu; prezentacja ustaleń; odsyłacze
- **Zastosowanie:** Lokalizacja obowiązujących planów do dalszej weryfikacji.
- **Ograniczenia:** Potrzebne teksty uchwał i aktualność; mapowy obraz nie zastępuje reguł prawnych.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### URBAN_REGISTER — Rejestr Urbanistyczny — publikacje

[Źródło](https://rejestr-urbanistyczny.gov.pl/published)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Administracja publiczna — Rejestr Urbanistyczny
- **Kraj:** PL
- **Kategoria:** spatial_planning_register
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; web application
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — nie zweryfikowano eksportu danych
- **Zastosowanie:** Plany ogólne i dokumenty planistyczne po ocenie pokrycia.
- **Ograniczenia:** Otworzył się interfejs JS; brak testu kompletności i publicznego API.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GDOS_GIS — GDOŚ — WFS form ochrony przyrody

[Źródło](https://sdi.gdos.gov.pl/wfs?SERVICE=WFS&REQUEST=GetCapabilities)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Generalna Dyrekcja Ochrony Środowiska
- **Kraj:** PL
- **Kategoria:** protected_areas_natura2000
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** WFS; WMS; XML
- **API:** YES
- **GIS:** WFS_CAPABILITIES_VERIFIED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** typy warstw; CRS; operacje
- **Zastosowanie:** Przecięcia kandydackich tras z obszarami ochrony.
- **Ograniczenia:** Sprawdzono capabilities, nie wszystkie geometrie; akty ustanawiające ochronę są rozstrzygające.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://www.gov.pl/web/gdos/dostep-do-danych-geoprzestrzennych)
- **Powiązane źródło/interfejs:** [link](https://sdi.gdos.gov.pl/wms)
- **Próba GDOS_CAPABILITIES:** HTTP 200; 2026-09-10T11:18:13.4573839Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/gdos_capabilities.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### WODY_SIGW — SIGW — udostępnianie danych Wód Polskich

[Źródło](https://www.gov.pl/web/wody-polskie/udostepnianie-danych-z-systemu-informacyjnego-gospodarowania-wodami)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Państwowe Gospodarstwo Wodne Wody Polskie
- **Kraj:** PL
- **Kategoria:** flood_and_water_constraints
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** WMS; downloads_on_request
- **API:** UNKNOWN
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Zasady zależą od danych i sposobu udostępnienia; do sprawdzenia dla wybranej warstwy.
- **Użycie komercyjne:** PRODUCT_SPECIFIC
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** zagrożenie; zasięg; produkt; scenariusz
- **Zastosowanie:** Ograniczenia powodziowe i wodne.
- **Ograniczenia:** Przeglądanie nie równa się dowolnemu pobraniu; możliwe opłaty i tryb wnioskowy zależnie od produktu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### BDL_GIS — Bank Danych o Lasach — usługi OGC

[Źródło](https://www9.bdl.lasy.gov.pl/portal/uslugi-ogc?v=1)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Bank Danych o Lasach / Lasy Państwowe
- **Kraj:** PL
- **Kategoria:** forest_constraints
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** WFS; WMS; WMTS; ArcGIS service URLs
- **API:** DOCUMENTED_NOT_TESTED
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** wydzielenia; granice; atrybuty leśne
- **Zastosowanie:** Warstwa ograniczeń leśnych i korytarzy.
- **Ograniczenia:** Nie potwierdzono pobierania masowego ani praw dla wszystkich warstw; nie ustala prawa własności.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://wfs.bdl.lasy.gov.pl/geoserver/BDL/ows)
- **Powiązane źródło/interfejs:** [link](https://mapserver.bdl.lasy.gov.pl/arcgis/services/WMS_BDL_mapa_drzewostanow/MapServer/WMSServer)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENTSOE_TP — Transparency Platform

[Źródło](https://www.entsoe.eu/data/transparency-platform/)

- **Operator:** ENTSO-E
- **Właściciel:** ENTSO-E / dostawcy danych
- **Kraj:** EUROPE
- **Kategoria:** system_timeseries
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Kraje, strefy rynkowe, przekroje; zakres zależny od serii
- **Format:** REST; XML; web portal
- **API:** DOCUMENTED_NOT_TESTED
- **GIS:** UNKNOWN
- **Aktualizacja:** Zależna od produktu i korekt.
- **Historia:** YES; zależne od serii.
- **Uwierzytelnienie:** Konto i token; nie użyto tokenu.
- **Licencja:** Lista danych i wyjątków ponownego wykorzystania; nie cała platforma automatycznie na jednej licencji.
- **Użycie komercyjne:** DATASET_SPECIFIC
- **Autorytet źródła:** A
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** time; area; generation; load; cross_border_flows; outages
- **Zastosowanie:** Kontekst systemowy i weryfikacja szeregów.
- **Ograniczenia:** Nie dostarcza pełnej lokalnej telemetrii GPZ.; Nie wykonano uwierzytelnionego zapytania.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Dokumentacja 20.04.2026 opisuje 400 żądań/min na token; stosować cache, limity i stronicowanie.
- **Warunki:** [źródło prawne](https://transparencyplatform.zendesk.com/hc/en-us/articles/40921911218961-Legal-Terms-and-Conditions)
- **Powiązane źródło/interfejs:** [link](https://transparencyplatform.zendesk.com/hc/en-us/articles/12845911031188-How-to-get-security-token)
- **Powiązane źródło/interfejs:** [link](https://transparencyplatform.zendesk.com/hc/en-us/articles/12783148966036-API-Rate-Limit-Part-1)
- **Powiązane źródło/interfejs:** [link](https://transparencyplatform.zendesk.com/hc/en-us/articles/15692855254548-Sitemap-for-Restful-API-Integration)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENTSOE_MAP — Grid Map — downloads

[Źródło](https://www.entsoe.eu/data/map/downloads/)

- **Operator:** ENTSO-E
- **Właściciel:** ENTSO-E
- **Kraj:** EUROPE
- **Kategoria:** transmission_overview_map
- **Napięcie:** WN/NN według legendy mapy
- **Zasięg:** Europa
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** stacje; linie; legenda
- **Zastosowanie:** Weryfikacja orientacyjnego przebiegu sieci przesyłowej.
- **Ograniczenia:** Wydanie opisane jako aktualizowane w 2024 r.; nie model operacyjny 2026.; Licencji TP nie przenosić na mapę.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### OSM_LICENSE — OpenStreetMap — dane i warunki ODbL

[Źródło](https://www.openstreetmap.org/copyright)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** OpenStreetMap contributors
- **Kraj:** GLOBAL
- **Kategoria:** community_grid_geometry
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Globalna, zmienne pokrycie
- **Format:** OSM PBF; XML; community tags
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** ODbL; atrybucja i warunki dla baz pochodnych.
- **Użycie komercyjne:** CONDITIONAL
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** osm_id; geometry; power tags; voltage; name; operator
- **Zastosowanie:** Geometria pomocnicza i hipotezy relacji.
- **Ograniczenia:** Brak gwarancji kompletności i aktualności; nie są to potwierdzone dane operatora.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** INFERRED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.openstreetmap.org/copyright)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GEOFABRIK_PL — Geofabrik — Poland OSM extract

[Źródło](https://download.geofabrik.de/europe/poland.html)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** OpenStreetMap contributors; extract Geofabrik
- **Kraj:** PL
- **Kategoria:** community_geometry_download
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** OSM PBF; downloads
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** Regularne, zwykle codzienne ekstrakty; odczytać datę konkretnego pliku.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** ODbL dla danych OSM.
- **Użycie komercyjne:** CONDITIONAL
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** OSM objects; tags; version
- **Zastosowanie:** Regionalne pobieranie geometrii bez masowych zapytań Overpass.
- **Ograniczenia:** Nie pobrano całego kraju w tym etapie; dziedziczy ograniczenia OSM.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** INFERRED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.openstreetmap.org/copyright)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### OPENINFRAMAP — OpenInfraMap — opis źródła

[Źródło](https://openinframap.org/about)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autorzy OpenInfraMap / OpenStreetMap contributors
- **Kraj:** GLOBAL
- **Kategoria:** infrastructure_visualization
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Globalna
- **Format:** web map
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Dane OSM: ODbL; interfejs to osobny produkt.
- **Użycie komercyjne:** CONDITIONAL
- **Autorytet źródła:** G
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** infrastruktura z OSM
- **Zastosowanie:** Wizualna inspekcja danych OSM.
- **Ograniczenia:** Nie jest niezależnym źródłem potwierdzającym OSM ani operatorem.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** INFERRED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PYPSA_EUR — PyPSA-Eur

[Źródło](https://github.com/PyPSA/pypsa-eur)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autorzy PyPSA-Eur i właściciele danych wejściowych
- **Kraj:** EUROPE
- **Kategoria:** open_grid_model_workflow
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Europa, konfiguracja modelu
- **Format:** Python; workflow; model datasets
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Repozytorium kodu MIT; prawa wejściowych danych sprawdzać oddzielnie.
- **Użycie komercyjne:** CONDITIONAL
- **Autorytet źródła:** H
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** buses; lines; transformers; generation; load; assumptions
- **Zastosowanie:** Wzorzec budowy modelu referencyjnego i scenariuszy.
- **Ograniczenia:** Modelowe i inferowane parametry nie są aktualnymi danymi operatora.; Licencje wejść odrębne od kodu; nie uruchomiono modelu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** ESTIMATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://arxiv.org/abs/2408.17178)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### MATPOWER_POLAND — MATPOWER case2383wp — historyczny przypadek Polski

[Źródło](https://github.com/MATPOWER/matpower/blob/master/data/case2383wp.m)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autor przypadku / autorzy MATPOWER
- **Kraj:** PL
- **Kategoria:** historical_grid_benchmark
- **Napięcie:** 110 kV; 220 kV; 400 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** MATPOWER .m
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Sprawdzić warunki konkretnego przypadku i wersji niezależnie od biblioteki.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** H
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** bus; branch; gen
- **Zastosowanie:** Test algorytmu i importu formatów.
- **Ograniczenia:** Historyczny przypadek z uproszczeniami; nie aktualna sieć Polski ani geograficzna baza projektów.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** Zima 1999/2000 według opisu pliku
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** ESTIMATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PANDAPOWER — pandapower

[Źródło](https://github.com/e2nIEE/pandapower)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autorzy pandapower
- **Kraj:** GLOBAL
- **Kategoria:** powerflow_library
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Narzędzie niezależne od kraju
- **Format:** Python
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Wymagana kontrola pliku LICENSE przypiętej wersji przed wdrożeniem.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** H
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** model buses/lines/transformers; powerflow results
- **Zastosowanie:** Przyszłe obliczenia przy kompletnych wejściach.
- **Ograniczenia:** Biblioteka nie dostarcza rzeczywistych brakujących danych KSE; nie zainstalowano i nie porównano solverów.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** CALCULATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### VERAGRID — GridCal / VeraGrid

[Źródło](https://github.com/SanPen/VeraGrid)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autorzy VeraGrid
- **Kraj:** GLOBAL
- **Kategoria:** powerflow_library
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Narzędzie niezależne od kraju
- **Format:** Python
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** MPL-2.0 według bieżącego repozytorium; przed wdrożeniem przypiąć wersję.
- **Użycie komercyjne:** CONDITIONAL
- **Autorytet źródła:** H
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** network model; simulation results
- **Zastosowanie:** Alternatywny solver do późniejszego porównania.
- **Ograniczenia:** Nie źródło współczesnej sieci Polski; zmiana nazwy repozytorium wymaga uwzględnienia w dokumentacji.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** CALCULATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### MATPOWER_LIBRARY — MATPOWER

[Źródło](https://github.com/MATPOWER/matpower)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Autorzy MATPOWER
- **Kraj:** GLOBAL
- **Kategoria:** powerflow_library
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Narzędzie niezależne od kraju
- **Format:** MATLAB; Octave
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Kontrola licencji konkretnej wersji i danych wymagana przed użyciem.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** H
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** bus; branch; gen; results
- **Zastosowanie:** Referencyjne obliczenia i testy.
- **Ograniczenia:** Nie utożsamiać licencji kodu z prawami wszystkich przypadków testowych.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** CALCULATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### POWERMODELS — PowerModels.jl

[Źródło](https://github.com/lanl-ansi/PowerModels.jl)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** LANL-ANSI / autorzy PowerModels
- **Kraj:** GLOBAL
- **Kategoria:** optimization_library
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Narzędzie niezależne od kraju
- **Format:** Julia
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Kontrola LICENSE przypiętej wersji przed wdrożeniem.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** H
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** network model; optimization formulation
- **Zastosowanie:** Późniejsze porównanie optymalizacji sieci.
- **Ograniczenia:** Dodatkowy stos wykonawczy; nieuzasadniony na etapie researchu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** CALCULATED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### OPSD_TIMESERIES — Open Power System Data — time series

[Źródło](https://data.open-power-system-data.org/time_series/)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** OPSD / pierwotni dostawcy szeregów
- **Kraj:** EUROPE
- **Kategoria:** historical_system_timeseries
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Europa, zakres zależny od serii
- **Format:** CSV; XLSX; data packages
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** YES
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** DATASET_SPECIFIC
- **Autorytet źródła:** E
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** timestamp; country; load; generation; price
- **Zastosowanie:** Historyczne testy i porównania.
- **Ograniczenia:** Nie źródło bieżących danych 2026; prawa pierwotnych danych odrębne od skryptów.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** 2020-10-06 — przejrzane wydanie
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### ENERGY_CHARTS — Energy-Charts API

[Źródło](https://api.energy-charts.info/openapi.json)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Fraunhofer ISE / dostawcy serii
- **Kraj:** EUROPE
- **Kategoria:** system_timeseries
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Polska potwierdzona dla próbki public_power
- **Format:** REST; JSON; OpenAPI
- **API:** YES
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Anonimowa próbka public_power działała.
- **Licencja:** Próbka v2/public_power zawiera CC BY 4.0 i atrybucję energy-charts.info; nie rozszerzać automatycznie na inne serie/endpoints.
- **Użycie komercyjne:** CONDITIONAL_FOR_VERIFIED_SAMPLE
- **Autorytet źródła:** E
- **Odczyt maszynowy:** YES
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** schema_version; series.id; data.timestamp; data.values; unit; license
- **Zastosowanie:** Kontekst generacji krajowej i porównania.
- **Ograniczenia:** Nie są to lokalne obciążenia GPZ.; Schemat v2: series + data.timestamp/values; nie starszy format unix_seconds/production_types.; Metadane licencji potwierdzono w odpowiedzi API; warunki pozostałych produktów wymagają odrębnej weryfikacji.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** API info.version 2.0
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://api.energy-charts.info/v2/public_power?country=pl&start=2026-09-01&end=2026-09-01)
- **Powiązane źródło/interfejs:** [link](https://energy-charts.info/publishing-notes.html)
- **Próba ENERGY_CHARTS_DOCS:** HTTP 200; 2026-09-10T11:18:13.5516656Z; `data/catalog/probe_results_20260910T111813793Z.json`; próbka `data/raw/research/2026-09-10/energy_charts_index.html`.
- **Próba ENERGY_CHARTS_OPENAPI:** HTTP 200; 2026-09-10T11:19:35.4032129Z; `data/catalog/probe_results_20260910T111959000Z.json`; próbka `data/raw/research/2026-09-10/energy_charts_openapi.json`.
- **Próba ENERGY_CHARTS_SAMPLE:** HTTP 200; 2026-09-10T11:22:48.5049578Z; `data/catalog/probe_results_20260910T112248796Z.json`; próbka `data/raw/research/2026-09-10/energy_charts_pl_sample.json`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### EMBER_API — Ember Energy API — dokumentacja

[Źródło](https://api.ember-energy.org/v1/docs)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Ember
- **Kraj:** GLOBAL
- **Kategoria:** system_energy_data
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Krajowe szeregi według produktu
- **Format:** API documentation
- **API:** DOCUMENTED_NOT_TESTED
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Rejestracja/klucz według interfejsu; nie wykonano zapytania z kluczem.
- **Licencja:** UNKNOWN — sprawdzić regulamin konkretnego produktu API.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** E
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — szczegóły schematu do weryfikacji
- **Zastosowanie:** Porównania krajowe i historyczne.
- **Ograniczenia:** Otwarta strona dokumentacji nie jest testem datasetu; brak danych lokalnej sieci.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Powiązane źródło/interfejs:** [link](https://api.ember-energy.org/signup)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### JRC_IDEES — JRC IDEES-2023

[Źródło](https://data.jrc.ec.europa.eu/dataset/1f0b480c-6d21-4d95-897d-20c7ca33df6f)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** European Commission Joint Research Centre
- **Kraj:** EUROPE
- **Kategoria:** historical_energy_demand_structure
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Państwa UE w zakresie datasetu
- **Format:** dataset downloads; metadata
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** YES — okres 2000–2023 według opisu.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** Do sprawdzenia warunki konkretnej paczki; nie przenosić licencji publikacji na wszystkie wejścia.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** kraj; sektor; rok; zużycie energii
- **Zastosowanie:** Założenia scenariuszy popytu na poziomie agregatów.
- **Ograniczenia:** Aktualizacja metadanych w 2026 nie oznacza obserwacji sieci 2026; brak stacji i feederów.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** IDEES-2023
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### COPERNICUS — Copernicus Data Space — OData i produkty

[Źródło](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

- **Operator:** UNKNOWN / nie dotyczy
- **Właściciel:** Copernicus / ESA / operatorzy CDSE zależnie od produktu
- **Kraj:** GLOBAL
- **Kategoria:** earth_observation
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zależna od produktu satelitarnego
- **Format:** OData; JSON; raster; STAC documentation
- **API:** DOCUMENTED_NOT_TESTED
- **GIS:** DOCUMENTED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Zależna od operacji; pobrania mogą wymagać tokenu.
- **Licencja:** Otwarte zasady danych Sentinel nie obejmują automatycznie wszystkich produktów i treści portalu.
- **Użycie komercyjne:** PRODUCT_SPECIFIC
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** product_id; footprint; acquisition_date; cloud_cover; product_type
- **Zastosowanie:** Pokrycie terenu i materiały do przyszłych modeli przestrzennych.
- **Ograniczenia:** Nie źródło parametrów sieci; brak pobrania próbki produktu.; Sentinel, DEM, portal i usługi mają różne warunki.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-10
- **Udany odczyt:** 2026-09-10
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://dataspace.copernicus.eu/terms-and-conditions)
- **Powiązane źródło/interfejs:** [link](https://documentation.dataspace.copernicus.eu/Quotas.html)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GRID_OZE_REPORT — Mamy przestrzeń dla OZE — raport metodyczny

[Źródło](https://gridw.home.pl/pub/Raport_potencjal_OZE.pdf)

- **Operator:** NOT_AN_OPERATOR
- **Właściciel:** UNEP/GRID-Warszawa i konsorcjum projektu
- **Kraj:** PL
- **Kategoria:** spatial_methodology
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** NO — dokument
- **GIS:** NO — dokument
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono licencji ponownego użycia
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** NO — preferować wskazane API lub plik; brak wdrożenia
- **Pola:** kryteria przestrzenne; bufory; powierzchnia ha; statystyki 18 gmin
- **Zastosowanie:** Inspiracja dla odrębnej oceny przestrzennej PV i wiatru
- **Ograniczenia:** Opracowanie 2025, parametry prawne wymagają osobnej aktualizacji; Nie określa rezerwy sieci ani zasad lokalizacji BESS; Raport opisuje przekazanie GPKG/SHP; nie zweryfikowano publicznej paczki
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GRID_OZE_REPORT:** HTTP 200; 2026-09-17T12:15:07.071618+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/report.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GRID_OZE_PORTAL — Geoportal OZE GRID — ArcGIS WebMap i FeatureServer

[Źródło](https://geoportal-oze.gridw.pl/)

- **Operator:** NOT_AN_OPERATOR
- **Właściciel:** UNEP/GRID-Warszawa; konto publikujące w ArcGIS
- **Kraj:** PL
- **Kategoria:** spatial_screening
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; ArcGIS REST JSON; GeoJSON advertised; PBF advertised
- **API:** YES — odczyt metadanych i query bez konta
- **GIS:** YES — ArcGIS REST FeatureServer
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono licencji ponownego użycia
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** NO — preferować wskazane API lub plik; brak wdrożenia
- **Pola:** TERYT; nazwa gminy; pow_ha; geometria EPSG:3857
- **Zastosowanie:** Warstwy potencjału i ograniczeń przestrzennych, po ustaleniu praw
- **Ograniczenia:** 18 gmin pilotażowych bez Chęcin; inne warstwy mają własny zakres; GPZ bufory 30/40 km nie są topologią ani rezerwą; Puste licenseInfo/copyrightText nie stanowią otwartej licencji; Próbka PV bez geometrii; GeoJSON/PBF deklarowane w metadanych, nie testowane; maxRecordCount 2000 dotyczy odpowiedzi, nie limitu zapytań na czas
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:15:06.325545+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/grid.html`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:15:36.988162+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/grid_app.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:16:06.603601+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/grid_webmap.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:16:06.759916+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/grid_metadata.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:17:00.525784+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/pv_layer.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:17:00.697275+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/pv_metadata.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:17:00.997329+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/gminy_sample.json`.
- **Próba GRID_OZE_PORTAL:** HTTP 200; 2026-09-17T12:17:01.995814+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/pv_sample.json`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### EMP_PW — Energetyczna Mapa Polski — katalog źródeł wytwórczych

[Źródło](https://emp.pw.edu.pl/mapa)

- **Operator:** NOT_AN_OPERATOR
- **Właściciel:** Koło Naukowe Energetyków Politechniki Warszawskiej
- **Kraj:** PL
- **Kategoria:** generation_asset_discovery
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; JavaScript; JSON
- **API:** YES — GET /api/v1/units odczytane bez konta
- **GIS:** UNKNOWN — współrzędne w JSON; WMS/WFS nie potwierdzono
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono licencji ponownego użycia
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** NO — preferować wskazane API lub plik; brak wdrożenia
- **Pola:** id; slug; name; unit_type; latitude; longitude; power_installed; owner; bibliography; parent_unit_slug; status
- **Zastosowanie:** Poszukiwanie projektów i źródeł pierwotnych, kontrola nazw i lokalizacji
- **Ograniczenia:** 173 rekordy w pobranej odpowiedzi nie dowodzą kompletności kraju; Brak jawnych dat aktualizacji rekordów, GPZ i PCC w sprawdzonym schemacie; Kody statusu 0/1 nie zostały zmapowane na cykl projektu; Możliwe relacje rodzic-dziecko; nie sumować mocy bez deduplikacji; Nie potwierdzono licencji, stabilności API ani limitów; brak wdrożonego cyklicznego pobierania
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba EMP_PW:** HTTP 200; 2026-09-17T12:15:06.530559+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/emp.html`.
- **Próba EMP_PW:** HTTP 200; 2026-09-17T12:15:37.334888+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/emp.js`.
- **Próba EMP_PW:** HTTP 200; 2026-09-17T12:16:18.665795+00:00; `data/catalog/probe_results_oze_2026-09-17.json`; próbka `data/raw/research/2026-09-17/oze/emp_units.json`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_OZE_DETAIL_2026 — Geoportal krajowy — szczegółowe usługi potencjału OZE

[Źródło](https://www.geoportal.gov.pl/aktualnosci/nowe-uslugi-potencjalu-oze-dane-szczegolowe/)

- **Operator:** NOT_AN_OPERATOR
- **Właściciel:** GUGiK / MKiŚ
- **Kraj:** PL
- **Kategoria:** spatial_potential
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML; WMS announced
- **API:** UNKNOWN
- **GIS:** YES — WMS ogłoszone; endpointów nie przetestowano
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono licencji ponownego użycia
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL
- **Scraping:** NO — preferować wskazane API lub plik; brak wdrożenia
- **Pola:** potencjał technologii OZE; potencjał magazynowania energii
- **Zastosowanie:** Kolejka do weryfikacji krajowej alternatywy przestrzennej
- **Ograniczenia:** Komunikat 15.06.2026; nie przetestowano usług ani licencji warstw; Potencjał magazynowania nie jest dostępną mocą przyłączeniową
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_INVESTMENTS_RADK — Portal inwestycji PSE — sekcja Radkowice

[Źródło](https://inwestycje.pse.pl/mapa_inwestycji_pse/)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV; 110 kV
- **Zasięg:** Polska; do pilota odczytano sekcję Radkowice
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — HTML wymaga rozpoznania sekcji
- **Scraping:** YES — dla tego widoku HTML; brak wdrożonego cyklicznego scrapera
- **Pola:** nazwa inwestycji; etap; status; rok zakończenia
- **Zastosowanie:** Oddzielenie zakończonych i przyszłych prac w stacji pilota
- **Ograniczenia:** Brak gwarantowanej częstotliwości aktualizacji i daty każdej zmiany; Wspólna nazwa stacji nie identyfikuje automatycznie tego samego zadania lub transformatora; Raport wpływu za 2023 rok i portal podają różne lata dla podobnie nazwanego zadania transformatora; zakres i data odbioru nierozstrzygnięte.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba PSE_INVESTMENTS_RADK:** HTTP 200; 2026-09-15T16:30:45.448433+00:00; `data/catalog/probe_results_radkowice_followup_2026-09-15.json`; próbka `data/raw/research/2026-09-15/pse_investments_2026-09-15.html`.
- **Próba PSE_INVESTMENTS_RADK:** HTTP 200; 2026-09-17T06:40:16.579444+00:00; `data/catalog/probe_results_radkowice_investment_dates_2026-09-17.json`; próbka `data/raw/research/2026-09-17/pse_investment_map_2026-09-17.html`.
- **Próba PSE_INVESTMENTS_RADK:** HTTP 200; 2026-09-11T10:42:22.0922672Z; `data/catalog/radkowice_snapshot_manifest.json`; próbka `data/raw/research/2026-09-11/pse_investments.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### CHECINY_ENERGY_PLAN — BIP Chęcin — założenia energetyczne 2025–2027 z perspektywą 2040

[Źródło](https://checiny.biuletyn.net/fls/bip_pliki/2026_03/BIPF64CD10561EC15Z/PZCEEPG_2025-2027.pdf)

- **Operator:** PSE / PGE — informacje przypisane w dokumencie gminy
- **Właściciel:** Gmina Chęciny — publikujący dokument; pierwotne dane PSE/PGE
- **Kraj:** PL
- **Kategoria:** local_grid_and_investments
- **Napięcie:** 220 kV; 110 kV; SN
- **Zasięg:** Gmina Chęciny i opisane powiązania sieciowe
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL — tekst PDF i schematy
- **Scraping:** NO — bezpośredni PDF; ekstrakcja i kontrola dokumentu
- **Pola:** stacje; relacje linii; napięcia; planowane inwestycje; operator danych
- **Zastosowanie:** Dowody topologii referencyjnej i plany dla Radkowic
- **Ograniczenia:** Mieszane daty wejść i starsze opisy planistyczne; Nie potwierdza aktualnych granic własności ani obsady transformatorów; Folder 2026_03 w URL nie jest datą obserwacji wszystkich wartości
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 21–25 (numeracja PDF od 1)
- **Sprawdzono:** 2026-09-11
- **Udany odczyt:** 2026-09-11
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba CHECINY_ENERGY_PLAN:** HTTP 200; 2026-09-11T10:42:22.6213255Z; `data/catalog/radkowice_snapshot_manifest.json`; próbka `data/raw/research/2026-09-11/checiny_energy_plan.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_TARIFF_2026 — Taryfa PSE 2026 — odbiorcy i miejsca dostarczania

[Źródło](https://www.pse.pl/documents/20182/7005343691/20260116_Tekst_Taryfy_na_2026_tekst_jednolity.pdf)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** operator_delivery_points
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — tekst PDF
- **Scraping:** NO — bezpośredni PDF
- **Pola:** symbol odbiorcy; nazwa operatora; nazwa węzła; typ MD; grupa MD
- **Zastosowanie:** Potwierdzenie relacji taryfowej PGE–Radkowice; nie własność urządzeń
- **Ograniczenia:** Tabela może pozostawać niezmieniona mimo zmian umów; nie jest bieżącą telemetrią ani schematem własności; source_date dotyczy tabel 6 i 7, nie wszystkich rozdziałów taryfy
- **Data stanu źródła:** 2025-12-03
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** Tekst uwzględniający decyzję z 16.01.2026; data tabel inna
- **Strona źródła:** 42, 43, 46 — tabele 6/7 i ich data stanu
- **Sprawdzono:** 2026-09-11
- **Udany odczyt:** 2026-09-11
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba PSE_TARIFF_2026:** HTTP 200; 2026-09-11T10:50:16.7756540Z; `data/catalog/radkowice_tariff_snapshot.json`; próbka `data/raw/research/2026-09-11/pse_tariff_2026.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PGE_RADK_CAPACITY_ATTEMPT — Próba dostępu do pliku mocy PGE I kw.2026

[Źródło](https://pgedystrybucja.pl/content/download/71691b9fb622cdf89306ec0dc0c1ac3d/file/dostepne-moce-pge-i-kw-2026.pdf?contentId=2208&inLanguage=pol-PL&version=6)

- **Operator:** PGE
- **Właściciel:** PGE Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** reported_connection_capacity
- **Napięcie:** UNKNOWN_OR_NOT_APPLICABLE
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** PDF — oczekiwany, nie otrzymany
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** UNKNOWN — pełna treść nie została zweryfikowana.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN — przed scraperem preferować oficjalny plik lub API.
- **Pola:** UNKNOWN — brak poprawnego pliku
- **Zastosowanie:** Kandydat do informacji o grupach mocy PGE po poprawnym odczycie
- **Ograniczenia:** HTTP 200, 346 bajtów, brak sygnatury PDF; nie pobrano wartości mocy; Dowód próby: data/catalog/pge_radkowice_access_2026-09-11.json
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-11
- **Udany odczyt:** UNKNOWN / nie dotyczy
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### SUW_RADK_WOLICA_3_2024 — Decyzja 3/2024 — przebudowa odcinka Radkowice–Wolica

[Źródło](https://bip.kielce.uw.gov.pl/download/2/33548/decprzesylnr324.pdf)

- **Operator:** PGE Dystrybucja — wnioskodawca
- **Właściciel:** Wojewoda Świętokrzyski / Świętokrzyski Urząd Wojewódzki
- **Kraj:** PL
- **Kategoria:** grid_investment_administrative_decision
- **Napięcie:** 110 kV
- **Zasięg:** Odcinek w gminach Morawica i Chęciny
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL — tekst i tabela PDF
- **Scraping:** NO — bezpośredni plik PDF
- **Pola:** relacja linii; napięcie; wnioskodawca; parametry planowanego odcinka; data decyzji
- **Zastosowanie:** Historyczny dowód relacji 110 kV i osobny rekord inwestycji
- **Ograniczenia:** Nie potwierdza realizacji inwestycji; 991,8 m dotyczy zakresu decyzji, nie całej linii; Brak aktualnej obciążalności i dokładnej granicy własności PSE/PGE
- **Data stanu źródła:** 2024-11-29
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** SPN.III.747.20.2024, decyzja 3/2024
- **Strona źródła:** 1–3
- **Sprawdzono:** 2026-09-11
- **Udany odczyt:** 2026-09-11
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba SUW_RADK_WOLICA_3_2024:** HTTP 200; 2026-09-11T13:40:11.4850806Z; `data/catalog/probe_results_radkowice_wolica_2026-09-11.json`; próbka `data/raw/research/2026-09-11/radkowice_wolica_decision_3_2024.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_RADK_BRIDGE_NOTICE_2025 — PSE — ogłoszenie 205815-2025, pole 220 kV i most Radkowice

[Źródło](https://www.pse.pl/documents/20182/5928746423/OKRESOWE_OGLOSZENIE_ROBOTY_BUDOWLANE.pdf/883a7669-eb9a-4650-84f4-cd67502fd545?safeargs=76657273696f6e3d312e31)

- **Operator:** PSE S.A.
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV
- **Zasięg:** Radkowice i opisane zadanie
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Pobrano publicznie bez konta; HTTP 200.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — tekst dokumentu wymaga walidacji kontekstu
- **Scraping:** PDF download
- **Pola:** nazwa zakresu; numer ogłoszenia; okres prognozy postępowań; zastrzeżenie informacyjnego charakteru
- **Zastosowanie:** Publiczny punkt odniesienia dla projektu mostu, bez obsadzenia i bez parametrów technicznych
- **Ograniczenia:** Prognoza zamówień, nie wynik przetargu ani dowód ukończenia; Adres zamawiającego nie jest geometrią stacji; Brak liczby miejsc, MW i przypisań projektów
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** 2025-03-31
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 29; metadane 37
- **Sprawdzono:** 2026-09-15
- **Udany odczyt:** 2026-09-15
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy snapshot z timeoutem i SHA-256. Nie ustalono API, limitów ani gwarantowanego cyklu; brak wdrożonej automatyzacji.
- **Próba PSE_RADK_BRIDGE_NOTICE_2025:** HTTP 200; 2026-09-15T16:30:45.003171+00:00; `data/catalog/probe_results_radkowice_followup_2026-09-15.json`; próbka `data/raw/research/2026-09-15/pse_bridge_notice_2025.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### RDOS_RADK_PIASKI_NOTICE_2025 — RDOŚ Kielce — obwieszczenie dotyczące Radkowice–Kielce Piaski

[Źródło](https://www.gov.pl/web/rdos-kielce/obwieszczenie-regionalnego-dyrektora-ochrony-srodowiska-w-kielcach-z-dnia-04122025-r-znak-woo-i42072025pjpp16)

- **Operator:** RDOŚ Kielce
- **Właściciel:** RDOŚ Kielce
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV
- **Zasięg:** Radkowice i opisane zadanie
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Pobrano publicznie bez konta; HTTP 200.
- **Licencja:** Gov.pl: treści tekstowe CC BY-SA 4.0, zastrzeżenia dla praw osób trzecich; ocena załączników osobno.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL — tekst dokumentu wymaga walidacji kontekstu
- **Scraping:** HTML parsing; brak wdrożonego cyklicznego scrapera
- **Pola:** znak obwieszczenia; znak decyzji; nazwa przedsięwzięcia; data obwieszczenia; data publikacji
- **Zastosowanie:** Potwierdzenie publicznej informacji o decyzji środowiskowej dla przebudowy 220 kV
- **Ograniczenia:** Nie potwierdza prawomocności, uruchomienia ani obciążalności; Nie utożsamiać całego zadania stacji z mostem
- **Data stanu źródła:** 2025-12-04
- **Publikacja:** 2025-12-09
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** Nagłówek i treść obwieszczenia
- **Sprawdzono:** 2026-09-15
- **Udany odczyt:** 2026-09-15
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy snapshot z timeoutem i SHA-256. Nie ustalono API, limitów ani gwarantowanego cyklu; brak wdrożonej automatyzacji.
- **Warunki:** [źródło prawne](https://www.gov.pl/web/gov/prawa-autorskie)
- **Próba RDOS_RADK_PIASKI_NOTICE_2025:** HTTP 200; 2026-09-15T16:30:45.228667+00:00; `data/catalog/probe_results_radkowice_followup_2026-09-15.json`; próbka `data/raw/research/2026-09-15/rdos_radkowice_piaski_2025.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### RDOS_RADK_PIASKI_DECISION_2025 — RDOŚ Kielce — pełna decyzja dla przebudowy linii Radkowice–Kielce Piaski

[Źródło](https://www.gov.pl/attachment/27ef7a8e-5094-4391-be1c-7e23cb1038b2)

- **Operator:** RDOŚ Kielce
- **Właściciel:** RDOŚ Kielce
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV
- **Zasięg:** Radkowice i opisane zadanie
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Pobrano publicznie bez konta; HTTP 200.
- **Licencja:** Dokument urzędowy; zasady Gov.pl zweryfikowano, zakres praw do załącznika i materiałów osób trzecich wymaga odrębnej oceny.
- **Użycie komercyjne:** REQUIRES_PERMISSION_REVIEW
- **Autorytet źródła:** C
- **Odczyt maszynowy:** PARTIAL — tekst dokumentu wymaga walidacji kontekstu
- **Scraping:** Pobranie PDF i ekstrakcja tekstu; walidacja kontekstu i numerów stron
- **Pola:** znak decyzji; data decyzji; słup 81; dotychczasowe pole 8; projektowane pole 6; około 60 m — tylko przebudowywane przęsło
- **Zastosowanie:** Dokumentacyjna topologia przyszła, rozdzielona od stanu aktualnego i mostu
- **Ograniczenia:** Plan przebudowy, nie potwierdzenie wykonania ani prawomocności; 60 m nie oznacza długości całej linii; Nie potwierdza parametrów mostu, jego obsadzenia ani dostępnych MW
- **Data stanu źródła:** 2025-12-04
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** 1: znak i data; 3: planowane przełączenie przęsła
- **Sprawdzono:** 2026-09-15
- **Udany odczyt:** 2026-09-15
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy snapshot z timeoutem i SHA-256. Nie ustalono API, limitów ani gwarantowanego cyklu; brak wdrożonej automatyzacji.
- **Warunki:** [źródło prawne](https://www.gov.pl/web/gov/prawa-autorskie)
- **Próba RDOS_RADK_PIASKI_DECISION_2025:** HTTP 200; 2026-09-15T16:42:41.935208+00:00; `data/catalog/probe_results_radkowice_decision_2026-09-15.json`; próbka `data/raw/research/2026-09-15/rdos_radkowice_piaski_decision_2025.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_IMPACT_REPORT_2023 — PSE — raport wpływu za 2023 rok, edycja 2024

[Źródło](https://api-raport.pse.pl/uploads/PSE-Zintegrowany_Raport_Wplywu_2023.pdf)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV; 110 kV
- **Zasięg:** Polska; sprawdzona wzmianka o Radkowicach
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** Raport roczny; brak zweryfikowanej gwarancji terminu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Publiczny PDF pobrany bez konta, HTTP 200.
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji raportu ani prawa do jego redystrybucji.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — tekst PDF; kontekst listy na poprzedniej stronie
- **Scraping:** Pobranie oficjalnego PDF, bez scrapingu HTML
- **Pola:** rok raportowany; zakończone zadania; nazwa inwestycji
- **Zastosowanie:** Porównanie historycznych deklaracji wykonania inwestycji
- **Ograniczenia:** Rok wymiany transformatora wymaga wyjaśnienia wobec portalu inwestycji wskazującego 2025.; Podobna nazwa nie ustala identyczności zakresu; brak numeru jednostki i mocy MVA.; Sprawdzono wskazany fragment, nie wszystkie 291 stron.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** Edycja 2024; rok raportowany 2023
- **Strona źródła:** 47–48
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy GET, timeout, zachowane bajty i SHA-256. API/GIS dla tego raportu nie ustalono.
- **Próba PSE_IMPACT_REPORT_2023:** HTTP 200; 2026-09-17T06:40:16.437810+00:00; `data/catalog/probe_results_radkowice_investment_dates_2026-09-17.json`; próbka `data/raw/research/2026-09-17/pse_impact_report_2023.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_PRSP_2027_2036_POST_CONSULTATION — Projekt PRSP 2027–2036 po konsultacjach — kwiecień 2026

[Źródło](https://www.pse.pl/documents/20182/7102190804/PRSP_2027-2036-dokument_glowny_projekt_po_konsultacji.pdf/de2f004f-8a80-4264-907a-a38d52c5d50f?safeargs=76657273696f6e3d312e30)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 110 kV; 220 kV; 400 kV
- **Zasięg:** Polska; zweryfikowano dwa wpisy inwestycji wokół Radkowic
- **Format:** PDF
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Publiczny dokument bez logowania
- **Licencja:** UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — warstwa tekstowa PDF; ograniczony parser dwóch wierszy
- **Scraping:** NO — bezpośredni PDF
- **Pola:** identyfikator zadania w dokumencie; opis; cel; rok rozpoczęcia; rok zakończenia
- **Zastosowanie:** Scenariusze przyszłych inwestycji z jawną wersją planu
- **Ograniczenia:** Projekt po konsultacjach; nie potwierdzono uzgodnienia tej wersji.; Zakończenie obejmuje wymiar techniczny, finansowy i formalny, nie jest datą załączenia.; Wpis nie zapewnia dodatkowej dostępnej mocy ani identyczności zakresu z innymi zadaniami.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** Projekt po konsultacjach, kwiecień 2026
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba PSE_PRSP_2027_2036_POST_CONSULTATION:** HTTP 200; 2026-09-17T11:04:59.379112+00:00; `data/catalog/probe_results_radkowice_prsp_2026-09-17.json`; próbka `data/raw/research/2026-09-17/pse_prsp_2027_2036_post_consultation.pdf`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### EBIN_ELECTRICITY — ebin.josm.pl — mapa sieci i konfiguracja warstw

[Źródło](https://ebin.josm.pl/electricity/)

- **Operator:** Community map — not grid operator
- **Właściciel:** Autor ebin.josm.pl; dane OpenStreetMap contributors
- **Kraj:** PL
- **Kategoria:** community_grid_geometry
- **Napięcie:** 110 kV; 220 kV; SN
- **Zasięg:** Mapa Europy i Polski; sprawdzono konfigurację i widok Radkowic
- **Format:** HTML; JavaScript; TileJSON; vector PBF (metadata only)
- **API:** TileJSON/vector tiles; no bulk service permission established
- **GIS:** YES
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public read without login
- **Licencja:** ODbL-1.0 for OSM data; map software and tile service conditions separate
- **Użycie komercyjne:** CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** NO — structured OSM XML preferred to copying rendered map
- **Pola:** OSM identity; object version; tags; geometry
- **Zastosowanie:** Geographic reference and candidate network topology, subject to operator verification
- **Ograniczenia:** Community data are not operator-verified, exhaustive or an operational switching diagram.; OSM operator tag is not ownership of all equipment.; Map declares 2026-02-26 update; individual OSM object edit dates differ.; No confirmed thermal ratings, loading or available MW.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.openstreetmap.org/copyright)
- **Próba EBIN_ELECTRICITY:** HTTP 200; 2026-09-17T11:40:39.685129+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/ebin_electricity_landing.html`.
- **Próba EBIN_ELECTRICITY:** HTTP 200; 2026-09-17T11:41:06.040649+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/ebin_electricity_map.js`.
- **Próba EBIN_ELECTRICITY:** HTTP 200; 2026-09-17T11:41:06.085406+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/ebin_electricity_locales.js`.
- **Próba EBIN_ELECTRICITY:** HTTP 200; 2026-09-17T11:41:36.780070+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/ebin_power_poland_tilejson.json`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### OSM_RADK_STATION_OBJECT — OSM — obiekt stacji Radkowice, way 199098055

[Źródło](https://www.openstreetmap.org/api/0.6/way/199098055/full)

- **Operator:** Community map — not grid operator
- **Właściciel:** OpenStreetMap contributors
- **Kraj:** PL
- **Kategoria:** community_grid_geometry
- **Napięcie:** 110 kV; 220 kV; SN
- **Zasięg:** Mały obszar stacji Radkowice
- **Format:** OSM XML
- **API:** YES — OSM read API
- **GIS:** YES
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public read without login
- **Licencja:** ODbL-1.0 for OSM data; map software and tile service conditions separate
- **Użycie komercyjne:** CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** NO — structured OSM XML preferred to copying rendered map
- **Pola:** OSM identity; object version; tags; geometry
- **Zastosowanie:** Geographic reference and candidate network topology, subject to operator verification
- **Ograniczenia:** Community data are not operator-verified, exhaustive or an operational switching diagram.; OSM operator tag is not ownership of all equipment.; Edit timestamps are not measurement or commissioning dates.; No confirmed thermal ratings, loading or available MW.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.openstreetmap.org/copyright)
- **Próba OSM_RADK_STATION_OBJECT:** HTTP 200; 2026-09-17T11:44:23.034423+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/osm_radkowice_way_199098055.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### OSM_RADK_STATION_AREA — OSM — próbka obszaru stacji Radkowice

[Źródło](https://www.openstreetmap.org/api/0.6/map?bbox=20.516927,50.783155,20.527321,50.792370)

- **Operator:** Community map — not grid operator
- **Właściciel:** OpenStreetMap contributors
- **Kraj:** PL
- **Kategoria:** community_grid_geometry
- **Napięcie:** 110 kV; 220 kV; SN
- **Zasięg:** Mały obszar stacji Radkowice
- **Format:** OSM XML
- **API:** YES — OSM read API
- **GIS:** YES
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public read without login
- **Licencja:** ODbL-1.0 for OSM data; map software and tile service conditions separate
- **Użycie komercyjne:** CONDITIONAL — ODbL attribution and applicable database obligations; service terms separate
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** NO — structured OSM XML preferred to copying rendered map
- **Pola:** OSM identity; object version; tags; geometry
- **Zastosowanie:** Geographic reference and candidate network topology, subject to operator verification
- **Ograniczenia:** Community data are not operator-verified, exhaustive or an operational switching diagram.; OSM operator tag is not ownership of all equipment.; Edit timestamps are not measurement or commissioning dates.; No confirmed thermal ratings, loading or available MW.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-17
- **Udany odczyt:** 2026-09-17
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://www.openstreetmap.org/copyright)
- **Próba OSM_RADK_STATION_AREA:** HTTP 200; 2026-09-17T11:45:03.826411+00:00; `data/catalog/probe_results_osm_radkowice_2026-09-17.json`; próbka `data/raw/research/2026-09-17/osm_radkowice_station_area.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PSE_RADK_STAGES — Portal inwestycji PSE — etapy modernizacji Radkowic

[Źródło](https://inwestycje.pse.pl/)

- **Operator:** PSE
- **Właściciel:** PSE S.A.
- **Kraj:** PL
- **Kategoria:** grid_investments
- **Napięcie:** 220 kV; 110 kV
- **Zasięg:** Polska; do pilota odczytano sekcję Radkowice
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** UNKNOWN
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN — nie ustalono licencji redystrybucji treści portalu
- **Użycie komercyjne:** UNKNOWN
- **Autorytet źródła:** B
- **Odczyt maszynowy:** PARTIAL — HTML wymaga rozpoznania sekcji
- **Scraping:** YES — dla tego widoku HTML; brak wdrożonego cyklicznego scrapera
- **Pola:** Etap I/II; Status publikowany; Nagłówek
- **Zastosowanie:** Rozdzielenie etapów modernizacji od zakończonej wymiany transformatora.
- **Ograniczenia:** Brak daty stanu i aktualizacji wpisów.; Brak identyfikatora PRSP i konkretnych urządzeń.; Status strony nie potwierdza odbioru ani dostępnej mocy.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-18
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowe pobranie HTML; parser h4 z kontrolą nagłówków. Brak potwierdzonego API i warunków stałego pobierania.
- **Próba PSE_RADK_STAGES:** HTTP 200; 2026-09-18T06:33:11.170759+00:00; `data/catalog/probe_results_radkowice_stages_2026-09-18.json`; próbka `data/raw/research/2026-09-18/pse_investments_home.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_MAP_HOME — TAURON — portal biznesowy z mapą

[Źródło](https://dostepnemoce.tauron-dystrybucja.pl/)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** station_dictionary_discovery
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public page; REST client uses timestamp/signature, not tested
- **Licencja:** Map database bulk extraction/reuse restricted by displayed operator terms; no permission established
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** B
- **Odczyt maszynowy:** HTML/JS; no validated dictionary export
- **Scraping:** UNKNOWN
- **Pola:** point code/name discovery; source limitations
- **Zastosowanie:** Ocena możliwości zbiorczej identyfikacji stacji
- **Ograniczenia:** Publiczna strona ładuje mapę; nie stanowi kompletnego eksportu stacji.; Brak zgody na komercyjny import bazy; nie potwierdzono zgodności kodów z wykazem PDF.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-18
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba TAURON_MAP_HOME:** HTTP 200; 2026-09-18T12:02:53.943948+00:00; `data/catalog/probe_results_tauron_dictionary_2026-09-18.json`; próbka `data/raw/research/2026-09-18/tauron_map_home.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_MAP_SCRIPT — TAURON — interfejs i zastrzeżenia mapy

[Źródło](https://dostepnemoce.tauron-dystrybucja.pl/wp-content/plugins/tauron-maps/mapy.js?ver=1788435768)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** station_dictionary_discovery
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** JavaScript
- **API:** DISCOVERED_IN_CLIENT_CODE_NOT_TESTED
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public page; REST client uses timestamp/signature, not tested
- **Licencja:** Map database bulk extraction/reuse restricted by displayed operator terms; no permission established
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** B
- **Odczyt maszynowy:** HTML/JS; no validated dictionary export
- **Scraping:** UNKNOWN
- **Pola:** point code/name discovery; source limitations
- **Zastosowanie:** Ocena możliwości zbiorczej identyfikacji stacji
- **Ograniczenia:** Kod wskazuje podpisywany REST oraz losowe przesuwanie znaczników GPZ; nie pobrano bazy endpointów.; Brak zgody na komercyjny import bazy; nie potwierdzono zgodności kodów z wykazem PDF.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-18
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba TAURON_MAP_SCRIPT:** HTTP 200; 2026-09-18T12:03:25.080362+00:00; `data/catalog/probe_results_tauron_dictionary_2026-09-18.json`; próbka `data/raw/research/2026-09-18/tauron_mapy.js`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_PENDING_MAP — TAURON — regionalny wykaz obiektów planowanych

[Źródło](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** station_dictionary_discovery
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public page; REST client uses timestamp/signature, not tested
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** B
- **Odczyt maszynowy:** HTML/JS; no validated dictionary export
- **Scraping:** UNKNOWN
- **Pola:** point code/name discovery; source limitations
- **Zastosowanie:** Ocena możliwości zbiorczej identyfikacji stacji
- **Ograniczenia:** Nawigacja do publikacji regionalnych, nie potwierdzony słownik kodów.; Brak zgody na komercyjny import bazy; nie potwierdzono zgodności kodów z wykazem PDF.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-18
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba TAURON_PENDING_MAP:** HTTP 200; 2026-09-18T12:02:54.504596+00:00; `data/catalog/probe_results_tauron_dictionary_2026-09-18.json`; próbka `data/raw/research/2026-09-18/tauron_pending_map.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### TAURON_GPZ_LODZKIE — TAURON — publikacja GPZ województwa łódzkiego

[Źródło](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace/gpz-lodzkie)

- **Operator:** TAURON Dystrybucja
- **Właściciel:** TAURON Dystrybucja S.A.
- **Kraj:** PL
- **Kategoria:** station_dictionary_discovery
- **Napięcie:** SN; 110 kV
- **Zasięg:** Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** VIEWER_ONLY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Public page; REST client uses timestamp/signature, not tested
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** B
- **Odczyt maszynowy:** HTML/JS; no validated dictionary export
- **Scraping:** UNKNOWN
- **Pola:** point code/name discovery; source limitations
- **Zastosowanie:** Ocena możliwości zbiorczej identyfikacji stacji
- **Ograniczenia:** W próbce nazwa Dworszowice i podział wnioski/planowane; brak potwierdzonego powiązania nazwa–kod wykazu PDF.; Brak zgody na komercyjny import bazy; nie potwierdzono zgodności kodów z wykazem PDF.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-18
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba TAURON_GPZ_LODZKIE:** HTTP 200; 2026-09-18T12:04:34.556557+00:00; `data/catalog/probe_results_tauron_dictionary_2026-09-18.json`; próbka `data/raw/research/2026-09-18/tauron_gpz_lodzkie.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_OWNERSHIP_GROUPS — Mapa własności — grupy rejestrowe

[Źródło](https://www.gov.pl/web/gugik/nowa-usluga-mapa-wlasnosci---grupy-rejestrowe-dostepna-w-modulach-geoportal-krajowy-i-geodezja-i-kartografia-w-serwisie-wwwgeoportalgovpl)

- **Operator:** GUGiK
- **Właściciel:** GUGiK / organy prowadzące EGiB
- **Kraj:** PL
- **Kategoria:** land_ownership
- **Napięcie:** 
- **Zasięg:** Polska; pokrycie nieweryfikowane
- **Format:** HTML
- **API:** UNKNOWN
- **GIS:** DISCOVERED_NOT_TESTED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** C
- **Odczyt maszynowy:** UNKNOWN
- **Scraping:** UNKNOWN
- **Pola:** grupa rejestrowa działki — do weryfikacji
- **Zastosowanie:** Struktura własności powierzchni w buforze 1 km od stacji
- **Ograniczenia:** Komunikat potwierdza zasilanie mapy danymi powiatowych WFS oraz różnice kompletności między powiatami.; Nie zweryfikowano samego endpointu mapy grup rejestrowych ani praw do komercyjnego wykorzystania.; Zbiorczy WFS EGiB deklaruje GRUPA_REJESTROWA, ale cztery odczytane działki koło Radkowic mają puste pole; próbka nie mierzy całego bufora.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-19
- **Udany odczyt:** 2026-09-18
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GUGIK_OWNERSHIP_NEWS:** HTTP 200; 2026-09-18T18:14:51.710807+00:00; `data/catalog/probe_results_land_ownership_2026-09-18.json`; próbka `data/raw/research/2026-09-18/gugik_ownership_news.html`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### KIELCE_EGIB_OWNERSHIP_DISCOVERY — Powiat kielecki — schematy publicznych usług WFS

[Źródło](https://geoportal.powiat.kielce.pl/map/geoportal/wfse.php)

- **Operator:** Powiat kielecki
- **Właściciel:** Starosta Kielecki
- **Kraj:** PL
- **Kategoria:** land_ownership_discovery
- **Napięcie:** 
- **Zasięg:** Próbki: Radkowice i Brzeziny, powiat kielecki
- **Format:** WFS; XML; GML
- **API:** WFS 2.0.0
- **GIS:** WFS_SCHEMA_VERIFIED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** NO
- **Pola:** ID_DZIALKI; geometria; GRUPA_REJESTROWA — tylko usługa zbiorcza, puste w próbce
- **Zastosowanie:** Ocena dostępności własności gruntów w otoczeniu stacji
- **Ograniczenia:** Oba schematy działek zawierają identyfikatory, nazwy, datę i geometrię; nie deklarują grupy rejestrowej.; Brak pola w tych schematach nie oznacza braku informacji w EGiB lub innych usługach.; Portal zawiera ograniczenia kopiowania/publikacji; zakres praw do wykorzystania danych WFS pozostaje nierozstrzygnięty.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-19
- **Udany odczyt:** 2026-09-19
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba KIELCE_WFS_INFO:** HTTP 200; 2026-09-18T18:14:18.281463+00:00; `data/catalog/probe_results_land_ownership_2026-09-18.json`; próbka `data/raw/research/2026-09-18/kielce_wfs_info.html`.
- **Próba KIELCE_EGIB_CAPS:** HTTP 200; 2026-09-18T18:14:18.363976+00:00; `data/catalog/probe_results_land_ownership_2026-09-18.json`; próbka `data/raw/research/2026-09-18/kielce_egib_caps.xml`.
- **Próba KIELCE_EGIB_SCHEMA:** HTTP 200; 2026-09-18T18:14:18.443767+00:00; `data/catalog/probe_results_land_ownership_2026-09-18.json`; próbka `data/raw/research/2026-09-18/kielce_egib_schema.xml`.
- **Próba KIELCE_EGIB_FULL_CAPS:** HTTP 200; 2026-09-18T18:14:51.066511+00:00; `data/catalog/probe_results_land_ownership_2026-09-18.json`; próbka `data/raw/research/2026-09-18/kielce_egib_full_caps.xml`.
- **Próba KIELCE_EGIB_FULL_SCHEMA:** HTTP 200; 2026-09-19T04:59:30.351046+00:00; `data/catalog/probe_results_land_ownership_2026-09-19.json`; próbka `data/raw/research/2026-09-19/kielce_egib_full_schema.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_EGIB_OWNERSHIP_PROBE — GUGiK — próba grupy rejestrowej w zbiorczym WFS

[Źródło](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza)

- **Operator:** GUGiK
- **Właściciel:** GUGiK / Starosta Kielecki
- **Kraj:** PL
- **Kategoria:** land_ownership_discovery
- **Napięcie:** 
- **Zasięg:** Ograniczone próbki: Radkowice, Brzeziny i Grudziądz
- **Format:** WFS; XML; GML
- **API:** WFS 2.0.0
- **GIS:** WFS_SCHEMA_VERIFIED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** NO
- **Pola:** ID_DZIALKI; geometria; GRUPA_REJESTROWA — uzupełniona w próbce Grudziądza, pusta w otoczeniu Radkowic
- **Zastosowanie:** Ocena dostępności własności gruntów w otoczeniu stacji
- **Ograniczenia:** Pole GRUPA_REJESTROWA opcjonalne: cztery rekordy z otoczenia Radkowic puste; dwa rekordy z Grudziądza z grupami 9 i 7. DATA puste we wszystkich tych próbkach.; Próbki prostokątne z COUNT=3, nie pełny bufor 1 km; brak podstaw do procentowego podziału własności. Zgodność WMS/WFS dla jednego ID nie jest niezależnym potwierdzeniem.; Brak interpretacji grup rejestrowych i brak potwierdzenia warunków regularnego komercyjnego importu.; Paginacja potwierdzona na 2 stronach po 1 działce; numberMatched unknown. Capabilities: ImplementsResultPaging TRUE, PagingIsTransactionSafe FALSE, CountDefault 1000. Koniec stron nie dowodzi spójnego snapshotu.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-19
- **Udany odczyt:** 2026-09-19
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GUGIK_EGIB_SCHEMA:** HTTP 200; 2026-09-19T05:00:11.241775+00:00; `data/catalog/probe_results_land_ownership_2026-09-19.json`; próbka `data/raw/research/2026-09-19/gugik_egib_schema.xml`.
- **Próba GUGIK_EGIB_RADK_SAMPLE:** HTTP 200; 2026-09-19T05:00:48.830247+00:00; `data/catalog/probe_results_land_ownership_2026-09-19.json`; próbka `data/raw/research/2026-09-19/gugik_radkowice_parcels_sample.gml`.
- **Próba GUGIK_EGIB_RADK_STATION_SAMPLE:** HTTP 200; 2026-09-19T05:01:28.986980+00:00; `data/catalog/probe_results_land_ownership_2026-09-19.json`; próbka `data/raw/research/2026-09-19/gugik_radkowice_station_sample.gml`.
- **Próba GUGIK_OWNERSHIP_GRUDZIADZ_WFS:** HTTP 200; 2026-09-19T05:30:54.546684+00:00; `data/catalog/probe_results_ownership_comparison_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_grudziadz_wfs.gml`.
- **Próba GUGIK_OWNERSHIP_PAGING_CAPS:** HTTP 200; 2026-09-19T10:39:51.250945+00:00; `data/catalog/probe_results_ownership_paging_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_paging_caps.xml`.
- **Próba GUGIK_OWNERSHIP_PAGING_PAGE_0:** HTTP 200; 2026-09-19T10:39:55.133171+00:00; `data/catalog/probe_results_ownership_paging_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_paging_page_0.xml`.
- **Próba GUGIK_OWNERSHIP_PAGING_PAGE_1:** HTTP 200; 2026-09-19T10:39:58.634922+00:00; `data/catalog/probe_results_ownership_paging_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_paging_page_1.xml`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### GUGIK_OWNERSHIP_MAP — GUGiK — WMS Mapa własności i kompletność powiatowa

[Źródło](https://mapy.geoportal.gov.pl/wss/ext/MapaWlasnosci)

- **Operator:** GUGiK
- **Właściciel:** GUGiK / Starosta Kielecki
- **Kraj:** PL
- **Kategoria:** land_ownership_discovery
- **Napięcie:** 
- **Zasięg:** Polska; próbki: powiat kielecki oraz miasta na prawach powiatu Poznań, Grudziądz, Warszawa
- **Format:** WMS; XML; HTML; JSON
- **API:** WMS 1.3.0
- **GIS:** WMS_SAMPLE_VERIFIED
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** UNKNOWN
- **Użycie komercyjne:** NOT_CLEARED
- **Autorytet źródła:** C
- **Odczyt maszynowy:** YES
- **Scraping:** NO
- **Pola:** grupa rejestrowa; identyfikator działki; czas pozyskania; statystyki powiatowe
- **Zastosowanie:** Ocena dostępności własności gruntów w otoczeniu stacji
- **Ograniczenia:** Stan usługi, nie pełny stan EGiB: powiat kielecki 264634 działki bez grupy; aktualizacja ostatniego podzbioru 17.09.2026 00:07.; GetFeatureInfo text/plain bez atrybutów, HTML zawiera wartości; GetMap application/json zwraca siatkę UTFGrid z pustym data, nie geometrię działek.; Fees NONE i AccessConstraints NONE w capabilities nie rozstrzygają pełnych praw komercyjnych. Statystyki liczbowe powiatu nie są udziałami powierzchni bufora.; Porównanie 19.09.2026: Poznań 120070 i Grudziądz 24217 działek, po 0 bez grupy; Warszawa 287525 bez grupy. To kompletność kategorii w zbiorze usługi, nie powierzchnia ani kompletność EGiB.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-19
- **Udany odczyt:** 2026-09-19
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Próba GUGIK_OWNERSHIP_POZNAN_AREA:** HTTP 200; 2026-09-19T05:30:20.650306+00:00; `data/catalog/probe_results_ownership_comparison_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_poznan_area.html`.
- **Próba GUGIK_OWNERSHIP_GRUDZIADZ_AREA:** HTTP 200; 2026-09-19T05:30:21.192920+00:00; `data/catalog/probe_results_ownership_comparison_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_grudziadz_area.html`.
- **Próba GUGIK_OWNERSHIP_WARSAW_AREA:** HTTP 200; 2026-09-19T05:30:21.876213+00:00; `data/catalog/probe_results_ownership_comparison_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_warsaw_area.html`.
- **Próba GUGIK_OWNERSHIP_GRUDZIADZ_PARCEL:** HTTP 200; 2026-09-19T05:30:51.949828+00:00; `data/catalog/probe_results_ownership_comparison_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_grudziadz_parcel.html`.
- **Próba GUGIK_OWNERSHIP_MAP_CAPS:** HTTP 200; 2026-09-19T05:16:48.679521+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_capabilities.xml`.
- **Próba GUGIK_OWNERSHIP_MAP_PARCEL:** HTTP 200; 2026-09-19T05:20:06.249967+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_parcel_info.txt`.
- **Próba GUGIK_OWNERSHIP_MAP_COUNTY:** HTTP 200; 2026-09-19T05:20:07.040822+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_county_info.txt`.
- **Próba GUGIK_OWNERSHIP_MAP_PARCEL_HTML:** HTTP 200; 2026-09-19T05:20:32.558262+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_parcel_html.html`.
- **Próba GUGIK_OWNERSHIP_MAP_COUNTY_HTML:** HTTP 200; 2026-09-19T05:20:33.106000+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_county_html.html`.
- **Próba GUGIK_OWNERSHIP_MAP_PARCEL_VECTOR:** HTTP 200; 2026-09-19T05:20:33.671004+00:00; `data/catalog/probe_results_ownership_map_2026-09-19.json`; próbka `data/raw/research/2026-09-19/ownership_map_parcel_vector.txt`.

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

### PYPROJ_TRANSFORMER — pyproj 3.7.2 — Transformer i licencja

[Źródło](https://pyproj4.github.io/pyproj/stable/api/transformer.html)

- **Operator:** Open source
- **Właściciel:** pyproj contributors
- **Kraj:** International
- **Kategoria:** software_library
- **Napięcie:** 
- **Zasięg:** Transformacje CRS; w projekcie Polska EPSG:4326/2180
- **Format:** HTML; Python
- **API:** Python Transformer
- **GIS:** CRS_TRANSFORMATION_LIBRARY
- **Aktualizacja:** UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.
- **Historia:** UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.
- **Uwierzytelnienie:** Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.
- **Licencja:** MIT — zachowanie noty praw autorskich i licencji
- **Użycie komercyjne:** YES_UNDER_LICENSE
- **Autorytet źródła:** G
- **Odczyt maszynowy:** YES
- **Scraping:** NO
- **Pola:** always_xy; allow_ballpark; only_best; pipeline; accuracy
- **Zastosowanie:** Transformacja geometrii do metrycznego CRS przed obliczeniami powierzchni
- **Ograniczenia:** Licencja biblioteki nie dotyczy danych EGiB.; Dokładność transformacji nie jest dokładnością danych źródłowych.; W projekcie tryb offline; wersje pyproj i zależności przypięte w requirements-gis.txt.
- **Data stanu źródła:** UNKNOWN / nie dotyczy
- **Publikacja:** UNKNOWN / nie dotyczy
- **Wersja:** UNKNOWN / nie dotyczy
- **Strona źródła:** UNKNOWN / nie dotyczy
- **Sprawdzono:** 2026-09-19
- **Udany odczyt:** 2026-09-19
- **Klasyfikacja wejścia:** REPORTED
- **Automatyzacja:** Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.
- **Warunki:** [źródło prawne](https://github.com/pyproj4/pyproj/blob/3.7.2/LICENSE)

Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.

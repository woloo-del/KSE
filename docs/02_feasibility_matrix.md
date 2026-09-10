# Wstępna macierz wykonalności

**10.09.2026 — wynik badań etapu 1; nie jest deklaracją wdrożonej funkcjonalności.** Pełne dowody, daty i linki: [raport](01_data_research.md) i [katalog](data_sources.md). Identyfikatory poniżej odnoszą się do katalogu JSON.

`AVAILABLE_DIRECTLY` oznacza dostępność określonej informacji w zbadanym zakresie źródła, nie całego kraju ani całego poziomu napięcia. `CALCULABLE` wymaga wskazanych wejść i nie obejmuje imputowania braków. `ESTIMABLE` dopuszcza tylko jawnie warunkowy model. `NOT_CURRENTLY_AVAILABLE` dotyczy wiarygodnego produktu o opisanym zakresie w sprawdzonych źródłach publicznych.

| Moduł / precyzyjnie określona wielkość | Klasa | Dowód i warunek | Ograniczenie / wynik przy braku wejść |
|---|---|---|---|
| Wskazane stacje, rozdzielnie i szyny w publikacji PSE | AVAILABLE_DIRECTLY | PSE_API: próbka `specwezlow` | Nie jest kompletnym grafem ani listą wszystkich GPZ |
| Opublikowane miejsce przyłączenia konkretnego projektu | AVAILABLE_DIRECTLY | PSE_PIPELINE, TAURON_PIPELINE; dokument wskazuje miejsce | Może być nieustalone; WP nie oznacza fizycznego przyłączenia |
| Pełna liczba wszystkich projektów na dowolnym GPZ | NOT_CURRENTLY_AVAILABLE | Nie wykazano kompletności publicznych wykazów i przypisań | Nie przedstawiać znanej części jako pełnej liczby |
| Liczba znanych projektów przypisanych dokumentem do punktu | CALCULABLE | Deduplikacja, spójny snapshot, status i pewność relacji | Raportować pokrycie i projekty nieprzypisane |
| Moc znanych projektów na tym samym punkcie | CALCULABLE | Jawne MW i definicja mocy; PSE_PIPELINE / wykazy OSD | Osobno kierunek, etap, zainstalowana moc i PCC; nie jest przepływem |
| Pełna istniejąca generacja danego GPZ | NOT_CURRENTLY_AVAILABLE | URE_REGISTERS i wykazy operatorów mają różne zakresy | Możliwy częściowy udokumentowany inwentarz |
| Wskazana przez operatora moc przyłączeniowa w jego jednostce raportowania | AVAILABLE_DIRECTLY | PSE_CAPACITY, ENERGA_EXPORT/IMPORT, STOEN_EXPORT/IMPORT | Horyzont, grupa ograniczeń, kierunek i założenia są częścią wartości |
| Niezależna bieżąca wolna moc dowolnego GPZ | NOT_CURRENTLY_AVAILABLE | Brak kompletnej topologii, lokalnych profili i parametrów | `value=null`, `classification=UNKNOWN` |
| Moc znamionowa konkretnego transformatora opisana w dokumencie | AVAILABLE_DIRECTLY | Tylko jeśli właściwy dokument podaje parametr i obiekt | Ten research nie zwalidował pełnego inwentarza; brak wartości = UNKNOWN |
| Krajowy kompletny rejestr mocy transformatorów GPZ | NOT_CURRENTLY_AVAILABLE | Nie znaleziono kompletnego otwartego zbioru w badanym zakresie | Nie wnioskować z napięcia, zdjęcia lub typowej konstrukcji |
| Rzeczywiste obciążenie dowolnego transformatora GPZ | NOT_CURRENTLY_AVAILABLE | Brak publicznego pełnego pokrycia telemetrią | Moc znamionowa i suma PV nie wystarczą |
| Obciążenie dowolnej linii 110 kV | NOT_CURRENTLY_AVAILABLE | Brak parametrów i bieżącego układu/profili | Mapy linii nie pozwalają tego wyliczyć |
| Dane o bilansie i generacji na poziomie KSE | AVAILABLE_DIRECTLY | PSE_API; Energy-Charts jako dodatkowe źródło | Nie przenosić na lokalny GPZ |
| Raportowane redysponowanie z rozróżnieniem przyczyny | AVAILABLE_DIRECTLY | PSE_API poze-redoze, schemat i próbka | Lokalizacja ograniczenia nie wynika z agregatu; null nie jest zerem |
| Congestion konkretnego elementu w dowolnej lokalizacji | NOT_CURRENTLY_AVAILABLE | Brak powszechnego lokalnego dowodu | Możliwy opis udokumentowanego ograniczenia, bez udawanej mapy przeciążeń |
| Moc eksportowa/importowa BESS jako osobne pola projektu | AVAILABLE_DIRECTLY | PSE_PIPELINE i kierunkowe wykazy w badanym zakresie | Dostępność konkretnego pola zależy od rekordu; brak MWh nie uzupełniać domysłem |
| Czas magazynowania przy znanych MWh i mocy rozładowania | CALCULABLE | MWh / MW, dodatni mianownik, jawne znaczenie mocy i pojemności | Wymaga zgodnych nominalnych/użytecznych wartości; nie oznacza profilu pracy |
| Techniczna możliwość przyłączenia dowolnego BESS | NOT_CURRENTLY_AVAILABLE | Osobne import/eksport nie zastępują pełnej analizy sieci | Możliwy screening przesłanek dla obu kierunków |
| Scenariuszowy profil generacji PV/Wind | ESTIMABLE | Potrzebne parametry instalacji, pogoda, metoda i walidacja | Jeszcze nie wdrożono ani nie zwalidowano lokalnego modelu profili |
| Zastępcza lokalizacja/relacja sieciowa | ESTIMABLE | Kilka zgodnych dowodów; wynik relacji oznaczony INFERRED | Samo najbliższe GPZ nie wystarcza; konflikt zachować |
| Pełny łańcuch project–feeder–GPZ–PSE dla każdego projektu | NOT_CURRENTLY_AVAILABLE | Fragmenty dokumentacyjne + pomocnicza geometria | Dopuszczalne nieznane odcinki grafu |
| Udokumentowane planowane inwestycje | AVAILABLE_DIRECTLY | PSE_PLAN, ENERGA_PLAN, ENEA_PLAN | Projekt/uzgodnienie/realizacja to odrębne statusy |
| Przyszła dostępna moc z konkretnego wariantu publikacji | AVAILABLE_DIRECTLY | Jeśli operator podał wartość, datę i założenia; PSE_CAPACITY | Nie wyliczać prostym dodaniem MVA inwestycji do obecnych MW |
| Przyszła fizyczna dostępność każdego punktu | NOT_CURRENTLY_AVAILABLE | Brak kompletnych przyszłych profili, topologii i realizacji planów | Możliwa narracja wariantowa, nie gwarancja |
| Potencjalne korytarze i przecięcia ograniczeń GIS | CALCULABLE | Zweryfikowana geometria, CRS i aktualne warstwy | Nie jest prawem do gruntu ani pełną wykonalnością trasy |
| Rzeczywista możliwość pozyskania trasy przyłącza | NOT_CURRENTLY_AVAILABLE | Potrzebne prawa do nieruchomości, uzgodnienia i projekt techniczny | Publiczne działki i WMS nie wystarczą |
| Grid Connection Score 0–100 o zwalidowanej trafności | NOT_CURRENTLY_AVAILABLE | Nie skalibrowano wag, celu i zbioru referencyjnego | Nie wyświetlać arbitralnej liczby |
| Procentowe prawdopodobieństwo uzyskania WP | NOT_CURRENTLY_AVAILABLE | Brak reprezentatywnych etykiet wyników i wystarczających predyktorów | Nie utożsamiać historycznego udziału odmów z szansą konkretnego projektu |
| Historia wiedzy od rozpoczęcia archiwizacji | CALCULABLE | Snapshoty, manifesty, wersje normalizacji i metody | Nie odtworzy brakujących historycznych źródeł sprzed archiwizacji |

Najważniejsze rozróżnienie: wiarygodne przepisanie wartości operatora jest możliwe znacznie wcześniej niż wiarygodne obliczenie tej samej wielkości samodzielnie. Produkt powinien wyraźnie pokazywać, którą czynność wykonał.

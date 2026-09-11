# Propozycja pilota GPZ

11.09.2026 — propozycja zakresu do zatwierdzenia; nie oznacza uruchomienia MVP.

Pierwszy wynik: audytowalny raport jednego GPZ z powiązanymi projektami, stanem źródeł, kierunkami mocy i ograniczeniami. Obszar wybieramy po porównaniu dowodów, nie po liczbie punktów na mapie. Użytkownik może wskazać własny region.

## Kryteria odbioru

1. Stacja ma potwierdzonego operatora, napięcia, nazwę źródłową i identyfikator lokalny. Relacje 110 kV/PSE wskazują dowody albo pozostają nieznane.
2. Każdy wiersz projektu wskazuje dokument, wersję, stronę/wiersz, datę pobrania oraz dosłowny status źródłowy. Wykazane konflikty wykluczają pewne wnioski o bieżącym stanie.
3. Grupy A/B/C odpowiadają specyfikacji GPZ. Nieznany status jest osobną kategorią; brak daty WP nie oznacza oczekiwania.
4. Import, eksport, moc zainstalowana i PCC są rozdzielone. Brakujące wartości pozostają null. Wiele wniosków nie powoduje automatycznie wielokrotnego liczenia inwestycji.
5. Wszystkie pozycje wybranego pilota przechodzą ręczne porównanie z dokumentem. Błędne lub niejednoznaczne pozycje pozostają poza pewnymi agregatami; publikujemy liczebność próby i wyniki kontroli.
6. Raport można odtworzyć z wersji kodu, konfiguracji i niezmiennego snapshotu. Parser odrzuca nieznany format, a testy obejmują rzeczywiste próbki i izolowane przypadki błędów.
7. Prawa źródeł i dopuszczalny zakres zastosowania muszą być rozstrzygnięte przed produkcyjnym użyciem. Publiczny PDF nie jest dowodem licencji.

Wynik opisuje znane projekty i ograniczenia danych. Nie deklaruje pełnej listy projektów, pewnej rezerwy MW, obciążenia transformatora ani skalibrowanego prawdopodobieństwa przyłączenia. Wagi Grid Connection Score wymagają późniejszej, osobnej metodologii.

Najbliższe zależności: zaakceptować zakres, wybrać dopuszczone źródła, porównać kandydatów GPZ, zaprojektować model i wdrożyć parsery. Kontrola jakości źródeł może być rozwijana niezależnie od wyboru regionu.

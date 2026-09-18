# Słownik kodów TAURON — przegląd dostępu

Sprawdzono 18.09.2026. Cel: znaleźć zbiorcze powiązanie kodów z wykazu PDF z nazwami stacji. **Nie uzyskano jeszcze zweryfikowanego słownika.** Ustalono natomiast konkretną ścieżkę techniczną i ograniczenia, które trzeba rozstrzygnąć przed importem.

## Ustalenia

1. Publiczny [portal](https://dostepnemoce.tauron-dystrybucja.pl/) ładuje [skrypt mapy](https://dostepnemoce.tauron-dystrybucja.pl/wp-content/plugins/tauron-maps/mapy.js?ver=1788435768). Skrypt wskazuje REST `/wp-json/tauron/v1` z zasobami `wytworcy`, `odbiorcy`, `oze`, `wnioski`. Żądania klienta zawierają timestamp i podpis. To odkrycie interfejsu w kodzie, nie potwierdzenie publicznej licencji API ani udanej odpowiedzi. Nie generowano podpisów i nie pobierano bazy przez te endpointy.
2. Normalizacja w kliencie przewiduje pola `id`, `name`, `gpz_code`/`code`, `lat`, `lng`, `is_active`, `is_external`; inne listy odwołują się do `id_gpz` oraz `gpz_kod`. Możliwe jest więc istnienie słownika, ale jego pokrycie, aktualność i zgodność z kodami PDF pozostają niezweryfikowane.
3. Kod `createRandomMaskedGpzLatLng` oraz użycie tej funkcji przy budowie markerów pokazują losowe przesunięcie środka znacznika o 250–600 m; promień obszaru GPZ ustawiono na 500 m. Dotyczy to prezentacji tej warstwy mapy. Nie oznacza dokładności wszystkich danych GIS ani opisu każdej mapy TAURONA. Współrzędnych widocznego znacznika nie wolno używać jako dokładnej lokalizacji stacji lub podstawy potwierdzonego dopasowania przestrzennego.
4. Funkcja `getLegalHtml`, punkty 7 i 9, deklaruje aktualizację co najmniej kwartalną oraz ogranicza pobieranie i wtórne wykorzystywanie całej bazy lub istotnej części bez uprzedniej zgody, z wyjątkami przewidzianymi prawem. Odnotowujemy treść zastrzeżenia operatora; nie ustalono uprawnienia projektu do masowego importu ani warunków komercyjnego użycia.
5. Oddzielny [wykaz regionalny](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace) prowadzi do [strony łódzkiej](https://www.tauron-dystrybucja.pl/przylaczenie-do-sieci/dostepne-moce/wnioski-wp-oczekujace/gpz-lodzkie). Odczytano próbkę dla Dworszowic z rozdziałem kompletnych wniosków oraz wydanych WP/umów. Nie znaleziono w tej próbce jawnego powiązania z kodem wykazu PDF. Nie przypisano stacji kodu na podstawie skrótu nazwy i nie znormalizowano mocy tabeli.

## Decyzja dla projektu

Nie uruchamiać zbiorczego pobierania bazy mapy na podstawie samej dostępności skryptu. Zachować odnośniki i wiedzę o interfejsie; ustalić możliwość uzyskania oficjalnego eksportu kod–nazwa–lokalizacja wraz z warunkami użycia (NEED-019/020). Nie wysłano żadnej wiadomości w imieniu użytkownika. W międzyczasie niezależny audyt PSE i poprawa ekstrakcji kolumn PDF TAURON mogą postępować bez tej bazy.

624 grupy TAURON nadal pozostają grupami kod + poziom napięcia, nie kanonicznymi stacjami. Interfejs nie otrzymuje nowych punktów mapy. Brak licencji nie jest oceną sytuacji sieciowej stacji.

## Audyt i odtworzenie

Cztery publiczne pliki HTML/JS zachowano w niezmienionej postaci, z adresami, czasem pobrania i SHA-256 w `data/catalog/probe_results_tauron_dictionary_2026-09-18.json`. Archiwum: `data/archives/tauron_dictionary_discovery_2026-09-18.zip`; manifest `data/catalog/tauron_dictionary_archive_2026-09-18.json`. Surowe strony, parametry strony i cache nie trafiają do Git. Zapisany skrypt analizowano jako tekst — nie wykonywano go lokalnie. Nie pobierano kafli mapy ani danych konta.

Techniczny przegląd obejmował HTML, wskazany skrypt i jedną publikację regionalną. Nie potwierdzono WMS/WFS/WMTS, stabilnego eksportu, limitów API ani cyklu aktualizacji regionalnego wykazu. Nie jest to dowód ich nieistnienia. Rejestr nie zawiera tokenów ani podpisanych URL.

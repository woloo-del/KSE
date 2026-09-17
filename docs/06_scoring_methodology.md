# Status Grid Connection Score

## Obowiązująca decyzja produktowa — 17.09.2026

Aplikacja dostarcza użytkownikowi fakty, przesłanki korzystne, ryzyka, sprzeczności i niewiadome do jego decyzji. **Nie szacuje możliwości przyłączenia, wolnych MW, obciążenia ani prawdopodobieństwa WP i nie tworzy Grid Connection Score.** To wyłączenie z zakresu, nie odroczenie funkcji. Dane przepływowe od operatorów i model rozpływowy nie są warunkiem rozwoju ani aktywnym celem pozyskania.

Modernizacja może być przesłanką korzystną, gdy jej zakres dotyczy analizowanego punktu; plan nie oznacza dostępnej mocy. Znane przyłączone lub planowane inwestycje mogą wskazywać potencjalną konkurencję o udokumentowaną wspólną infrastrukturę. Sama liczba projektów nie dowodzi negatywnego wpływu lub przeciążenia. Znaczenie zależy od kierunku pracy, napięcia, relacji sieciowej i terminu. Brak dowodu oznacza neutralny kontekst lub niewiadomą.

Można prezentować wartości opublikowane przez operatora z ich datą, jednostką raportowania i założeniami; nie przeliczać ich na własną ocenę dostępności dla projektu użytkownika. Jakość danych opisujemy oddzielnie. Nie sumujemy przesłanek do werdyktu technicznego ani punktacji. Ustawienia zakresu: `config/product_policy.json`. Starsze treści poniżej mają charakter historyczny w zakresie sprzecznym z tą decyzją.

**10.09.2026 — metoda nie jest jeszcze zdefiniowana ani wdrożona.**

`Grid Connection Score = null`, `Estimated connection probability = null`. Badanie nie dostarczyło reprezentatywnego zbioru wyników przyłączeniowych, który uzasadniałby wagi, progi lub procentowe prawdopodobieństwo. Historyczne odmowy mogą być powtórzeniami prób i dotyczyć innych parametrów niż oceniany projekt.

| Potencjalna zmienna | Stan dowodów |
|---|---|
| Raportowana dostępność kierunkowa | Dostępna dla określonych jednostek i założeń operatorów |
| Znany pipeline i etap | Częściowo dostępny; wymaga deduplikacji i relacji infrastrukturalnych |
| Planowane wzmocnienia | Dostępne dokumentacyjnie; terminy i realizacja nie są pewne |
| Napięcie i odległość | Dostępne/obliczalne przy znanym obiekcie i geometrii; sama odległość nie rozstrzyga |
| Obciążenia i topologia ruchowa | Brak pełnego publicznego pokrycia |
| Elastyczność BESS | Parametry kierunkowe częściowo dostępne; strategia pracy i akceptacja warunków często nieznane |
| Odmowy, curtailment i redysponowanie | Konieczny właściwy zakres przestrzenny i przyczyna; brak podstaw do automatycznej lokalnej kary |

Data Confidence jest osobną charakterystyką: autorytet źródła, aktualność, kompletność pól, pewność topologii, pokrycie projektów i konflikty. W etapie 1 opisujemy te wymiary tekstowo. Nie nadano im pozornej skali procentowej i nie utożsamiono autorytetu oficjalnego źródła z pewnością możliwości przyłączenia.

Do przyszłego opracowania: zdefiniować cel wskaźnika, zbiór referencyjny, sposób traktowania braków, niezależną walidację i analizę błędów według technologii/napięcia. Każda wersja metody ma być zapisana i nie może po cichu reinterpretować poprzednich raportów.

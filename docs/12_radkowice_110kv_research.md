# Radkowice–Wolica: dowód dla sieci 110 kV

Weryfikacja: **11.09.2026**. [Decyzja Wojewody Świętokrzyskiego nr 3/2024, znak SPN.III.747.20.2024](https://bip.kielce.uw.gov.pl/download/2/33548/decprzesylnr324.pdf), wydana 29.11.2024 na rzecz PGE Dystrybucja, opisuje przebudowę istniejącej linii 110 kV SE Radkowice–GPZ Wolica. Strony 1–3 zawierają zakres i parametry. Nie potwierdza to ukończenia robót ani własności całej stacji Radkowice.

Zakres tej decyzji obejmuje **991,8 m**, jeden tor i planowane przewody AFLs-10 300 mm². To długość odcinka objętego decyzją, nie długość całej linii. Nie przeliczamy przekroju przewodów na dostępną moc przyłączeniową bez warunków obciążalności, pozostałych ograniczeń i modelu pracy sieci.

Wersja `radkowice_documentary_v2` zawiera **13 obiektów i 13 relacji**. Dodano odniesienie do Wolicy, linię 110 kV oraz osobny rekord inwestycji. PGE występuje jako wnioskodawca inwestycji. Planowane parametry pozostają w rekordzie inwestycji; aktualna obciążalność i stan realizacji są nieznane. Poprzedni graf v1 pozostaje zachowany.

Odtworzenie po przywróceniu wszystkich źródeł:

```powershell
python scripts/build_radkowice_graph.py --version 2
python -m unittest discover -s tests -v
```

Manifest źródła: `data/catalog/probe_results_radkowice_wolica_2026-09-11.json`. Paczka źródłowa: `data/archives/radkowice_wolica_2026-09-11.zip`; manifest `data/catalog/radkowice_wolica_archive.json`. Zachowano bajty i sprawdzono hash. Nie potwierdzono zewnętrznej kopii zapasowej.

Plik PDF pobrano bez logowania, z bezpośredniego adresu BIP. Nie potwierdzono API dla tej kolekcji ani licencji na cały zbiór/załączniki. Jednorazowy odczyt nie jest wdrożeniem cyklicznego scrapera. Przed automatyzacją trzeba ustalić warunki ponownego wykorzystywania i limity.

Pozostałe tropy wyszukiwarki: decyzja 2/2024 oraz projekt planu rozwoju PGE 2026–2031. Pełnych dokumentów tych dwóch tropów nie udało się odczytać w tym kroku; dat i wartości z ich snippetów nie włączono do modelu.

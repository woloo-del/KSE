# Granice metody oceny dostępności

**10.09.2026 — wymagania badawcze, brak zaimplementowanego silnika mocy.**

Pierwszy raport powinien oddzielać:

1. **Fakty:** parametry i deklaracje z publikacji, wraz z datą, jednostką raportowania i zakresem.
2. **Obliczenia:** tylko deterministyczne wyniki z jawnych wejść, np. suma znanych unikalnych projektów w jednym kierunku i etapie.
3. **Założenia i estymacje:** odrębne od faktów, z metodą i analizą wrażliwości.
4. **Niewiadome:** brakujące połączenia, parametry, profile i nieznane pokrycie pipeline.

Publikowana dostępna moc i moc znamionowa urządzeń to różne wielkości. Niedopuszczalne jest utożsamianie `MVA transformatora − MW znanej generacji` z wolną mocą przyłączeniową. Nie wolno też odejmować po raz drugi projektów już uwzględnionych w wariancie raportu operatora.

Scenariusz opisuje osobno stan sieci (`CURRENT_GRID`, `FUTURE_GRID` + rok), wariant założeń (`BASE_CASE`, `CONSERVATIVE`, `OPTIMISTIC`) i kierunek BESS (`CHARGING`, `DISCHARGING`). Horyzont nie potwierdza wykonania inwestycji. Ograniczenie PCC jest niezależne od zainstalowanych składników hybrydy.

Przed power-flow wymagane są co najmniej kompletne dla badanego obszaru: topologia, szyny, impedancje, limity linii, parametry transformatorów, generacja, pobór i założenia ruchowe. Analiza N-1 wymaga również jawnej listy zdarzeń i ograniczeń. Gdy te dane są niedostępne, wynik mocy pozostaje UNKNOWN, a raport może opisywać przesłanki i ryzyka.

W badaniu nie ustalono parametrów pozwalających wyznaczyć wiarygodny przedział wolnej mocy dla dowolnego GPZ. Nie utworzono sztucznych zakresów MW ani współczynników zastępczych. Dowody: [raport, rozdziały 3–4 i 8–9](01_data_research.md).

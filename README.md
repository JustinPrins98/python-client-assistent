# KlantAssistent – WerkZeker Nederland

## Wat doet de tool?

De **KlantAssistent** is een Python terminal applicatie die medewerkers van WerkZeker Nederland ondersteunt bij het inschatten van klantdossiers.

De tool:

* Vraagt gegevens van één of meerdere klanten (naam, leeftijd, besteding en klanttype)
* Verwerkt deze gegevens 
* Genereert per klant één advieslabel
* Geeft aan het einde een samenvatting van alle gegenereerde adviezen

De tool voert geen acties uit, kent geen rechten toe en neemt geen echte besluiten.

---

## Hoe gebruik je hem?

### Benodigdheden

* Python 3.x
* Een terminal of command prompt

### Applicatie starten

1. Open een terminal
2. Navigeer naar de map waarin het Python-bestand staat
3. Start de applicatie met:

```bash
python main.py
```

*(Gebruik eventueel `python3`)*

### Gebruik

1. De applicatie vraagt hoeveel klanten je wilt invoeren
2. Per klant vul je de volgende gegevens in:

   * Naam
   * Leeftijd (getal)
   * Bestedingsniveau per maand (getal)
   * Klanttype (`nieuw`, `bestaand` of `premium`)
3. Na elke invoer toont de applicatie direct een advieslabel
4. Na afloop verschijnt een samenvatting met:

   * Het totaal aantal ingevoerde klanten
   * Het aantal keer dat elk advieslabel voorkomt
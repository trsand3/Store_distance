
# Store_distance
Finner avstand til butikklokasjoner
=======
# Beregn avstand til mål-adresse fra Excel-liste

Dette prosjektet inneholder et Python-skript (`calculate_distances.py`) som leser en Excel-fil med stedsnavn (SITE NAME), geokoder hver rad til en full adresse, og beregner avstanden i kilometer til en forhåndsdefinert mål-adresse (Bedriftsveien 9, 0950 Oslo, Norway). Resultatet lagres i en ny Excel-fil med ekstra kolonner for full adresse og avstand.

## Funksjonalitet
- Leser inn en Excel-fil (`Store_wired_adress.xlsx`) med kolonnen `SITE NAME`.
- Geokoder hvert stedsnavn til en full adresse ved hjelp av Nominatim (OpenStreetMap).
- Beregner avstanden fra hver adresse til mål-adressen ved hjelp av geodesisk avstand (geopy).
- Sorterer resultatet etter korteste avstand.
- Skriver resultatet til en ny Excel-fil (`Store_wired_adress_with_distances.xlsx`).

## Forbedret geokoding
- Skriptet forsøker nå å rense stedsnavn automatisk for å øke sjansen for treff i geokoding (fjerner butikknummer og bindestrek, f.eks. "Kiwi 315 Kværnerbyen - 13183" → "Kiwi Kværnerbyen").
- Hvis renset navn ikke gir treff, prøves originalt navn.
- Dette gir langt bedre resultater for kolonnene `ADRESSE` og `AVSTAND (km)`.

## Avhengigheter
- Python 3.x
- pandas
- geopy
- openpyxl

Installer avhengigheter med:
```bash
pip install pandas geopy openpyxl
```

## Bruk
1. Legg inn dine stedsnavn i `Store_wired_adress.xlsx` under kolonnen `SITE NAME`.
2. Kjør skriptet:
   ```bash
   python calculate_distances.py
   ```
3. Resultatet lagres i `Store_wired_adress_with_distances.xlsx` med kolonnene:
   - `SITE NAME`
   - `ADRESSE` (full adresse)
   - `AVSTAND (km)` (avstand til mål-adresse)

## Tilpasning
- Endre mål-adressen ved å justere adressen i koden:
  ```python
  target = geolocator.geocode("Bedriftsveien 9, 0950 Oslo, Norway")
  ```
- Endre input/output-filsti i variablene `input_path` og `output_path`.

## Feilhåndtering
- Hvis en adresse ikke kan geokodes, vil avstanden settes til `None`.
- Skriptet stopper hvis mål-adressen ikke kan geokodes.

## Lisens
Dette prosjektet bruker åpen kildekode og er fritt til privat bruk.
>>>>>>> 62d5992 (Første commit: avstandskalkulator)

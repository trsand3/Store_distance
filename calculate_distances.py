import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Angi input- og output-filsti
input_path  = 'Store_wired_adress.xlsx'
output_path = 'Store_wired_adress_with_distances.xlsx'

# Les inn Excel-filen
df = pd.read_excel(input_path, engine='openpyxl')

# Sett opp geolocator (Nominatim)
geolocator = Nominatim(user_agent="geoapiSolver")

# Geokode mål-adressen Bedriftsveien 9, 0950 Oslo
target = geolocator.geocode("Bedriftsveien 9, 0950 Oslo, Norway")
if target is None:
    raise RuntimeError("Kunne ikke geokode Bedriftsveien 9, 0950 Oslo.")
target_coords = (target.latitude, target.longitude)

# Funksjon for å slå opp full adresse basert på SITE NAME
def geocode_site_to_address(site_name):
    try:
        # Prøv å fjerne butikknummer og bindestrek for bedre treff
        # Eksempel: "Kiwi 315 Kværnerbyen - 13183" -> "Kiwi Kværnerbyen"
        import re
        # Fjern tall og bindestrek på slutten
        cleaned = re.sub(r"[-–—]?\s*\d+$", "", site_name)
        # Fjern butikknummer i starten (f.eks. "Kiwi 315 ")
        cleaned = re.sub(r"Kiwi \d+ ", "Kiwi ", cleaned, flags=re.IGNORECASE)
        # Fjern eventuelle ekstra mellomrom
        cleaned = cleaned.strip()
        # Prøv først med renset navn
        loc = geolocator.geocode(cleaned + ", Norway", timeout=10)
        if loc:
            return loc.address
        # Hvis ikke treff, prøv originalt navn
        loc = geolocator.geocode(site_name + ", Norway", timeout=10)
        return loc.address if loc else None
    except Exception:
        return None

# Funksjon for å beregne avstand (km) til mål-adressen
def distance_to_target(address):
    if address is None:
        return None
    try:
        loc = geolocator.geocode(address, timeout=10)
        if not loc:
            return None
        coords = (loc.latitude, loc.longitude)
        return round(geodesic(coords, target_coords).kilometers, 2)
    except Exception:
        return None

# Legg til kolonnene ADRESSE og AVSTAND (km)
df['ADRESSE']       = df['SITE NAME'].apply(geocode_site_to_address)
df['AVSTAND (km)'] = df['ADRESSE'].apply(distance_to_target)

# Sorter på korteste avstand
df_sorted = df.sort_values(by='AVSTAND (km)', ascending=True).reset_index(drop=True)

# Lagre til ny Excel-fil
df_sorted.to_excel(output_path, index=False)

print(f"Ferdig! Fil lagret som: {output_path}")
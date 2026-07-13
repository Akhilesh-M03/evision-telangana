import pandas as pd
from pathlib import Path

csv_path = Path("data/raw/charging_stations/EV_Charging_Stations_April_2024.csv")
df = pd.read_csv(csv_path)

# Let's check duplicates by all columns except S.No.
cols_to_check = [c for c in df.columns if c != "S.No."]
dupes_exact = df.duplicated(subset=cols_to_check, keep=False)
print(f"Exact duplicates (excluding S.No.): {dupes_exact.sum()}")
print(df[dupes_exact].head(10))

# Let's check duplicates by name and address
dupes_name_addr = df.duplicated(subset=["Name of the EV Charging Station (Private / Public Charging Infra)", "Address"], keep=False)
print(f"\nDuplicates by name and address: {dupes_name_addr.sum()}")

# Let's check duplicates by name and coordinates
dupes_name_coords = df.duplicated(subset=["Name of the EV Charging Station (Private / Public Charging Infra)", "Latitude", "Longitude"], keep=False)
print(f"\nDuplicates by name and coordinates: {dupes_name_coords.sum()}")

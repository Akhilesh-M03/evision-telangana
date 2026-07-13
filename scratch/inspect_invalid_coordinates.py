import pandas as pd
from pathlib import Path

csv_path = Path("data/raw/charging_stations/EV_Charging_Stations_April_2024.csv")
df = pd.read_csv(csv_path)

invalid_rows = []
for idx, row in df.iterrows():
    lat = str(row["Latitude"]).strip()
    lon = str(row["Longitude"]).strip()
    
    # Try converting to float
    try:
        float(lat)
        lat_ok = True
    except ValueError:
        lat_ok = False
        
    try:
        float(lon)
        lon_ok = True
    except ValueError:
        lon_ok = False
        
    if not lat_ok or not lon_ok:
        invalid_rows.append({
            "S.No.": row["S.No."],
            "Name": row["Name of the EV Charging Station (Private / Public Charging Infra)"],
            "District": row["District"],
            "Latitude": row["Latitude"],
            "Longitude": row["Longitude"]
        })

print(f"Total invalid rows in raw: {len(invalid_rows)}")
print("Sample of invalid coordinate formats:")
for i, r in enumerate(invalid_rows[:30]):
    print(f"{i+1}. S.No. {r['S.No.']} | Name: {r['Name']} | Lat: {r['Latitude']} | Lon: {r['Longitude']}")

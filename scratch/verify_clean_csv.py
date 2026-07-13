import json
import pandas as pd
from pathlib import Path

csv_path = Path("data/interim/charging_stations/charging_stations_clean.csv")
geojson_path = Path("data/raw/geography/telangana_33_districts.geojson")

with open(geojson_path, "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

geojson_districts = {f["properties"]["dtname"] for f in geojson_data["features"]}

df = pd.read_csv(csv_path)

print("--- Clean CSV Verification ---")
print(f"Row count: {len(df)}")
print("Columns:", df.columns.tolist())

# Check for NaNs
print("Null counts:\n", df.isnull().sum())

# Check if all districts match geojson list
unique_csv_districts = set(df["district"].dropna().unique())
extra_districts = unique_csv_districts - geojson_districts
print(f"Districts in CSV not in GeoJSON: {extra_districts}")

# Check coordinates validity
lat_out_of_bounds = df[(df["latitude"] < 15.8360) | (df["latitude"] > 19.9168)]
lon_out_of_bounds = df[(df["longitude"] < 77.2358) | (df["longitude"] > 81.3226)]
print(f"Latitude out of bounds: {len(lat_out_of_bounds)}")
print(f"Longitude out of bounds: {len(lon_out_of_bounds)}")

# Check string columns for whitespaces
string_cols = ["station_name", "state", "district", "address", "owning_organisation"]
whitespace_issues = 0
for col in string_cols:
    trimmed = df[col].astype(str).str.strip()
    not_equal = df[df[col].astype(str) != trimmed]
    if len(not_equal) > 0:
        print(f"Column '{col}' has whitespace issues in {len(not_equal)} rows!")
        whitespace_issues += len(not_equal)

if whitespace_issues == 0:
    print("All string columns are correctly trimmed!")

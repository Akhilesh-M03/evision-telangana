import pandas as pd
raw_csv_path = "data/raw/charging_stations/EV_Charging_Stations_April_2024.csv"
raw_df = pd.read_csv(raw_csv_path)

print("Row 34 details:")
print(raw_df.iloc[34])

print("\nRow 61 details:")
print(raw_df.iloc[61])

with open("data/interim/charging_stations/charging_stations_clean.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Header:", lines[0].strip())
print("Row 31 (1-indexed):", lines[30].strip())
print("Row 57 (1-indexed):", lines[56].strip())
print("\nSubstrings containing 'nan' (case-insensitive):")
for idx, line in enumerate(lines):
    if "nan" in line.lower() and "nanakramguda" not in line.lower() and "hanumakonda" not in line.lower() and "mananthani" not in line.lower() and "spandan" not in line.lower():
        print(f"Line {idx+1}: {line.strip()}")

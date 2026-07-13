import re
import pandas as pd
from pathlib import Path
from typing import Optional, Any

def parse_coordinate(val: Any) -> Optional[float]:
    """Parse a coordinate string in various formats to decimal degrees."""
    if pd.isna(val):
        return None
        
    s = str(val).strip()
    if not s:
        return None
        
    # Clean trailing characters and spaces
    s = s.rstrip(",'\"")
    s = s.replace(" ", "")
    
    # Check for hemisphere suffix at the very end
    hemi = None
    if s and s[-1].upper() in ["N", "S", "E", "W"]:
        hemi = s[-1].upper()
        s = s[:-1].rstrip(",'\"")
        
    # Try simple float conversion first (handles standard decimals and those with hemisphere stripped)
    try:
        val_float = float(s)
        if hemi in ["S", "W"]:
            val_float = -val_float
        return val_float
    except ValueError:
        pass
        
    # Check for multiple dots format (e.g. DD.MMSS.S)
    if s.count(".") >= 2:
        parts = s.split(".")
        if len(parts) >= 3:
            try:
                deg = float(parts[0])
                mmss = parts[1]
                frac_sec = parts[2]
                if len(mmss) == 4 and mmss.isdigit():
                    min_val = float(mmss[:2])
                    sec_val = float(mmss[2:]) + float(f"0.{frac_sec}")
                    decimal = deg + (min_val / 60.0) + (sec_val / 3600.0)
                    if hemi in ["S", "W"]:
                        decimal = -decimal
                    return decimal
            except (ValueError, IndexError):
                pass

    # DMS / DDM parser using generalized pattern (degrees, non-digits, minutes, non-digits, optional seconds, optional hemisphere)
    pattern = r"^(\d+)\D+(\d+(?:\.\d+)?)(?:\D+(\d+(?:\.\d+)?))?\D*$"
    match = re.match(pattern, s)
    if match:
        try:
            deg = float(match.group(1))
            min_str = match.group(2)
            sec_str = match.group(3)
            
            if len(min_str) == 4 and min_str.isdigit():
                min_val = float(min_str[:2])
                sec_val = float(min_str[2:])
                if sec_str:
                    sec_val += float(f"0.{sec_str}")
            else:
                min_val = float(min_str)
                sec_val = float(sec_str) if sec_str else 0.0
                
            decimal = deg + (min_val / 60.0) + (sec_val / 3600.0)
            if hemi in ["S", "W"]:
                decimal = -decimal
            return decimal
        except ValueError:
            pass

    return None

# Test on the CSV file
csv_path = Path("data/raw/charging_stations/EV_Charging_Stations_April_2024.csv")
df = pd.read_csv(csv_path)

print("Parsed results:")
parsed_count = 0
unparsed = []
for idx, row in df.iterrows():
    lat_raw = row["Latitude"]
    lon_raw = row["Longitude"]
    
    lat_parsed = parse_coordinate(lat_raw)
    lon_parsed = parse_coordinate(lon_raw)
    
    # We want to identify if it was originally not parseable as simple float
    try:
        float(str(lat_raw).strip())
        float(str(lon_raw).strip())
        was_simple_float = True
    except ValueError:
        was_simple_float = False
        
    if not was_simple_float:
        if lat_parsed is not None and lon_parsed is not None:
            print(f"S.No. {row['S.No.']} | Raw: ({lat_raw}, {lon_raw}) -> Parsed: ({lat_parsed:.6f}, {lon_parsed:.6f})")
            parsed_count += 1
        else:
            # Check if it was completely empty in raw
            if pd.isna(lat_raw) and pd.isna(lon_raw):
                pass
            else:
                unparsed.append((row["S.No."], row["Name of the EV Charging Station (Private / Public Charging Infra)"], lat_raw, lon_raw, lat_parsed, lon_parsed))

print(f"\nSuccessfully parsed {parsed_count} previously unparseable coordinates.")
print(f"Remaining unparsed count: {len(unparsed)}")
for r in unparsed:
    print(r)

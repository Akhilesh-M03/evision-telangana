# EVision Telangana - Geography Preprocessing Report

This report outlines the results of **Epic 4: Geography Dataset Preprocessing** for the EVision Telangana charging infrastructure planning database.

## Processing Summary

- **Total Districts Processed:** 33
- **Total State Land Area:** 112,185.98 km²
- **Geographic CRS:** WGS 84 (EPSG:4326)
- **Projected CRS (for calculations):** WGS 84 / UTM Zone 44N (EPSG:32644)

## Quality & Validation Checks

| Check | Status | Action Taken |
| :--- | :--- | :--- |
| **GeoJSON Integrity** | Passed | Validated GeoJSON structure and parsed features. |
| **Geometry Correctness** | Corrected | Checked geometry validity; repaired 1 invalid polygon self-intersection using `make_valid()`. |
| **Spelling Standardization** | Standardized | Cleaned whitespace and mapped outdated/incorrect district names (`Jagitial` -> `Jagtial`, `Jangoan` -> `Jangaon`, `Jayashankar Bhupalapally` -> `Jayashankar Bhupalpally`). |
| **Coordinate Bounds Check** | Passed | Verified all coordinates fall within Telangana limits (Lat: 15°N–21°N, Lon: 77°E–82°E). |

## Standardized District Geography Metadata

| District Name | Area (km²) | Centroid Latitude | Centroid Longitude |
| :--- | :---: | :---: | :---: |
| Adilabad | 3999.98 | 19.519845 | 78.565890 |
| Bhadradri Kothagudem | 6901.59 | 17.690287 | 80.716714 |
| Hanumakonda | 1656.77 | 18.062270 | 79.532820 |
| Hyderabad | 191.62 | 17.395106 | 78.470166 |
| Jagtial | 2886.42 | 18.832247 | 78.877866 |
| Jangaon | 2396.60 | 17.726333 | 79.281834 |
| Jayashankar Bhupalpally | 2872.49 | 18.505979 | 79.924199 |
| Jogulamba Gadwal | 2577.85 | 16.071720 | 77.781035 |
| Kamareddy | 3752.29 | 18.324965 | 78.061623 |
| Karimnagar | 2003.94 | 18.380020 | 79.245464 |
| Khammam | 4675.03 | 17.205980 | 80.365155 |
| Kumuram Bheem Asifabad | 4535.90 | 19.357265 | 79.419678 |
| Mahabubabad | 3539.93 | 17.675077 | 79.996102 |
| Mahabubnagar | 2806.79 | 16.751462 | 78.013115 |
| Mancherial | 3855.61 | 18.991567 | 79.512376 |
| Medak | 2750.97 | 17.953225 | 78.265002 |
| Medchal Malkajgiri | 1076.22 | 17.544204 | 78.557704 |
| Mulugu | 4286.97 | 18.291511 | 80.337354 |
| Nagarkurnool | 6204.70 | 16.382248 | 78.595979 |
| Nalgonda | 7204.00 | 16.876389 | 79.192881 |
| Narayanpet | 2366.85 | 16.643141 | 77.580215 |
| Nirmal | 3719.19 | 19.113391 | 78.314660 |
| Nizamabad | 4216.81 | 18.701624 | 78.211231 |
| Peddapalli | 2193.58 | 18.620167 | 79.453681 |
| Rajanna Sircilla | 1809.39 | 18.414077 | 78.763438 |
| Ranga Reddy | 5002.07 | 17.130948 | 78.412553 |
| Sangareddy | 4460.56 | 17.785308 | 77.874265 |
| Siddipet | 3727.80 | 18.021595 | 78.856920 |
| Suryapet | 3592.81 | 17.080454 | 79.754637 |
| Vikarabad | 3712.20 | 17.246215 | 77.750714 |
| Wanaparthy | 2229.60 | 16.289550 | 78.042477 |
| Warangal | 1749.59 | 17.866192 | 79.751064 |
| Yadadri Bhuvanagiri | 3229.85 | 17.451169 | 78.978687 |

---
*Report generated automatically on behalf of EVision Telangana Preprocessing Pipeline.*

# EV Charging Stations Preprocessing Report

This report summarizes the data cleaning, schema validation, coordinate check, and spatial classification of charging stations for the EVision Telangana planning support system.

## 1. Executive Summary

- **Total Raw Records Loaded**: 551
- **Records Removed due to Missing/Invalid Coordinates**: 19
- **Records Removed due to Coordinates Outside Telangana Boundary**: 5
- **Duplicate Records Removed**: 13
- **Cleaned Records Retained**: 514

## 2. Spatial and Coordinate Checks

Coordinates were validated spatially against Telangana's 33 districts boundaries defined in `telangana_33_districts.geojson`.
- **Bounding Box of Telangana**:
  - Latitude: [15.918149, 19.741383]
  - Longitude: [77.501050, 80.826514]

### District Name Typos & Spatial Mismatches Resolved (287)

The following table lists samples of station district mismatches corrected by assigning standard district names from spatial polygons:

| S.No. | Station Name | District Mismatch |
|---|---|---|
| 2 | IOCL-Sri Ravi FS, Palvancha | 'Bhadradri' -> 'Bhadradri Kothagudem' |
| 3 | IOCL Orugallu FS | 'Hanamkonda' -> 'Hanumakonda' |
| 4 | IOCL Balaji FS Yellapur | 'Warangal' -> 'Siddipet' |
| 7 | IOCL Vishwambhara FS | 'Mahaboobnagar' -> 'Hanumakonda' |
| 12 | IOCL Sri Ramakrishna FS Manthani Peddapally | 'Karimnagar - Peddapalli' -> 'Peddapalli' |
| 13 | IOCL Janapriya FS Yellandu | 'Bhadradri Kothagudem' -> 'Mahabubabad' |
| 15 | IOCL Sri laxmi narasimha swamy Filling st Birkoor | 'Nizamabad' -> 'Kamareddy' |
| 17 | IOCL AP prison Department | 'Warangal' -> 'Hanumakonda' |
| 19 | IOCL Yadadri Filling station | 'Warangal' -> 'Hanumakonda' |
| 20 | Kona Vijay shankar filling station | 'Malkajgiri Medchal' -> 'Medchal Malkajgiri' |
| 21 | Srinidhi Service station Nizampet | 'Ranga Reddy' -> 'Medchal Malkajgiri' |
| 22 | Srinidhi Service station Nizampet | 'Ranga Reddy' -> 'Medchal Malkajgiri' |
| 23 | Kona Vijay shankar filling station, Bahadurpalle | 'Malkajgiri Medchal' -> 'Medchal Malkajgiri' |
| 29 | Synergy car case champapet | 'Ranga Reddy' -> 'Hyderabad' |
| 31 | Orange Auto Attapur | 'Ranga Reddy' -> 'Hyderabad' |
| 35 | IOCL Rajyalaxmi FP Mahaboobnagar | 'Mahaboobnagar' -> 'Mahabubnagar' |
| 36 | IOCl Durga Indhan Kando NH 9 | 'Sanga Reddy' -> 'Sangareddy' |
| 38 | IOCL Sri sangameshwara FS Narayankhed | 'Sanga Reddy' -> 'Sangareddy' |
| 40 | IOCL Sri Sai Raghava Sangareddy | 'Sanga Reddy' -> 'Sangareddy' |
| 41 | IOCL Laxmi Narasimha sadasivpet | 'Sanga Reddy' -> 'Sangareddy' |
| 42 | IOCL Express way FS Malkapur | 'Sanga Reddy' -> 'Sangareddy' |
| 43 | IOCL Sri sai FS Malkapur | 'Sanga Reddy' -> 'Sangareddy' |
| 45 | IOCL Sri Balaji FS Huzurnagar | 'Nalgonda' -> 'Suryapet' |
| 46 | IOCL 7 Hills FS Jedcharla | 'Mahaboobnagar' -> 'Mahabubnagar' |
| 49 | IOCL Sainath Filling station medak | 'Sanga Reddy' -> 'Sangareddy' |
| 54 | Sree venkateshwara Motors, Kamareddy | 'Kamareddy' -> 'Medak' |
| 56 | IOCL Adhoc AP Prison | 'Warangal' -> 'Hanumakonda' |
| 57 | IOCl Sai SS Elakaturty | 'Mahaboobnagar' -> 'Hanumakonda' |
| 58 | IOCL Sai leela FS Kundanpally | 'Karimnagar' -> 'Kamareddy' |
| 60 | IOCL Man air petro FS | 'Karimnagar' -> 'Rajanna Sircilla' |
| 61 | IOCL Shiva sai filling point Hanamkonda | 'Warangal' -> 'Hanumakonda' |
| 62 | IOCL NSLV Auto service | 'Khammam' -> 'Suryapet' |
| 64 | IOCL - UNI TRADERS, Itikyal Mandal | 'Jogulamba, Gadwal' -> 'Jogulamba Gadwal' |
| 65 | IOCL Raghu Vamsi Fs, Mahabubnagar | 'Mahabubna gar' -> 'Mahabubnagar' |
| 66 | TML Venkata ramana Motors, Kukatpally | 'Medchal' -> 'Medchal Malkajgiri' |
| 67 | TML Venkataramana Motors, Vikarabad | 'Vikarabad' -> 'Hyderabad' |
| 69 | Venkataramana Motors, Gachibowli | 'Hyderabad' -> 'Ranga Reddy' |
| 70 | IOCL - SRI SAI RAGHAVA, Sangareddy | 'Hyderabad' -> 'Sangareddy' |
| 71 | IOCL - Bhargavl Fs, Mahabubabad | 'Hyderabad' -> 'Mahabubabad' |
| 72 | IOCL-JalGanesh Fs | 'Hyderabad' -> 'Mulugu' |
| 73 | IOCL - Ganapathy Fs, Jaipur | 'Hyderabad' -> 'Mancherial' |
| 74 | IOCL - Police Petrol Pump | 'Hyderabad' -> 'Adilabad' |
| 76 | IOCL • Onkar Roadlines FP, Andagullapally, | 'Hyderabad' -> 'Peddapalli' |
| 77 | IOCL - Kalyani Fs, Oglapur | 'Hyderabad' -> 'Hanumakonda' |
| 78 | IOCL - Coco Malleboinapally, Mahabubnagar | 'Hyderabad' -> 'Mahabubnagar' |
| 79 | IOCL - Hitech Fp, Mahabubnagar | 'Hyderabad' -> 'Mahabubnagar' |
| 80 | IOCL - Raja Rajeshwara F/P, Gangadhara | 'Hyderabad' -> 'Karimnagar' |
| 81 | IOCL - Abhirama As | 'Hyderabad' -> 'Medchal Malkajgiri' |
| 82 | Raju gari Ruchulu Highway Restaurants, NH65 | 'Hyderabad' -> 'Suryapet' |
| 83 | 7 Food Court (People Combine Pvt Ltd) | 'Hyderabad' -> 'Suryapet' |
| ... | and 237 more mismatches | |


## 3. District-Wise Station Distribution

The cleaned station distribution across Telangana's 33 standardized districts:

| District | Cleaned Station Count |
|---|---|
| Ranga Reddy | 129 |
| Medchal Malkajgiri | 111 |
| Hyderabad | 101 |
| Nalgonda | 19 |
| Sangareddy | 18 |
| Suryapet | 14 |
| Hanumakonda | 13 |
| Mahabubnagar | 13 |
| Yadadri Bhuvanagiri | 11 |
| Nizamabad | 10 |
| Kamareddy | 8 |
| Karimnagar | 7 |
| Wanaparthy | 5 |
| Bhadradri Kothagudem | 5 |
| Khammam | 5 |
| Medak | 5 |
| Nagarkurnool | 4 |
| Siddipet | 4 |
| Mahabubabad | 4 |
| Narayanpet | 3 |
| Peddapalli | 3 |
| Warangal | 3 |
| Adilabad | 3 |
| Mancherial | 3 |
| Jogulamba Gadwal | 3 |
| Vikarabad | 3 |
| Rajanna Sircilla | 2 |
| Jangoan | 2 |
| Nirmal | 1 |
| Mulugu | 1 |
| Kumuram Bheem Asifabad | 1 |


## 4. Owner Distribution (Top 20)

Cleaned stations breakdown by owning organization or person:

| Owning Organisation / Person | Count |
|---|---|
| TATA Power Company Limited | 83 |
| Fortum Charge and Drive India Pvt Ltd | 83 |
| TGREDCO | 81 |
| BPCL | 72 |
| Joule Point pvt Ltd | 58 |
| Ather Energy Pvt Ltd | 27 |
| TATA POWER COMPANY PVT LD | 25 |
| HPCL | 20 |
| SUN Mobility Private Limited | 16 |
| M/s. Trinity Cleantech Private Limited | 7 |
| TGREDCO/REIL | 6 |
| Bharath Petroleum Corporation Limited | 3 |
| ETO Motors Private Limited | 2 |
| Hyderabad Metro | 2 |
| BPN Projects Pvt Ltd | 2 |
| TTL Electric Fuel Pvt Ld | 1 |
| Fresh Bus Private Limited | 1 |
| UPMEDIA Solutions | 1 |
| Samisthi Aranya Resort | 1 |
| Magenta EV Solutions Pvt Ltd | 1 |
| ... | and 22 more organizations |


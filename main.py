
import requests
import pandas as pd
import time

# NYC 311 API
url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

# Dataset columns
columns = [
    "unique_key",
    "created_date",
    "closed_date",
    "agency",
    "complaint_type",
    "descriptor",
    "borough",
    "status",
    "latitude",
    "longitude",
    "due_date",
    "city"
]

# Download settings
batch_size = 10000
target_records = 100000
offset = 0

all_records = []

print("Starting URBAN PULSE data extraction...")

while len(all_records) < target_records:

    params = {
        "$select": ",".join(columns),
        "$limit": batch_size,
        "$offset": offset,
        "$order": "created_date DESC, unique_key DESC"
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()

    records = response.json()

    if not records:
        print("No more records available.")
        break

    all_records.extend(records)

    offset += batch_size

    print(
        f"Downloaded: {len(all_records)} records"
    )

    time.sleep(1)

# Convert into DataFrame
df = pd.DataFrame(all_records)

# Remove duplicate IDs
df = df.drop_duplicates(subset="unique_key")

# Save dataset
df.to_csv("urban_pulse_raw.csv", index=False)

print("\nExtraction completed!")
print("Total records:", len(df))
print("Unique request IDs:", df["unique_key"].nunique())
print("Saved as urban_pulse_raw.csv")

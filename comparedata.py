
import pandas as pd

# 1. Load raw and cleaned datasets
raw = pd.read_csv("urban_pulse_raw.csv")
cleaned = pd.read_csv("urban_pulse_cleaned.csv")

# 2. Convert date columns back to datetime for verification
cleaned["created_date"] = pd.to_datetime(
    cleaned["created_date"], utc=True
)

cleaned["closed_date"] = pd.to_datetime(
    cleaned["closed_date"], utc=True
)

# 3. Row count
print("\n--- ROW COUNT ---")
print("Raw rows:", len(raw))
print("Cleaned rows:", len(cleaned))

# 4. Column count
print("\n--- COLUMN COUNT ---")
print("Raw columns:", len(raw.columns))
print("Cleaned columns:", len(cleaned.columns))

# 5. Duplicate IDs
print("\n--- DUPLICATE IDs ---")
print("Raw duplicates:", raw["unique_key"].duplicated().sum())
print("Cleaned duplicates:", cleaned["unique_key"].duplicated().sum())

# 6. Cleaning check
print("\n--- CLEANING CHECK ---")
print("Missing created_date:", cleaned["created_date"].isna().sum())
print("Missing resolution_hours:", cleaned["resolution_hours"].isna().sum())

# 7. New columns
print("\n--- NEW COLUMNS ---")
print(set(cleaned.columns) - set(raw.columns))

# 8. Final row count comparison
print("\n--- FINAL RESULT ---")
if len(raw) == len(cleaned):
    print("Same row count: Check duplicate removal and transformations.")
else:
    print("Row count changed: Check duplicates removed.")

# 9. Resolution validation
print("\n--- RESOLUTION VALIDATION ---")
print("Missing closed_date:", cleaned["closed_date"].isna().sum())
print("Missing resolution_hours:", cleaned["resolution_hours"].isna().sum())
print("Closed requests:", cleaned["is_closed"].sum())
print("Unclosed requests:", (~cleaned["is_closed"]).sum())
print("Negative resolution hours:",
      (cleaned["resolution_hours"] < 0).sum())

# 10. Investigate records with closed_date but missing resolution_hours
problem_records = cleaned[
    cleaned["closed_date"].notna()
    & cleaned["resolution_hours"].isna()
]

print("\n--- INVESTIGATE RECORDS ---")
print("Records:", len(problem_records))

print(problem_records[
    ["unique_key", "created_date",
     "closed_date", "resolution_hours"]
].head(20).to_string())

# 11. Check data types
print("\n--- DATA TYPES ---")
print(cleaned[
    ["created_date", "closed_date", "resolution_hours"]
].dtypes)

# 12. Check negative time differences in raw calculation
print("\n--- NEGATIVE TIME DIFFERENCE CHECK ---")

time_difference = (
    cleaned["closed_date"] - cleaned["created_date"]
).dt.total_seconds() / 3600

print("Negative time differences:",
      (time_difference < 0).sum())

print("\n--- VERIFICATION COMPLETED ---")

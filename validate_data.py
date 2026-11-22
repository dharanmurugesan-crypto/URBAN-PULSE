
import pandas as pd

# 1. Load cleaned dataset
df = pd.read_csv("urban_pulse_cleaned.csv")

print("=" * 50)
print("URBAN PULSE - DATA VALIDATION")
print("=" * 50)

# 2. Dataset dimensions
print("\n1. Dataset Dimensions")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Duplicate request IDs
print("\n2. Duplicate Request IDs")
print(df["unique_key"].duplicated().sum())

# 4. Missing values
print("\n3. Missing Values")
print(df.isnull().sum())

# 5. Invalid dates
print("\n4. Invalid Created Dates")
df["created_date"] = pd.to_datetime(
    df["created_date"], errors="coerce", utc=True
)
print(df["created_date"].isna().sum())

# 6. Negative resolution hours
print("\n5. Negative Resolution Hours")
print((df["resolution_hours"] < 0).sum())

# 7. Open and closed requests
print("\n6. Request Status")
print("Closed Requests:", df["is_closed"].sum())
print("Open Requests:", (~df["is_closed"]).sum())

# 8. Data types
print("\n7. Data Types")
print(df.dtypes)

# 9. Validation summary
print("\n8. Validation Summary")
print("Total Records:", len(df))
print("Duplicate IDs:", df["unique_key"].duplicated().sum())
print("Invalid Created Dates:", df["created_date"].isna().sum())

print("\nVALIDATION COMPLETED!")

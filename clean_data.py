
import pandas as pd

# 1. Load raw dataset
df = pd.read_csv("urban_pulse_raw.csv")

print("Original shape:", df.shape)

# 2. Remove duplicate request IDs
original_rows = len(df)

df = df.drop_duplicates(subset="unique_key")

duplicates_removed = original_rows - len(df)

print("Duplicates removed:", duplicates_removed)

# 3. Convert date columns
df["created_date"] = pd.to_datetime(
    df["created_date"], errors="coerce", utc=True
)

df["closed_date"] = pd.to_datetime(
    df["closed_date"], errors="coerce", utc=True
)

df["due_date"] = pd.to_datetime(
    df["due_date"], errors="coerce", utc=True
)

# 4. Clean text columns
text_columns = [
    "agency",
    "complaint_type",
    "borough",
    "status",
    "descriptor",
    "city"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# 5. Convert coordinates into numeric values
df["latitude"] = pd.to_numeric(
    df["latitude"], errors="coerce"
)

df["longitude"] = pd.to_numeric(
    df["longitude"], errors="coerce"
)

# 6. Calculate resolution hours
df["resolution_hours"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 3600

# Remove invalid negative resolution times
df.loc[df["resolution_hours"] < 0, "resolution_hours"] = pd.NA

# 7. Create closed status indicator
df["is_closed"] = df["closed_date"].notna()

# 8. Create date-based columns
df["created_year"] = df["created_date"].dt.year

df["created_month"] = df["created_date"].dt.month

df["created_weekday"] = df["created_date"].dt.day_name()

df["created_hour"] = df["created_date"].dt.hour

# 9. Display missing values
print("\nMissing values:")
print(df.isnull().sum())

# 10. Display cleaned dataset information
print("\nCleaned shape:", df.shape)

print("\nFirst 5 cleaned records:")
print(df.head())

# 11. Save cleaned dataset
df.to_csv("urban_pulse_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# 12. Create cleaning log
with open("cleaning_log.txt", "w") as file:
    file.write("URBAN PULSE - DATA CLEANING LOG\n")
    file.write("--------------------------------\n")
    file.write(f"Original rows: {original_rows}\n")
    file.write(f"Duplicates removed: {duplicates_removed}\n")
    file.write(f"Final rows: {df.shape[0]}\n")
    file.write(f"Final columns: {df.shape[1]}\n")
    file.write("Date columns converted.\n")
    file.write("Text columns trimmed.\n")
    file.write("Coordinates converted to numeric.\n")
    file.write("Resolution hours calculated.\n")
    file.write("Date-based columns created.\n")

print("Cleaning log saved successfully!")


import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# 1. Read cleaned CSV
df = pd.read_csv("urban_pulse_cleaned.csv")

# 2. Convert missing values to None for PostgreSQL
df = df.astype(object).where(pd.notna(df), None)

# 3. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="urban_pulse_db",
    user="postgres",
    password="Dharankumar8",
    port="5432"
)

cursor = conn.cursor()

# 4. Insert data
columns = list(df.columns)

insert_query = """
INSERT INTO service_requests ({})
VALUES %s
""".format(",".join(columns))

data = [tuple(row) for row in df.to_numpy()]

execute_values(
    cursor,
    insert_query,
    data,
    page_size=1000
)

# 5. Commit changes
conn.commit()

print("Data loaded successfully!")

# 6. Verify row count
cursor.execute("SELECT COUNT(*) FROM service_requests")
print("Total records in PostgreSQL:", cursor.fetchone()[0])

cursor.close()
conn.close()

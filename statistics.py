
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load cleaned dataset
df = pd.read_csv("urban_pulse_cleaned.csv")

# 2. Resolution hours
resolution = df["resolution_hours"].dropna()

print("=" * 50)
print("URBAN PULSE - DESCRIPTIVE STATISTICS")
print("=" * 50)

# 3. Basic statistics
print("\n1. Resolution Time Statistics")

print("Mean:", resolution.mean())
print("Median:", resolution.median())
print("Mode:", resolution.mode().tolist())
print("Minimum:", resolution.min())
print("Maximum:", resolution.max())
print("Range:", resolution.max() - resolution.min())

# 4. Quartiles and IQR
Q1 = resolution.quantile(0.25)
Q2 = resolution.quantile(0.50)
Q3 = resolution.quantile(0.75)

IQR = Q3 - Q1

print("\n2. Quartiles and IQR")
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("IQR:", IQR)

# 5. Variance and standard deviation
print("\n3. Variance and Standard Deviation")
print("Variance:", resolution.var())
print("Standard Deviation:", resolution.std())

# 6. Outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = resolution[
    (resolution < lower_bound) |
    (resolution > upper_bound)
]

print("\n4. IQR Outlier Analysis")
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outlier Count:", len(outliers))

# 7. Histogram
plt.figure(figsize=(10, 5))
plt.hist(resolution, bins=50)
plt.title("Distribution of Resolution Hours")
plt.xlabel("Resolution Hours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("resolution_histogram.png")
plt.show()

# 8. Boxplot
plt.figure(figsize=(10, 5))
plt.boxplot(resolution)
plt.title("Resolution Hours Boxplot")
plt.ylabel("Resolution Hours")
plt.tight_layout()
plt.savefig("resolution_boxplot.png")
plt.show()

print("\nStatistics completed!")

# ==============================
# Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("data/raw/fordgobike-tripdataFor201902.csv")
df  # Display dataset


# ==============================
# Check Missing Values
# ==============================
df_nulls = df.isnull().sum()  # Count nulls per column
ratio = df_nulls / df.shape[0]  # Calculate null ratio

# Create summary table for missing values
pd.DataFrame({"null": df_nulls, "Ratio": ratio}).T


# ==============================
# Descriptive Statistics
# ==============================
df.describe().T  # Statistical summary for numerical columns


# ==============================
# Drop Unnecessary Columns
# ==============================
df.drop(['start_time', 'end_time'], axis=1, inplace=True)


# ==============================
# Handle Missing Values
# ==============================

# Drop rows with missing station data (critical columns)
df.dropna(subset="start_station_name", inplace=True)
df.dropna(subset="start_station_id", inplace=True)
df.dropna(subset="end_station_id", inplace=True)
df.dropna(subset="end_station_name", inplace=True)

# Fill missing gender with most frequent value (mode)
df["member_gender"].fillna(df["member_gender"].mode()[0], inplace=True)

# Fill missing birth year with median value
df["member_birth_year"].fillna(df["member_birth_year"].median(), inplace=True)

df.head()


# ==============================
# Check Data Types & Unique Values
# ==============================
def check_datatype(df):
    datatypes = df.dtypes  # Column data types
    n_unique = df.nunique()  # Number of unique values

    return pd.DataFrame({
        "Data type": datatypes,
        "Num_unique": n_unique
    }).T

check_datatype(df)


# ==============================
# Convert Columns to Category
# ==============================
def handle_datatype(df, cols):
    df[cols] = df[cols].astype("category")

handle_datatype(df, [
    "start_station_id",
    "start_station_name",
    "end_station_id",
    "end_station_name",
    "user_type",
    "member_gender",
    "bike_share_for_all_trip",
    "bike_id"
])

check_datatype(df)


# ==============================
# Select Numerical Columns
# ==============================
num_cols = df.select_dtypes('number').columns
num_cols.value_counts()


# ==============================
# Check & Remove Duplicates
# ==============================
df.duplicated().sum()  # Count duplicates

df.drop_duplicates(inplace=True)

df.duplicated().sum()  # Confirm removal


# ==============================
# Visualize Outliers Using Boxplots
# ==============================
plt.figure(figsize=(14, 10))

for i, col in enumerate(num_cols):
    plt.subplot(3, 3, i+1)
    sns.boxplot(df[col], orient='h')  # Horizontal boxplot
    plt.title(col)

plt.tight_layout()
plt.show()


# ==============================
# Log Transformation (Reduce Skewness)
# ==============================
df['duration_sec'] = np.log1p(df['duration_sec'])


# ==============================
# Feature Engineering - Create Age
# ==============================
df['age'] = 2026 - df['member_birth_year']

# Keep realistic age range only
df = df[(df['age'] >= 15) & (df['age'] <= 80)]


# ==============================
# Remove Zero Coordinates
# ==============================
df = df[df['start_station_latitude'] != 0]

# IQR Outlier Removal (Using 5% and 95% Quantiles)
Q1 = df['start_station_latitude'].quantile(0.05)
Q3 = df['start_station_latitude'].quantile(0.95)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['start_station_latitude'] >= lower) & 
        (df['start_station_latitude'] <= upper)]


# Repeat Same Process for End Latitude
df = df[df['end_station_latitude'] != 0]

Q1 = df['end_station_latitude'].quantile(0.05)
Q3 = df['end_station_latitude'].quantile(0.95)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['end_station_latitude'] >= lower) & 
        (df['end_station_latitude'] <= upper)]


# Repeat for Start Longitude
df = df[df['start_station_longitude'] != 0]

Q1 = df['start_station_longitude'].quantile(0.05)
Q3 = df['start_station_longitude'].quantile(0.95)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['start_station_longitude'] >= lower) & 
        (df['start_station_longitude'] <= upper)]


# Repeat for End Longitude
df = df[df['end_station_longitude'] != 0]

Q1 = df['end_station_longitude'].quantile(0.05)
Q3 = df['end_station_longitude'].quantile(0.95)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['end_station_longitude'] >= lower) & 
        (df['end_station_longitude'] <= upper)]


# ==============================
# Visualize After Cleaning
# ==============================
plt.figure(figsize=(14, 10))

for i, col in enumerate(num_cols):
    plt.subplot(3, 3, i+1)
    sns.boxplot(df[col], orient='h')
    plt.title(col)

plt.tight_layout()
plt.show()


df.head()

import os
if not os.path.exists('data/processed'):
    os.makedirs('data/processed')

df.to_csv("data/processed/cleaned_fordgobike_data.csv", index=False)
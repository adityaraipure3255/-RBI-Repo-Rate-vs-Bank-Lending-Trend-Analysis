# RBI Repo Rate vs Bank Lending Trend Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load datasets
repo_path = "data/RBI_Monetary_Policy_Rates.xlsx"
walr_path = "data/RBI_WALR_Outstanding_Loans.xlsx"

repo_df = pd.read_excel(repo_path)
walr_df = pd.read_excel(walr_path)

print("Datasets loaded successfully!")
print("Repo Rate Data Shape:", repo_df.shape)
print("WALR Data Shape:", walr_df.shape)




# Clean Repo Rate Data

repo_raw = pd.read_excel(
    repo_path,
    header=None
)

repo_df = repo_raw.iloc[8:, 1:9].copy()

repo_df.columns = [
    "Effective Date",
    "Bank Rate",
    "Repo",
    "Reverse Repo",
    "SDF Rate",
    "MSF Rate",
    "CRR",
    "SLR"
]

repo_df["Effective Date"] = pd.to_datetime(
    repo_df["Effective Date"],
    errors="coerce"
)

repo_df["Repo"] = pd.to_numeric(
    repo_df["Repo"],
    errors="coerce"
)

repo_df = repo_df.dropna(
    subset=["Effective Date", "Repo"]
).reset_index(drop=True)

print("\nRepo Rate data cleaned successfully!")
print("Clean Repo Rate Shape:", repo_df.shape)


# Clean WALR Data

walr_df["Month"] = pd.to_datetime(
    walr_df["Month"],
    errors="coerce"
)

walr_columns = [
    "Public Sector Banks",
    "Private Sector Banks",
    "Foreign Banks",
    "All SCBs"
]

for col in walr_columns:
    walr_df[col] = pd.to_numeric(
        walr_df[col],
        errors="coerce"
    )

walr_df = walr_df.dropna(
    subset=["Month", "All SCBs"]
).reset_index(drop=True)

print("\nWALR data cleaned successfully!")
print("Clean WALR Shape:", walr_df.shape)


# Sort data by date

repo_df = repo_df.sort_values(
    "Effective Date"
).reset_index(drop=True)

walr_df = walr_df.sort_values(
    "Month"
).reset_index(drop=True)

print("\nData sorted successfully!")

print("Repo Rate First Date:",
      repo_df["Effective Date"].min().date())

print("WALR First Date:",
      walr_df["Month"].min().date())



# Convert Repo Rate Data to Quarterly Frequency

repo_quarterly = (
    repo_df
    .set_index("Effective Date")["Repo"]
    .resample("QE")
    .last()
    .reset_index()
)

print("\nRepo Rate converted to quarterly frequency!")
print("Quarterly Repo Rate Shape:", repo_quarterly.shape)

print(repo_quarterly.head(10))



# Create Quarter Column for WALR

walr_df["Quarter"] = (
    walr_df["Month"]
    .dt.to_period("Q")
    .dt.end_time
    .dt.normalize()
)

print("\nQuarter column created for WALR!")

print(
    walr_df[
        ["Month", "Quarter", "All SCBs"]
    ].head(10)
)




# Create Quarter Column for Repo Rate

repo_quarterly["Quarter"] = (
    repo_quarterly["Effective Date"]
    .dt.to_period("Q")
    .dt.end_time
    .dt.normalize()
)

print("\nQuarter column created for Repo Rate!")

print(
    repo_quarterly[
        ["Effective Date", "Quarter", "Repo"]
    ].head(10)
)




# Merge Repo Rate and WALR Data

merged_df = pd.merge(
    walr_df,
    repo_quarterly[["Quarter", "Repo"]],
    on="Quarter",
    how="inner"
)

merged_df = merged_df.sort_values(
    "Quarter"
).reset_index(drop=True)

print("\nDatasets merged successfully!")
print("Merged Data Shape:", merged_df.shape)

print(merged_df.head(10))




# Create Final Analysis Dataset

analysis_df = merged_df.drop(
    columns=["Month"]
).copy()

analysis_df = analysis_df[
    [
        "Quarter",
        "Repo",
        "Public Sector Banks",
        "Private Sector Banks",
        "Foreign Banks",
        "All SCBs"
    ]
]

print("\nFinal analysis dataset created!")
print("Analysis Data Shape:", analysis_df.shape)

print(analysis_df.head(10))




# Handle Missing Repo Rate Values

analysis_df["Repo"] = analysis_df["Repo"].ffill()

print("\nMissing Repo Rate values after forward fill:")
print(analysis_df["Repo"].isnull().sum())

print("\nFirst 10 Repo Rate values:")
print(analysis_df[["Quarter", "Repo"]].head(10))




# Remove Remaining Missing Repo Rate Value

analysis_df = analysis_df.dropna(
    subset=["Repo"]
).reset_index(drop=True)

print("\nFinal missing values check:")
print(analysis_df.isnull().sum())

print("\nFinal Analysis Data Shape:", analysis_df.shape)




# Calculate Quarterly Rate Changes

analysis_df["Repo_Change"] = analysis_df["Repo"].diff()

analysis_df["WALR_Change"] = analysis_df["All SCBs"].diff()

print("\nQuarterly rate changes calculated!")

print(
    analysis_df[
        [
            "Quarter",
            "Repo",
            "Repo_Change",
            "All SCBs",
            "WALR_Change"
        ]
    ].head(10)
)





# One-Quarter Lag Analysis

analysis_df["Repo_Change_Lag_1Q"] = (
    analysis_df["Repo_Change"].shift(1)
)

print("\nOne-quarter lag column created!")

print(
    analysis_df[
        [
            "Quarter",
            "Repo_Change",
            "Repo_Change_Lag_1Q",
            "WALR_Change"
        ]
    ].head(10)
)





# Calculate Correlations

correlation = analysis_df["Repo"].corr(
    analysis_df["All SCBs"]
)

change_correlation = analysis_df["Repo_Change"].corr(
    analysis_df["WALR_Change"]
)

lag_correlation = analysis_df["Repo_Change_Lag_1Q"].corr(
    analysis_df["WALR_Change"]
)

print("\nCorrelation Analysis")

print(
    "Repo Rate vs All SCBs WALR:",
    round(correlation, 3)
)

print(
    "Repo Rate Change vs WALR Change:",
    round(change_correlation, 3)
)

print(
    "Previous Quarter Repo Change vs Current WALR Change:",
    round(lag_correlation, 3)
)




# Maximum and Minimum Rate Analysis

repo_max = analysis_df.loc[
    analysis_df["Repo"].idxmax()
]

repo_min = analysis_df.loc[
    analysis_df["Repo"].idxmin()
]

walr_max = analysis_df.loc[
    analysis_df["All SCBs"].idxmax()
]

walr_min = analysis_df.loc[
    analysis_df["All SCBs"].idxmin()
]

print("\nRepo Rate:")
print(
    "Maximum:",
    repo_max["Repo"],
    "on",
    repo_max["Quarter"].date()
)

print(
    "Minimum:",
    repo_min["Repo"],
    "on",
    repo_min["Quarter"].date()
)

print("\nAll SCBs WALR:")
print(
    "Maximum:",
    walr_max["All SCBs"],
    "on",
    walr_max["Quarter"].date()
)

print(
    "Minimum:",
    walr_min["All SCBs"],
    "on",
    walr_min["Quarter"].date()
)





# Create Final Analysis Summary

summary = {
    "Repo Rate Maximum": analysis_df["Repo"].max(),
    "Repo Rate Minimum": analysis_df["Repo"].min(),
    "WALR Maximum": analysis_df["All SCBs"].max(),
    "WALR Minimum": analysis_df["All SCBs"].min(),
    "Repo-WALR Correlation": correlation,
    "Change Correlation": change_correlation,
    "Lagged Correlation": lag_correlation
}

summary_df = pd.DataFrame(
    summary.items(),
    columns=["Metric", "Value"]
)

print("\nFinal Analysis Summary:")
print(summary_df)






# Save Cleaned Analysis Dataset

output_path = "data/RBI_Repo_Rate_Analysis_Cleaned.csv"

analysis_df.to_csv(
    output_path,
    index=False
)

print("\nCleaned analysis dataset saved successfully!")
print("File:", output_path)







# Final Dataset Validation

print("\n========== FINAL VALIDATION ==========")

print("Final Dataset Shape:", analysis_df.shape)

print("\nColumn Names:")
print(analysis_df.columns.tolist())

print("\nMissing Values:")
print(analysis_df.isnull().sum())

print("\nDuplicate Rows:")
print(analysis_df.duplicated().sum())

print("\nFirst 5 Records:")
print(analysis_df.head())




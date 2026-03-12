# Creating Date data
import pandas as pd

data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "Sales": [200, 150, 300]
}

df = pd.DataFrame(data)
print(df)

# Convert to datetime
df["Date"] = pd.to_datetime(df["Date"])
print(df)

# Extrac Date components
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()
print(df)

# Set Date as index
# df = df.set_index("Date", inplace=True)
# print(df)

# # Filtering by month
# df_jan = df[df.index.month == 1]
# print(df_jan)

#Date Range Creation
# dates = pd.date_range(start="2026-01-01", periods=5, freq="D")
# print(dates)

# Exporting Data
df.to_csv("output.csv", index=False)
print("Data exported to output.csv")

df.to_excel("output.xlsx", index=False)
print("Data exported to output.xlsx")
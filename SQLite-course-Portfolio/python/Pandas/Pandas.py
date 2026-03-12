# import pandas as pd

# data = {
#     "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
#     "sales": [1200, 800, 1500, 600, 2000, 1800, 1600]
# }

# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# df = pd.read_csv("sales_data.csv")
# print(df)
# print(df.head(5))

# print(df.info())

# print(df.describe())
# print(df.head(5))
# print(df.tail(5))

# print(df.info())
# print(df.describe())

# import pandas as pd
# df = pd.read_csv("sales_data.csv")

# print(df.head(5))
# print(df.tail(5))

# print(df.info())
# print(df.describe())

# print(df["sales"].sum())
# print(df["sales"].mean())
# print(df["sales"].max())
# print(df["sales"].min())

# Filtering
# high_sales = df[df["sales"] > 1500]
# print(high_sales)

# low_sales = df[df["sales"] < 800]
# print(low_sales)

# Sorting
# sorted_sales = df.sort_values(by="sales", ascending=False)
# print(sorted_sales)

# sorted_sales = df.sort_values(by="sales", ascending=True)
# print(sorted_sales)

# Business questions (Best Sales Day)
# best_day = df.loc[df["sales"].idxmax()]
# print(best_day)

# Business questions (Worst Sales Day)
# worst_day = df.loc[df["sales"].idxmin()]
# print(worst_day)

# sales_above_average = df[df["sales"] > df["sales"].mean()]
# print(sales_above_average)

# Step 3 : Grouping Data
# Total sales By region
# sales_by_region = df.groupby("region")["sales"].sum()
# print(sales_by_region)

#Average sales by region
# average_sales = df.groupby("region")["sales"].mean()
# print(average_sales)

# Count Days per region
# days_per_region = df.groupby("region").count()
# print(days_per_region)

# Best region for sales
# best_region = df.groupby("region")["sales"].sum().idxmax()
# print(best_region)

# Worst region for sales
# worst_region = df.groupby("region")["sales"].sum().idxmin()
# print(worst_region)

# Sales trends over time
# sales_trends = df.groupby("day")["sales"].sum()
# print(sales_trends)

# Grouping Data (Real Analysis)

# df.groupby("region")
# Total Sales By Region
# sales_by_region = df.groupby("region")["sales"].sum()
# print(sales_by_region)

# Average Sales By Region
# avg_sales_region = df.groupby("region")["sales"].mean()
# print(avg_sales_region)

# Count days Per Region
# days_per_region = df.groupby("region")["sales"].count()
# print(days_per_region)

# Multiple Metrics At Once
# summary = df.groupby("region")["sales"].agg(["sum","mean","max","min"])
# print(summary)

# Mini Project

import pandas as pd
df = pd.read_csv("sales_data.csv")

# print(df.head())
# print(df.info())
# print(df.describe())

# Total Sales
total_sales = df["sales"].sum()
print("Total Sales:", total_sales)

# Average Sales
average_sales = df["sales"].mean()
print("Average Sales:", average_sales)

# Best sales day
best_day = df.loc[df["sales"].idxmax()]
print("Best Sales Day:", best_day)

# Worst sales day
worst_day = df.loc[df["sales"].idxmin()]
print("Worst Sales Day:", worst_day)
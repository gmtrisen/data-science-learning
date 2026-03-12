import pandas as pd

# # CSV = Comma Separated Values

# # Loading CSV file
df = pd.read_csv("pandas/data.csv")
print(df)

# Sorting DataFrames(sort-values)&(sort_index)

# sort by column(sort_values)
# sort by one column(ascending)
df_sorted = df.sort_values("Score")
print(df_sorted)

# sort by one column(descending)
df_sorted = df.sort_values("Score", ascending=False)
print(df_sorted)

# sort by multiple columns
df_sorted = df.sort_values(["Age", "Score"], ascending=[True, False])
print(df_sorted)

# Sort by index(sort_index)
df_sorted = df.sort_index()
print(df_sorted)

# Sort by index(descending)
df_sorted = df.sort_index(ascending=False)
print(df_sorted)

# # Important: inplace=True Permanently changes the original DataFrame    
# df.sort_values("Score", ascending=False, inplace=True)
# print(df)

# Reset Index after sorting
df = df.sort_values("Score", ascending=False)
df = df.reset_index(drop=True)
print(df)
# drop=True = prevents old index from being added as a column
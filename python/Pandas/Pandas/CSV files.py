import pandas as pd

# # CSV = Comma Separated Values

# # Loading CSV file
df = pd.read_csv("pandas/data.csv")
print(df)    

# print(df.head(2))

# Selecting Columns & Rows
# Selecting Columns
# print(df["Name"])
# print(df["Age"])
# print(df["Score"])

# Selecting multiple columns
# print(df[["Name", "Score"]])

# selecting Rows By position _ iloc
# print(df.iloc[0])
# print(df.iloc[1])
# print(df.iloc[2])

# Miltiple rows
# print(df.iloc[0:2])

# Specific rows and columns
# print(df.iloc[0, 1]) 
# print(df.iloc[1, 2])
# print(df.iloc[2, 0])

# Selecting rows by Label _ loc = uses index & column names
# print(df.loc[0])

# Conditional Selection
# print(df[df["Age"] > 20])
# print(df[df["Score"] > 80])
# # Multiple Conditions
# print(df[df["Age"] > 20 & df["Score"] > 80])

# print(df[["Name", "Age"]])
# print(df.iloc[1])
# print(df.loc[0:1, ["Name", "Score"]])
# print(df[df["Score"] >= 85]) 


# # Adding a New column
# df["Country"] = "Kenya","Tanzania","Uganda"
# print(df)

# Assign from a List
df["passed"] = [True,True,False]
print(df)

# Assign from a condition
df["passed"] = df["Score"] >= 80
print(df)

# Calculate from other columns
df["Bonus"] = df["Score"]+5
print(df)

# Modifying existing columns
df["Score"] = df["Score"]+10
print(df)

# Dropping columns
df = df.drop("Bonus",axis=1)
print(df)

# # Dropping multiple columns
# df = df.drop(["Bonus","passed"],axis=1)
# print(df)

# Dropping rows
df = df.drop(1, axis=0)
print(df)

# Inplace Drop =  True is Permanent
df.drop("Score", axis=1, inplace=True)  # permanently removes column

# Renaming columns
df.rename(columns={"Name":"Student Name", "Age":"Student Age", "Score":"Student Score"}, inplace=True)
print(df)


# MIni Practice
# Add a column passed with true or false based on score >= 80
df["passed"] = df["Score"] >= 80
print(df)

# # Calculate bonus points (10% of score)
# df["bonus"] = df["Score"] * 0.10
# print(df)

# # Drop the bonus column
# df = df.drop("bonus", axis=1)
# print(df)

# # Rename columns
# df.rename(columns={"Name":"Student Name", "Age":"Student Age", "Score":"Student Score"}, inplace=True)
# print(df)

df.rename(columns={"Score":"Marks"}, inplace=True)
print(df)
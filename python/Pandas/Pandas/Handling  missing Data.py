# import pandas as pd
# df = pd.read_csv("pandas/data.csv")
# print(df)    

# # Handling missing data
# # What is NaN (Not a Number)

# # detecting missing data
# print(df.isnull())
# # Checking for missing data
# print(df.notnull())
# # Counting missing values
# print(df.isnull().sum())

# Mini Practice
import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [20, np.nan, 19, 21],
    "Score": [85, 90, np.nan, 88]
}

# df = pd.DataFrame(data)
# print(df)

# # Drop Missing Values
# df_drop = df.dropna()
# print(df_drop)

# # Drop Columns with missing values
# df_drop_col = df.dropna(axis=1)
# print(df_drop_col)

# # Fill missing values
# df_fill = df.fillna(0)
# print(df_fill)

# # Fill with column Mean
# df["Age"].fillna(df["Age"].mean(), inplace=True)
# df["Score"].fillna(df["Score"].mean(), inplace=True)
# print(df)

# Practice example
df= pd.DataFrame(data)
df= df.isnull().sum()
print(df)

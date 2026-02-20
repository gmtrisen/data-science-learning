import pandas as pd

# Pandas Series(1D)  - A series = labelled 1D array
ages = pd.Series([18,22,30,40])
print(ages)

ages = pd.Series([18,22,30] , index=["A","B","C"])
print(ages)

# Pandas DataFrames(2) - A DataFrame = table(rows+columns)

data = {
    "name": ["Alice","Bob","Charlie"],
    "age":[20,25,30],
    "score":[85,90,88]
}
df = pd.DataFrame(data)
print(df)

# Numpy Inside Pandas(Bridge Concept)
df["score"].mean()
print(df["score"].mean())

# Inspecting Data
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())



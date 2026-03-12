import pandas as pd

# Loading Data
# df = pd.read_csv("data.csv")
# print(df)

# Creating DataFrame Manually (for Practice)
data = {
    "name": ["Alice","Bob","Charlie","Diana"],
    "age":[20,25,30,28],
    "score":[85,90,88,92]
}

df = pd.DataFrame(data)
print(df)
# selecting column
print(df["name"])
print(df["age"])
print(df["score"])

# # Selecting Row
# print(df.loc[0])
# print(df.loc[1])
# print(df.loc[2])
# print(df.loc[3])  



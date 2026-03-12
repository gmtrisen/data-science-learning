import pandas as pd

# Creating first Dataframe
data = {
    "name":["ALice","Bob","Charlie"],
    "age":[20,22,19],
    "score":[85,90,78]
}

df = pd.DataFrame(data)

print(df)
# Understanding the output 
# Left numbers are called index
# Top names are called columns
# Bottom values are called data
# Each row is called a record
# Each column is called a feature

# df.head()      # first 5 rows
# df.tail()      # last 5 rows
# df.shape       # (rows, columns)
# df.columns     # column names
# df.info()      # data types & nulls

import pandas as pd

data ={
    "Country":["Kenya","Uganda","Tanzania"],
    "Population_m":[54,48,65]
}
df= pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df.info())
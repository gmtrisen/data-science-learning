# Stacking DataFrames - stack() & unstack()
# Stack - wide to long
# Unstack - long to wide
import pandas as pd

# Vertical Concatenation (Stacking rows(one under another))
df1 = pd.DataFrame({
    "Name": ["Alice","Bob"],
    "Age": [20,22]
})

df2 = pd.DataFrame({
    "Name":["Charlie","David"],
    "Age":[19,21]
})

combined = pd.concat([df1,df2])
print(combined)

combined = pd.concat([df1, df2], ignore_index=True)
print(combined)

# Horizontal concatention
df3 = pd.DataFrame({
    "Score" : [85,90]
})

result = pd.concat([df1,df3], axis=1)
print(result)

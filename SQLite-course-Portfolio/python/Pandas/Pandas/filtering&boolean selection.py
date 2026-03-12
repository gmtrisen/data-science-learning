import pandas as pd

df = pd.read_csv("pandas/data.csv")
print(df)    

# Filtering rows with conditions
# filtering with one condition
df=df[df["Age"] > 20]
print(df)
df=df[df["Score"] > 80]
print(df)
df=df[(df["Age"] > 19) & (df["Score"] >= 85)]
print(df)

# Or Condition(|)
df = df[(df["Age"] > 20) | (df["Score"] < 80)]
print(df)

# Not condition(~)
df = df[~(df["Age"] > 20)]
print(df)

# Eaxmple
df = pd.read_csv("pandas/data.csv")
print("Original DataFrame:")
print(df)

# Age greater than 20
age_gt_20 = df[df["Age"] >20]
print("Age greater than 20:")
print(age_gt_20)

# Score less than 80
low_scores = df[df["Score"] <80]
print("Score less than 80:")
print(low_scores)

# Or condition
or_filter = df[(df["Age"] >20) | (df["Score"] < 80)]
print("\nAge < 20 Or Score < 80:")
print(or_filter)
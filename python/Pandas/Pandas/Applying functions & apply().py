# Applying functions & apply() & lambda functions

# why apply() exists - write logic that pandas can't do directly

import pandas as pd
df = pd.read_csv("pandas/data.csv")
print(df)


def grade(score):
   if score >= 85:
    return "A"
   elif score >= 70:
    return "B"
   else:
    return "C"

df["Grade"] = df["Score"].apply(grade)
print(df)           
   
# Same thing with lambda function
df["Grade"] = df["Score"].apply(
    lambda x: "A" if x >=85
    else "B" 
    if x >=70
    else "C"
)
print(df)


# Complex logic - def 
# Short logic - lambda

# Apply to multiple columns
# Pass/fail using age& score
df["Status"] = df.apply(
    lambda row : "Pass" if row["Score"] >= 80 and row["Age"] >=20
    else "Fail",
    axis=1
)
print(df)

# # Transform Numbers
# # Increase score by 10%
# df["Adjusted_Score"] = df["Score"].apply(lambda x: x * 1.1)
# print(df)

# # Round to nearest integer
# df["Adjusted_Score"] = df["Adjusted_Score"].round(0)
# print(df)

# Apply with missing values
df["Score"] = df["Score"].fillna(0)
df["Grade"] = df["Score"].apply(
    lambda x: "Missing" if x==0 else "A"
    if x >=85
    else "B"
    if x >=70
    else "C"
)
print(df)

# Mini practice
# Create column "Level"
df["Level"] = df["Age"].apply(lambda x: "Adult" if x >= 18 
else "Teen" if x <20
else "Minor")
print(df)

# apply - custom logic engine
# lambda - quick inline function
# axis=1 - apply row-wise
# axis=0 - apply column-wise

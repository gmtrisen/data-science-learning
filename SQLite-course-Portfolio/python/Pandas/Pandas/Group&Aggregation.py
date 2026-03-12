# Grouping and Aggregation - groupby()
import pandas as pd

# data = {
#     "Name" : ["Alice", "Bob", "Charlie", "Diana", "Evan"],
#     "Department": ["IT","IT","HR","HR","IT"],
#     "Salary" : [50000,60000,45000,48000,70000]
# }
# df = pd.DataFrame(data)
# print(df)

# Basic Grouping
# Average salary by department
# f = df.groupby("Department")["Salary"].mean()
# print(f)

# # Multiple aggregations
# f = df.groupby("Department")["Salary"].agg(["mean","sum","count"])
# print(f)

# Group by Multiple columns
data = {
    "Department": ["IT","IT","HR","HR","IT"],
    "Gender" : ["M","F","F","M","M"],
    "Salary" : [50000,60000,45000,48000,70000]
}

df= pd.DataFrame(data)
print(df)

# Group by two columns
f = df.groupby(["Department","Gender"])["Salary"].mean()
print(f)

# # Reset index
# result = df.groupby("Department")["Salary"].mean().reset_index()
# print(result)

f = df.groupby("Department", as_index=False)["Salary"].mean()
print(f)

# 6️⃣ Real-World Thinking

# Groupby answers questions like:

# Average sales per region

# Total revenue per month

# Number of students per class

# Mean salary per department

# Get total salary per department
f = df.groupby("Department", as_index=False)["Salary"].sum()
print(f)

# Get count of employees per department
f = df.groupby("Department", as_index=False)["Salary"].count()
print(f)

f = df.groupby("Department")["Salary"].count()
print(f)
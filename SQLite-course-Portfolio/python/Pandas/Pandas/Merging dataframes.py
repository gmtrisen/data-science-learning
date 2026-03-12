# Merging DataFrames - pd.merge()
import pandas as pd

# Table1 - students info
# Table2 - students scores

# We combine them using merge()

students = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"]
})

scores = pd.DataFrame({
    "ID":[1,2,4],
    "Score":[85,90,75]
})

print(students)
print(scores)

# step 2 : Basic Merge
merged = pd.merge(students,scores, on="ID")
print(merged)

# step 3 : Inner Merge (Default) inner → when you only want matching clean data
# Only rows with matching IDs in BOTH tables 
merged = pd.merge(students,scores, on="ID", how="inner")
print(merged)

# step 4 : Left Merge  left → when one table is your main dataset
# All rows from left table + matching from right
merged = pd.merge(students,scores, on="ID", how="left")
print(merged)

# step 5 : Right Merge
# All rows from right table + matching from left
merged = pd.merge(students,scores, on="ID", how="right")
print(merged)

# # step 6 : Outer Merge
# # All rows from BOTH tables
merged = pd.merge(students,scores, on="ID", how="outer")
print(merged)

# 6️⃣ Real-World Thinking

# Merge is used when you have:

# Student info in one table

# Score info in another table

# You need to combine them based on a common column (like ID)

# Think of it like joining two Excel sheets on a common column

# Mini Practice
teachers = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"]
})

scores = pd.DataFrame({
    "ID":[1,2,4],
    "Score":[85,90,75]
})

print(teachers)
print(scores)

merged = pd.merge(teachers,scores, on="ID", how="inner")
print(merged)
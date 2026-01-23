import numpy as np

# arr = np.array([10,20,30,40,50])
# print(arr[[0,2,4]])

# # Reordering an repeating
# print(arr[[4,0,0,2]])

# Fancy indexing with 2D array
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
# print(arr[[0,2]])
# print(arr[[0,1,2],[2,1,0]])

# Combine fancy indexing with boolean masking
# arr = np.array([10,20,30,40,50])
# mask = arr > 25
# print(arr[mask])

# Real life Example
scores = np.array([45,67,89,34,90])
top_students = scores[[1,2,4]]
print(top_students)
# 
import numpy as np

# arr =np.array([10,20,30,40])
# mask = arr > 25
# print(mask)
# filtering using boolean mask
# print(arr[mask])

# Direct filtering(shortcut)
# print(arr[arr > 25])

# Boolean masking with 2D array
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# mask = arr > 25
# print(mask)
# print(arr[mask])

# Multiple conditions(& and |)
# And condition
# mask = arr[(arr>20) & (arr<50)]

# print(mask)

# grades = np.array([45,62,78,30,90])

# passed = grades[grades >= 50]
# failed = grades[grades < 50]

# print("Passed:",passed)
# print("Failed:",failed)

# np.where()
# Syntax: np.where(condition, value_if_true, value_if_false)
# simple replacement
# arr = np.array([10,25,40])

# print(np.where(arr > 20 , arr , 0))

# categorizing data
# scores = np.array([45,60,82,30])

# result = np.where(scores >= 50, "Pass", "Fail")
# print(result)

# Boolean Masking with 2D arrays(structured)
# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# # print(arr[arr > 25])
# arr[arr < 30] = -1
# print(arr)

arr = np.array([
    [10,20,30],
    [40,50,60]
])
arr[arr<30] = -1
print(arr)
# Combining Boolean Masking + Axis(practical)
scores = np.array([
    [60,70,80],
    [45,55,65],
    [90,85,95]
])

avg_scores = scores.mean(axis=1)
scores[avg_scores>= 60]
print(scores)


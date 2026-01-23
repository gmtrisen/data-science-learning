import numpy as np
# scalar operations
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# print(a + 10)
# print(a - 10)
# print(a * 10)
# print(a / 10)

# elementwise operations
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# 2D Array operations
# arr = np.array([
#     [2,4,6],
#     [8,10,12]
# ])
# print(arr*2)
# print(arr+10)
# print(arr-2)
# print(arr/2)

# Broadcasting (the powerful part)
# 1D+2D
# arr = np.array([
#     [2,4,6],
#     [8,10,12]
# ])

# b = np.array([1,2,3])

# print(arr + b)

# Axis based math
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
# print(arr.sum())

# Statistical operations
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(arr.mean())
# print(arr.max())
# print(arr.min())
# print(arr.std())
# print(arr.var())

# comparison operations
# arr = np.array([10,20,30,40])
# print(arr > 25)
# print(arr == 20)

# multiple operations together
# arr = np.array([2, 4, 6])

# print((arr * 2) + 1)

# arr = np.array([10,25,40])
# print(np.where(arr > 20, arr, 0))

# real life example
# marks = np.array([48,55,67,72])

# bonus_marks = marks + 5
# print(bonus_marks)

# real life example2
marks = np.array([48,55,67,72])

bonus_marks = np.where(marks > 50, marks + 5, marks)
print(bonus_marks)
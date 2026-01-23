import numpy as np

# ddtype = type of data stored in array

arr = np.array([1,2,3,4])
print(arr.dtype)

# Setting dtype manually
arr = np.array([1,2,3,], dtype=float)
print(arr.dtype)
print(arr)

# Changing dtype(Type casting)
arr = np.array([1.7,2.3,3.9])
print(arr.astype(int))



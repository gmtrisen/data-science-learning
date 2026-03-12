import numpy as np

arr = np.array([40,10,30,20])
print(np.sort(arr))

# argsort() Returns the indices that would sort the array
arr = np.array([40,10,30,20])
print(np.argsort(arr))

# Searching in arrays 
# where() Returns the indices of elements in an input array where the given condition is satisfied
arr = np.array([10,20,30,40,])
print(np.where(arr > 25))

# searchsorted() Returns the indices where elements should be inserted to maintain the sorted order
arr = np.array([10,20,30,40,])
print(np.searchsorted(arr, 25))

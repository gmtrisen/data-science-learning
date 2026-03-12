import numpy as np

# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(2,3))
# print(arr.reshape(3,-1))

# Reshapinh 2D array
# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(arr.reshape(3,2))
# print(arr.reshape(3,-1))

# Flatten() vs ravel()
# arr = np.array([1,2,3,4,5,6])
# print(arr.flatten())
# print(arr.ravel())

# flatten() creates a new array
# ravel() returns a view
# flatten

# Rehssaping arrays
# arr = np.array([10,20,30])
# print(arr.reshape(3,1))
# print(arr[:, np.newaxis])
# print(arr.resize(3,1))

# ages = np.array([18,22,30,40])
# ages = ages.reshape(-1,1)
# print(ages)

# Column Vector
# arr = np.array([10,20,30])
# arr = arr.reshape(-1,1)
# print(arr)

# Row Vector
# arr = np.array([10,20,30])
# arr = arr.reshape(1,-1)
# print(arr)

# arr = np.array([1,2,3,4])
# # Make it a column vector
# arr = arr.reshape(-1,1)
# print(arr)

# # Make it a row vector
# arr = np.array([1,2,3,4])
# arr = arr.reshape(1,-1)
# print(arr)

# # Flatten it back to 1D array
# arr = np.array([1,2,3,4])
# arr = arr.flatten()
# arr = arr.ravel()
# print(arr)

# Stacking  = combining multiple arrays into one

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.stack((a,b)))

# # Vertical stacking
# print(np.vstack((a,b)))

# # Horizontal stacking
# print(np.hstack((a,b)))

# Stacking 2D arrays
# a = np.array([
#     [1,2],
#     [3,4]
# ])
# b = np.array([
#     [5,6],
#     [7,8]
# ])
# # print(np.vstack((a,b)))

# # print(np.hstack((a,b)))

# # Concanate()  more control

# print(np.concatenate((a,b), axis=0))
# print(np.concatenate((a,b), axis=1))

# Splitting arrays  1D array
arr = np.array([10,20,30,40,50,60])
print(np.split(arr, 3))


# Splitting 2D array
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(np.hsplit(arr, 2))






import numpy as np

# a=np.array([10,20,30,40,50])
# print(a[1:4])
# print(a[:3])
# print(a[2:])

arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])
print(arr[0:2])
print(arr[:,1:3])

print(arr[1:3,2:4])




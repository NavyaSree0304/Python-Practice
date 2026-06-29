import numpy as np

oneD = np.array([1, 2, 3, 4])

twoD = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

threeD = np.zeros((3, 3))

fourD = np.ones((4, 2))

print(oneD)
print(twoD)
print(threeD)
print(fourD)

print(oneD.shape)

reshape_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(3, 4)

print(reshape_arr)

print(oneD[0])
print(oneD[-1])
print(twoD[0])
print(twoD[:, 1])

marks = np.array([78, 92, 65, 88, 95, 73])

print(marks.max())
print(marks.min())
print(marks.mean())

marks.sort()

print(marks)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[1, 1])
print(matrix[0])
print(matrix[:, -1])
print(matrix.shape)

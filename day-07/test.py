import numpy as np

# arr = np.array([1, 4, 5])

# print(arr)
# print("Type of the array: ", type(arr))
# print("Shape of the array: ", arr.shape)

# print(arr[0],arr[1],arr[2])

# arr[1] = 10

# print(arr)


# arr2D = np.array([
#     [2, 5, 6],
#     [1, 5, 3]
# ])


# print(arr2D)
# print("Type of the array: ", type(arr2D))
# print("Shape of the array: ", arr2D.shape)

# print(arr2D[0], type(arr2D[0]))
# print(arr2D[1], type(arr2D[1]))


# print(arr2D[0, 0], arr2D[0, 1], arr2D[0, 2])
# print(arr2D[1, 0], arr2D[1, 1], arr2D[1, 2])


# zeros = np.zeros([3, 4])
# print(zeros, zeros.shape)

# ones = np.ones([4, 5])
# print(ones, ones.shape)

# consts = np.full([3,7],5)
# print(consts, consts.shape)

# random = np.random.random([4,5])
# print(random,random.shape)


# consts = consts = np.full([3, 3], 1)

# for i in range(len(consts[0])):
#     consts[i][i] = 0

# print(consts)


temp = np.array([
    [5, 4, 3, 1],
    [7, 3, 9, 3],
    [6, 4, 2, 4]
])

# print(temp)


# subArray = temp[:2,1:3]
# print(subArray)

# subArray = temp[1:,2:]
# print(subArray)

# subArray = temp[2,:]
# print(subArray)

# subArray = temp[:,2]
# print(subArray)

# subArray = temp[0:2,:]
# print(subArray)


# print(temp)
# print(temp > 2)
# print(temp[temp > 2])


# x = np.array([3, 4])
# print(x)
# print(x.dtype)


# y = np.array([3,4,5],dtype=np.float64)
# print(y)
# print(y.dtype)

# x = np .array([
#     [3, 4],
#     [7, 6]
# ], dtype=np.float64)

# y = np .array([
#     [1, 2],
#     [3, 2]
# ], dtype=np.float64)

# print("Normal sum:\n", x+y)
# print("Numpy sum:\n", np.add(x, y))

# print(np.subtract(x, y))
# print(np.multiply(x, y))
# print(np.divide(x, y))
# print(np.sqrt(x))


# x = np .array([
#     [3, 4],
#     [7, 6]
# ], dtype=np.float64)

y = np .array([
    [1, 2],
    [3, 2]
], dtype=np.float64)

v = np.array([9, 10])
w = np.array([5, 6])

# inner product

# print(v.dot(w))
# print(np.dot(v, w))

# print(x.dot(y))
# print(np.dot(x, y))

# print(x.dot(y))


x = np .array([
    [1, 2, 3],
    [4, 3, 1],
    [5, 8, 3]
], dtype=np.float64)

# print(x)
# print(x.T)


# print(np.sum(x))
# print(np.sum(x,axis=0))
# print(np.sum(x,axis=1))

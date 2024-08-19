import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)

newarr2d = arr.reshape(4, 3)
print(newarr2d)

newarr3d = arr.reshape(2, 3, 2)
print(newarr3d)

newarrUnknown = arr.reshape(2, 2, -1)
print(newarrUnknown)

arrMulti = np.array([[1, 2, 3], [4, 5, 6]])
print(arrMulti)
newarrFlat = arrMulti.reshape(-1)
print(newarrFlat)

tmp = np.array([[[1, 2, 3], [4, 5, 6]]])
print(tmp.reshape(1, -1))  # 二维，行向量
print(tmp.reshape(-1, 1))  # 二维，列向量

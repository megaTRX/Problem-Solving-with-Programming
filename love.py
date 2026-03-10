import numpy as np

# # 리스트를 생성하고 배열로 변환하기
# list1 = [1, 2, 3, 4]
# a = np.array(list1)
# print('a.shape: ', a.shape)
# print('a[0]: ', a[0])
#
# # 2차원 배열 생성하기
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print('b.shape: ', b.shape)
# print('b[0,0]: ', b[0,0])
# print('b[0]: ', b[0])

# a = np.zeros(2)
# print('a\n', a)
# b = np.zeros((2, 2))
# print('b\n', b)
# c = np.ones((2, 3))
# print('c\n', c)
# d = np.full((2, 3), 5)
# print('d\n', d)
# e = np.eye(3)
# print('e\n', e)

# # 실수형 배열 생성하기
# a = np.array([1, 2], dtype=np.float64)
# print(a.dtype)
#
# # 정수형 배열로 변환하기
# a_i8 = a.astype(np.int8)
# print(a_i8.dtype)

# arr = np.array([[0, 1, 2], [3, 4, 5]])
#
# print('type(arr): ', type(arr))
# print('arr.ndim:', arr.ndim)
# print('arr.dtype:', arr.dtype)
# print('arr.itemsize:', arr.itemsize)
# print('arr.size:', arr.size)
# print('arr.nbytes:', arr.nbytes)
# print('arr.T:\n', arr.T)
# print('arr.shape:', arr.shape)

# a = np.arange(8)
# print('a\n', a)
#
# # 다차원 배열로 변경하기
# a.shape = (2, 4)
# print('shpae\n', a)
#
# # 1차원 배열로 변경하기
# print('flatten\n', a.flatten())
#
# # resize 함수로 모양 변경하기
# a.resize((4, 2))
# print('resize\n', a)

# a = np.array([[0,1,2],[3,4,5]])
# print('a\n', a)
#
# b = a.transpose()
# print('b\n', b)
# c = a.T
# print('c\n', c)

# a = np.array(range(10)).reshape((2, 5))
# b = a.transpose()
# print('a\n', a)
# print('b\n', b)

# list1 = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
#
# a = np.array(list1)
# print(a[1:3, :3])
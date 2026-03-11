import numpy as np

a = np.arange(6) # 0부터 5까징의 정수로 넘파이 배열을 만들어 a에 할당합니다.
b = a # a의 값을 b에 저장합니다.
print(a)
print(b is a)

b[0] = 10 # 복사본인 배열 b에 값을 추가해도 원본 배열 a의 요소도 함께 변경됩니다.
print(a)

a = np.arange(6)
c = a.copy() # copy() 함수를 사용하여 복사하면 복사본인 배열 c의 값을 수정해도 원본 a에 영향이 없습니다.

c[0] = 20
print('A: ', a)
print('C: ', c)

a = np.array([3, 2, 5, 1, 4])

print('원본\n', a)
print('정렬 후\n', np.sort(a))

print('원본\n', a)
print('정렬한 인덱스\n', np.argsort(a))

a.sort()
print('원본\n', a)
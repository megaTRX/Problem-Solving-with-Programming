import numpy as np

mask = np.array([0, 1, 1, 0], dtype=bool)
print(mask)

data = np.random.randn(4,2)
print('\ndata 출력\n', data) # 랜덤 데이터 배열 data

print('\n마스킹된 데이터 출력\n', data[mask])
print('\n마스킹 역전된 데이터 출력\n', data[~mask])


posit = data[data > 0]
print('양수 데이터 출력', '\n', posit)

# 다중 조건
over1 = data[1][data[1] > 0]
print('두 번째 행의 양수 데이터 출력', '\n', over1)
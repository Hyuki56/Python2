import numpy as np
# 1차원 넘파이 배열 인덱싱
x = np.array([1,2,3,4,5])
print(x[0])
print(x[1])
print(x[-1])
print(x[-2], '\n')

# 다차원 넘파이 배열 인덱싱 : 각 차원의 인덱스를 ','로 구분
print('# 다차원 넘파이 배열 인덱싱 : 각 차원의 인덱스를 ','로 구분')
x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x2[1,2])
print(x2[0,0])
print(x2[-1,-1], '\n')

# boolean 인덱싱 : 조건을 사용해 배열의 특정 요소 선택
print('boolean 인덱싱 : 조건을 사용해 배열의 특정 요소 선택')
x = np.array([1,2,3,4,5,6])
y = x > 3
print(y) # 조건에 충족하는 요소들은 True, 충족하지 못하면 False
print(x[y], '\n') # 조건에 충족하는 요소들만 출력

# 펜시 인덱싱 : 넘파이 배열의 특정 인덱스를 리스트나 배열로 지정해 여러 요소를 한 번에 선택
y = [0,2,4]
print('펜시 인덱싱')
print(x[y], '\n')

# 다차원 배열 슬라이싱 : 차원마다 ','를 사용해 별도로 지정
print('다차원 배열 슬라이싱')
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[0:2,1:3], '\n')
y = x[:, 1]
print(y)

# boolean 배열을 사용한 슬라이싱
print('boolean 배열을 사용한 슬라이싱--')
y = x % 2 == 0
print(y)
print(x[y])
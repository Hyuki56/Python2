# 배열 비교
import numpy as np
x = np.array([1,2,3,4,5])
print(x>3)

y = np.array([[1,2,3],[4,5,6]])
print(y>3)
print()

# 배열간 비교 ( 브로드 캐스팅 비교 )
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(' 배열간 비교 ')
print(x>=y)
print(x>=z)

# np.all() : 모든 요소가 True 인지 평가
# np.any() : 하나 이상의 요소가 True 인지 평가

x = np.array([1,2,3])
result1 = np.empty((),dtype=bool) # 0차원 넘파이 베열
np.all(x>0, out=result1) # out : 결과를 저장할 넘파이 배열
print(result1)

#out 사용 안 함
result1 = np.all(x>0)
print(result1)

# np.any() : 하나 이사으이 요소가 True 인지 평가 
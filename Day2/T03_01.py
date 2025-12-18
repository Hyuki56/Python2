'''넘파이 배열 연산

특징
- 브로드 캐스팅 : 두 배열의 크기가 같을 때 요소별 연산 자동 수행
- 벡터화 : 배열 간 연산을 반복문을 사용하지 않고 빠르게 처리
- 데이터 타입 : 연산 결과도 같은 데이터 타입으로 반환 '''

import numpy as np


# 산술 연산
x = np.array([1,2,3])
y = np.array([3,2,1])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# 지수 연산 (제곱)
a = x ** 2
print(a)

# 비교 연산
print(x>y)
print(x==y)

# 넘파이 배열과 스칼라(단일 값) 연산
a = x + 2
print(a)
b = x + 5
print(b)

# 논리 연산(AND, OR, NOT)
x = np.array([True, False, True])
y = np.array([False, False, True])
# np.logical_and(x,y) : AND
a = np.logical_and(x,y)
print(a)

# np.logical_or : OR
a = np.logical_or(x,y)
print(a)

# np.logical_not : NOT
a = np.logical_not(x)
print(a)

# np.sqrt : 넘파이 베열의 각 요소에 대한 제곱근 연산 수행
x = np.sqrt([1,4,9])
a = np.sqrt(x)
print(a)
''' 표준 모듈
파이썬에서 기본으로 제공하는 모듈

math 모듈
파이썬에서 수학 관련 기능을 다룰 때 주로 사용하는 모듈. 삼각함수,
제곱근, 로그, 절대값 계산 등 다양한 수학 관련 함수를 제공함.

# 사용 방법
import math

# 상수 사용 방법
모듈명.상수명 '''

import math

def circumference(r):
    return 2 * math.pi * r
'''
radius = float(input('반지름 입력 : '))

# 함수 호출해 원 둘레 구하기
result = circumference(radius)
print(f'반지름이 {radius}인 원의 둘레 : {result:.2f}')
# f-string 방식에서 {실수:.nf} : 소수점 이하 n자리 출력
'''

# 올림 ceil(값)
print('1.2를 올림 처리하면',math.ceil(1.2))
print('-3.5를 올림 처리하면',math.ceil(-3.5))
print()

# 내림 floor(값)
print('1.7을 내림 처리하면',math.floor(1.7))
print('-2.7을 내림 처리하면',math.floor(-2.7))
print()

# 소수점 이하 버리기 : trunc(실수)
print('1.3의 소수점 이하를 버리면',math.trunc(1.3))
print('-2.3의 소수점 이하를 버리면',math.trunc(-2.3))

# sqrt(n) : n의 제곱근 반환
# pow(n,m) : n을 m번 거듭제곱한 값 반환

n = 49
# 제곱근
result1 = math.sqrt(n)
result1 = int(result1)
print(f'{n}의 제곱근 : {result1}')

# 거듭제곱
result2 = math.pow(n,3)
print(f'{n}의 3 거듭제곱 : {result2}')
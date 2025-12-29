''' pandas
데이터 조작, 분석을위한 오픈소스 라이브러리로 주로 데이터 과학, 분석, 머신러닝
통계학 등의 분야에서 사용됨. 표 형식의 데이터를 다루기 위한 DataFrame, Series
두 가지 주요 데이터 구조를 제공함

- 강력한 데이터 구조 (Series, DataFrame)
- 데이터 조작 및 변환 (필터링, 정렬, 그룹화, 집계 등 다양한 데이터 조작 기능)
- 데이터 입출력 (CSV, Excel, SQL, JSON 등 여러 형식의 데이터 파일
- 유연한 데이터 처리 (결측치, 데이터 타입 변환, 중복 데이터 제거 등)
- 고성능 계산 지원
- 통계 기능 (평균, 중위수, 분산, 표준 편차 등 다양한 통계량 계산 가능)
- 시계열 데이터 처리
- 시각화 지원 (Matplotlib 과 함께 사용, 직접 시각화 함수 제공)
'''
import pandas as pd

''' Series
데이터 분석에 유용한 1차원 배열 구조로 다양한 데이터 타입을 저장하고
인덱스를 통해 데이터에 접근 가능함. NumPy 배열을 기반으로하며 고급 데이터 조작, 분석 기능을 제공함.
- 1차원 데이터 (배열)
- 인덱스로 접근 가능(정수형 인덱스, 사용자 정의 인덱스)
- 다양한 데이터 타입을 혼합하여 저장 가능
- 데이터 분석에 필요한 다양한 함수, 속성 제공
'''

# Series 생성
# 리스트 사용
x = ['value',10,20,30,40]
y = pd.Series(x)
# print(y)

# 사용자 정의 인덱스 사용
y = ['index','a','b','c','d'] # 인덱스로 사용할 리스트
z = pd.Series(x,index=y)
# print(z)

# dictionary 사용 (key는 인덱스, value는 데이터)
x = {'apple':1, 'banana':2, 'cherry':3}
y = pd.Series(x)
# print(y)

# Seires 구조 확인 > # dtype
# print(y.dtype)

# index 속성
# print(y.index) # object 속성은 파이썬 객체들이 들어가는 바구니와 같다

# values 속성 (Series의 값 자체를 NumPy 배열로 변환)
# print(y.values)

x = pd.Series([1,2,3,4,5,6,7,8,9])
# head() : Series의 상위 n 개의 데이터를 출력, Series의 데이터 타입도 무조건 출력
# print(x.head())
# tail() : Series의 하위 n 개의 데이터를 출력
# print(x.tail())

# 인덱싱, 슬라이싱
# .iloc[] : 위치 기반 인덱싱 ( iloc > index location의 약자 )
# print(x.iloc[1])

# 위치 기반 슬라이싱
# print(x.iloc[1:4])

# .loc[] # 레이블 기반 인덱싱 ( 레이블 = 인덱싱 )
x = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(x.loc['b'])
print(x.loc['b':'d']) # 레이블 기준 범위 'b' >= 'd', 슬라이싱 기준 범위 'b' > 'd' ( 레이블과 슬라이싱의 범위가 다름 )
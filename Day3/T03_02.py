import pandas as pd
# 데이터 추가

data = pd.Series([1,2,3],index=['a','b','c'])
data2 = pd.Series([4,5], index=['d','e'])

# concat() : Series에 새로운 Series를 합치는 방식으로 데이터 추가
r1 = pd.concat([data,data2])
# print(r1)

# 할당 연산을 사용한 데이터 추가
r1['f'] = 6
# print(r1)

# Series 값 수정
# 인덱스 기반 값 수정
r1['b'] = 22
# print(r1)

# 인덱스 기반 다수의 값 수정
r1[['a','c']] = [11,33] # 인덱스를 리스트로 묶어서 줘야한다.
print(r1)

# 조건부 수정
r1[r1>10] = r1[r1>10]+100
print(r1)

# rename(): 인덱스 이름 변경
r1 = r1.rename({'a':'aa','b':'bb'}) # 원하는 인덱스와 변경 값을 딕셔너리 형태로 전달
print(r1)
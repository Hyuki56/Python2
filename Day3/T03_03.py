# 데이터 통계 및 요약
from operator import concat

import pandas as pd

d = pd.Series([1,2,3,4,5])

# mean() : 평균
avg = d.mean()
print(avg)

# sum() : 합계
s = d.sum()
print(s)

# median() : 중위수
mid = d.median()
print(f'중위수 : {mid}')

max = d.max()
print(f'최댓값 : {max}')

min = d.min()
print(f'최솟값 : {min}')

variance = d.var() # var() : 분산 (데아터가 평균으로부터 퍼짐 정도)
print(f'분산 : {variance}')

std_dev = d.std() # std() : 표준 편차 (분산의 제곱근, 데이터의 변동성)
print(f'표준 편차 : {std_dev}')

# 고유값
d = pd.Series(['a','b','a','c','b','a'])
# value_counts() : 빈도 수 확인
v_count = d.value_counts()
print(f'빈도 수 확인 : {v_count}')

v_counts_nomalized = d.value_counts(normalize=True) # 비율 확인
print(f'비율 확인 : {v_counts_nomalized}')

# 데이터 필터링 및 조건 검색
d = pd.Series([1,2,3,4,5])
f_data = d[d>3] # d[조건] 조건은 True False로 나올 수 있는 값으로 넣어줘야 한다
print(f_data)

# 다중 조건 필터링
and_f = d[(d>2.5) & (d<3.5)]
print(f'AND 조건 필터링 : {and_f}')

or_f = d[(d<2.5) | (d>3.5)]
print(f'OR 조건 필터링 : {or_f}')

# concat() : 데이터 연결
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5])
new_s = pd.concat([s1,s2])
print(f'concat 데이터 연결 : {new_s}') # index가 0,1,2,0,1로 나옴
# 사용자 정의 index= 와 파이썬 pd 내부의 인덱스가 나뉘는데 위와 같은 경우는 또 내부의 인덱스가 따로?

# 데이터 정렬
d = pd.Series([4,3,2,1],index=['a','b','c','d'])
x = d.sort_values() # value 기준 데이터 오름차순 정렬
print('오름차순 정렬')
print(x)

x = d.sort_values(ascending=False) # value 기준 데이터 내림차순 정렬
print('내림차순 정렬')
print(x)


'''
concat 데이터 연결 : 0    1
1    2
2    3
0    4
1    5'''
print(new_s[1])
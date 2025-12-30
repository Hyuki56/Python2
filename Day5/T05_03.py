''' 데이터 구조 이해
df.info() : DataFrame 기본 정보 출력
- DataFrame의 행, 열 수
- DataFrame의 각 열 이름
- DataFrame의 각 열의 데이터 타입
- DataFrame의 각 열의 non_null(비결측값) 수  # 비결측값 = 채워져 있는 수?
'''

import pandas as pd
df = pd.read_csv('data.csv')
print('---DataFrame 기본 정보---')
print(df.info()) # 마지막 결과 값 None 나오는 게 print문 때문
# df.info() # 마지막 결과 None 안나옴

''' 통계적 요약 : df.describe()
기초 통계량을 확인하여 데이터의 분포와 범위 이해
(기본적으로 숫자형 열에만 적용)

count : 각 열의 수(결측값 제외)
mean : 평균값
std : 표준 편차
min : 최솟값
25% : 1사분위수(하위 25% 지점)
50% : 중위수(2사분위수)
75% : 3사분위수(상위 25% 지점)
max : 최댓값 '''

print('\n\n---통계적 요약---')
print(df.describe()) # print를 쓰는 이유 한 파일에서 출력하는 데 인터프리터가 df.info()와 df.describe 여러 개 중 마지막 결과만 출력할 수 있어서

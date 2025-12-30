'''
카운트 플롯 (Countplot)
범주형 데이터의 카테고리별 데이터 개수(빈도)를 막대 형태로 나타내는 그래프.
각 카테고리에 속하는 데이터의 양을 비교하고 범주형 변수의 분포를 파악하는데 유용함.

seaborn.countplot(data, x, fill)
data : 카운트 플롯을 생성할  지정
x : x축 값들 (기본값 None)
fill : 막대 스타일 지정 (기본값 True)

matplotlib의 bar plot : 범주별 값(수치) 표현, 빈도를 직접 계산해주지 않음
'''


import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

data = {
  '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
  '인구 밀도(명/km²)': [17000, 12000, 8000, 10000, 7000, 6500, 7500, 9000, 11000, 500, 1200, 1300, 800, 700, 1100, 1400, 600],
  '평균 연령': [40, 42, 38, 39, 37, 36, 35, 34, 41, 43, 45, 44, 38, 36, 37, 39, 42]
}

df_data = pd.DataFrame(data)

sns.countplot(data=df_data, x='평균 연령', fill=True)

plt.title('카운트 플롯')
plt.xlabel('평균연령')
plt.ylabel('수')

plt.show()
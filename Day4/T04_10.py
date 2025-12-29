'''
클러스터맵 (Clustermap)

cluster : 군집
군집화 : 서로 비슷한 데이터를 묶는 것

2차원 행렬 데이터를 계층적 클러스터링으로 행, 열을 재정렬하고 히트맵으로 표현하는 그래프. 덴드로그램(dendrogram)은 나뭇가지 모양의 다이어그램으로 클러스터맵의 옆면이나 위쪽에 표시되며 데이터간 유사성에 따른 계층적 연결 구조를 보여줌.

sns.clustermap(data, cmap, annot, fmt)
data : 클러스터맵 생성 데이터 지정
cmap : 컬러맵 (기본값 None)
annot: 각 셀의 설명 표기
fmt : 각 셀의 설명 서식
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

data = {
  '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
  '인구 밀도(명/km²)': [17000, 12000, 8000, 10000, 7000, 6500, 7500, 9000, 11000, 500, 1200, 1300, 800, 700, 1100, 1400, 600],
  '평균 연령': [40, 42, 38, 39, 37, 36, 35, 34, 41, 43, 45, 44, 38, 36, 37, 39, 42]
}

df_data = pd.DataFrame(data)
numeric_data = df_data.set_index('지역').select_dtypes(include=['number']) # 넘버 데이터들만 포함하겠다
sns.clustermap(numeric_data, cmap='coolwarm', annot=True, fmt='d')

plt.title('클러스터(히트)맵')

plt.show()

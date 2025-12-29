'''
박스 플롯 (Boxplot)
수치 데이터를 시각화하여 집합의 범위와 중위수를 빠르게 확인할 수 있으며 통계적으로 이상치가 있는지 빠른 확인이 가능한 시각화 기법. 수치 데이터를 통계량을 상자 모양으로 상위 경계, 3사분위수, 2사분위수(중위수), 1사분위수, 하위 경계, 이상치로 구성됨.

sns.boxplot(data,fill,gap)
data : 박스 플롯을 생성할 데이터
fill : 거친 스타일 적용 여부 (기본값 True)
gap : 요소 간 간격 (기본값 0)

수염(whiskers) : 이상치를 제외한 데이터 범위
이상치(outlier) : 보통 범위를 벗어난 값, 점으로 표시
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

data = {
    '수익' : [1000,1500,1300,1600,1700],
    '비용' : [800,1200,1100,1300,1400],
    }

df_data = pd.DataFrame(data)

sns.boxplot(data=df_data, fill=False, gap=0.1)
plt.title('박스 플롯')
plt.show()
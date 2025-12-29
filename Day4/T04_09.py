'''
seaborn
matplotlib의 확장된 개념으로 심미적 그래프를 쉽게 그리도록 도와주는 도구.
matplotlib이 세부적 커스터마이징에 유용하다면, seaborn은 빠르고 아름다운 시각화를 위한 고수준 인터페이스를 제공. 기본적으로 제공되는 디자인과 색상이 예뻐서 그래프를 꾸미는 노력을 덜어줌.

히트맵(Heatmap)
2차원 행렬 형태의 데이터를 색상의 농도나 변화로 표현하는 그래프. 데이터의 크기, 패턴, 변수 간 상관 관계를 시각적으로 파악하는데 유용함

sns.heatmap(data, cmap, annot, fmt)
data : 히트맵 생성할 데이터 지정
cmap : 컬러맵 (색상, matplotlib의 컬러맵 이름 가능)
annot(annotation) : 각 셀의 설명 표기 (기본값 None)
fmt : 각 셀의 설명 서식 (기본값 '.2g')
'''

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# print(sns.__version__)
# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

data = [[100,150,200,120],
        [80,120,180,160],
        [75,130,190,180],
        [90,140,170,190],
        [60,110,160,140]]

sns.heatmap(data,cmap='Blues',annot=True,fmt='d')
# fmt : 정수(d), 실수(.nf, 소수점 이하 n자리)

plt.title('히트맵')
plt.xlabel('x축')
plt.ylabel('y축')

plt.show()
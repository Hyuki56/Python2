''' 히스토그램
연속적인 수치 데이터를 일정한 구간(bins)으로 나누어 각 구간에 포함된 데이터의 빈도를 나타내는
그래프.

plt.hist(x,bins,color,alpha)
x : 히스토그램 생성 데이터 지정
bins : 데이터를 나눌 구간의 수 또는 경곗값 지정 인자 (기본값 None)
color : 막대 색상 지정 (기본값 None)
alpha : 투명도 '''

import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

data = []
for i in range(500):
    value = sum([(i*j) % 100 / 100 for j in range(1,13)])-6
    data.append(value)

# 히스토그램 그리기
plt.hist(data,bins=30,color='pink',alpha=0.7)

plt.title('정규 분포 히스토그램')
plt.xlabel('값')
plt.ylabel('빈도 수')
plt.grid() # 격자

plt.show() # 그래프 표시
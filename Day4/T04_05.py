'''
산점도 (Scatter plot)
두 변수 간 관계를 점으로 표현한 그래프, 각 점은 데이터의 한 관측 값을 나타내며 x,y축의 좌표는 값 변숫값을 의미함.

plt.scatter(x,y,c,s)
x : 데이터 포인트의 x축 좌표 지정
y : 데이터 포인트의 y축 좌표 지정
c : 각 점 색상 지정 (기본값 None)
s : 각 점 크기 지정 (기본값 None)
'''

import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 생성
x = [1.5, 2.5, 3.5, 4.5, 5.5]
y = [50, 60, 65, 70, 75]
plt.scatter(x, y, c='blue', s=100)

# 그래프 요소 추가
plt.title('키와 몸무계 관계')
plt.xlabel('키(m)')
plt.ylabel('몸무게(kg)')
plt.grid()

plt.show()
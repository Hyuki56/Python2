'''
파이 차트 (Pie chart)
원형 차트로 전체를 100%로 보고 각 부분이 전체에서 차지하는 비율을 시각화한 그래프

plt.pie(x,labels,colors,autopct,startangle,explode)
x : 그래프 비율 값 지정
labels : 각 조각에 대한 레이블 지정
colors : 색상 지정
autopct : 각 조각 비율 텍스트 표시
startangle : 첫 번쨰 조각의 시작 각도 (기본값 0 : 3시 방향, 90 : 12시 방향, 180 : 9시 방향, 270 : 6시 방향)
explode : 특정 조각을 원 중심에서 떨어트릴 정도 지정 ( 기본값 : None ) '''

import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 생성
labels = ['피자','햄버거','샐러드','파스타']
sizes = [40,30,20,10]
colors = ['gold','lightcoral','lightskyblue','lightgreen']
explode = (0.1,0,0,0)

# 파이 차트 그리기
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',startangle=90,explode=explode)
plt.show()
''' 막대 그래프 (Bar chart)
각 범주에 대한 값을 막대의 길이로 표현하여 범주 간 비교를 용이하게 하는 그래프.

plt.bar(x,height,width)
x : 그래프의 x축 위치 지정 인자
height : 각 막대 높이 지정 인자
width : 각 막대 너비 지정 인자

'''
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 생성
categories = ['학생1','학생2','학생3','학생4']
v1 = [85,92,78,90]
v2 = [88,91,75,85]

x = np.arange(len(categories)) # 범주 위치 생성
# 막대 그래프 그리기
plt.bar(x-0.2,v1,width=0.4,label='1반',color='blue')
plt.bar(x+0.2,v2,width=0.4,label='2반',color='yellow')

# 그래프 요소 추가
plt.title('학생 성적 비교')
plt.xlabel('학생')
plt.ylabel('성적')
plt.grid(axis='y') # y축에만 격자
plt.xticks(x,categories) # x축 눈금 범주 설정
plt.legend() # 범례

plt.show()
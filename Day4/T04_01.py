''' pip install matplotlib 설치

matplotlib
파이썬에서 데이터 시각화를 위한 가장 인기있는 라이브러리중 하나.
여러 유형의 그래프를 지원하여 데이터를 시각적으로 분석하고 이해하는데 유용함.

plot(플롯)
데이터를 다양한 그래프의 형식으로 표현하는 일종의 캔버스와 같은 역할을 함.

matplotlib에서 제공하는 하위 모듈로 플롯을 생성, 관리하는 함수들을 포함.
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
# print(mpl.__version__) # matplotlib 버전 확인용

''' plt.plot(*args) : 기본 플롯 생성 함수
*args(가변 매개변수) : 그래프에 표시할 데이터를 지정 (일반적으로 x, y 좌표 전달 '''

# 데이터 생성
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1,0]

plt.plot(x, y) # x와 y를 메모리 상에서 직선 그래프 그리기
plt.title('Line Graph')
plt.xlabel('X-axis') # x축 레이블
plt.ylabel('Y-axis') # y축 레이블
plt.grid(True) # 격자 추가
plt.show()



'''
강사꺼 복붙
matplotlib
파이썬에서 데이터 시각화를 위한 가장 인기 있는 라이브러리 중 하나.
여러 유형의 그래프를 지원하여 데이터를 시각적으로 분석하고 이해하는데
유용함.

plot(플롯)
데이터를 다양한 그래프의 형식으로 표현하는 일종의 캔버스와 같은 역할을 함.

Pyplot
matplotlib에서 제공하는 하위 모듈로 플롯을 생성, 관리하는 함수들을 포함.
import matplotlib as mpl
import matplotlib.pyplot as plt
# print(mpl.__version__)

plt.plot(*args) : 기본 플롯 생성 함수
*args : 그래프에 표시할 데이터 지정 (일반적으로 x, y 좌표 전달) 

# 데이터 생성
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1,0]

plt.plot(x,y)
plt.title('Line Graph') # 그래프 제목 설정
plt.xlabel('X-axis') # x축 레이블
plt.ylabel('Y-axis') # y축 레이블
plt.grid(True) # 격자 추가
plt.show() # 플롯 표시

'''
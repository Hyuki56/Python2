import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 생성
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1,0]
y2 = [0,1,2,3,4,5,6,7,8,9]

'''
linestyle : 선 스타일 지정 (기본값 : '-'실선)
'--' : 점선
':' : 좁은 간격 점선
'-.' : 대시 점선 '''
# 선 그래프 그리기
plt.plot(x,y,label='감소하는 선',color='blue',linestyle=':')
plt.plot(x,y2,label='증가하는 선',color='#FF0000',linestyle='-')


# 그래프 요소 추가
plt.title('Cross Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend() # 범례 >> plt.plot()에서 설정한 label 보여주는 듯
plt.show()

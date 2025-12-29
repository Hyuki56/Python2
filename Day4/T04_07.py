'''
서브 플롯 (subplot)
하나의 그림 안에 여러 개의 플롯을 격자 형태로 배치하는 방법

plt.subplots(nrows, ncols)
nrows : 서브 플롯의 행 개수 지정 (기본값 : 1 )
ncols : 서브 플롯의 열 개수 지정 (기본값 : 1)

'''

import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = 'Noto Sans CJK KR'

# 마이너스 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(1,2) # 1행 2열

# 첫 번째 서브 플롯 (선 그래프)
axs[0].plot([1,2,3],[1,4,9])
axs[0].set_title('선 그래프')
axs[0].set_xlabel('x값')
axs[0].set_ylabel('y값')

# 두 번째 서브 플롯 (막대 그래프)
axs[1].bar([1,2,3],[3,5,2])
axs[1].set_title('막대 그래프')
axs[1].set_xlabel('카테고리')
axs[1].set_ylabel('빈도 수')

plt.show()
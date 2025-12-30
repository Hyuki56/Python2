'''
플롯 이미지
matplotlib에서 생성한 플롯은 PNG, JPEG, PDF등 다양한 형식으로 저장 가능

plt.savefig()
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,1]

# 플롯 생성 및 사이즈 설정
plt.figure(figsize=(8,6)) # 가로8인치 세로6인치
plt.plot(x,y)

plt.title('sample line graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# 그래프를 파일로 저장
plt.savefig('sample_plot.png')

plt.show()
''' random 모듈
난수를 생성해주는 모듈 '''
import random

# randint(a,b) : a와 b 사이의 범위에서 랜덤한 정수 생성
# randrange(start,stop,step) : start부터 stop 이전까지
# step간격으로 임의의 정수 하나 생성, start의 기본값은 0

# 1~45 사이의 랜덤한 정수
r1 = random.randint(1,45)
print(f'1~45 사이의 랜덤한 정수 : {r1}')

# 0 이상 10 미만의 정수
r2 = random.randrange(10)
# 1 이상 20 미만의 홀수
r3 = random.randrange(1,20,2)
print(r2)
print(r3)

# sample(a, b) : 시퀀스 자료형 a 중에서 지정된 개수 b만큼의
#                요소 반환, 반환 결과는 중복이 없는 리스트

def lotto():
    n = random.sample(range(1,46),6)
    return n

lotto_num = lotto()
print('로또 번호 :',lotto_num)

# choice(시퀀스_자료형) : 시퀀스 자료형의 요소 중 하나
#                       임의로 반환
# shuffle(시퀀스_자료형) : 시퀀스 자료형의 요소 순서를
#                        임의로 섞어서 반환
# random() : 0 이상 1 미만의 임의의 실수 반환

import random as r # alias 별칭
print('\n\n\n\n\n=======아이스크림 내기=======')
# 당첨자 뽑기
def generate_win(persons):
    winner = r.choice(persons)
    return winner

list_persons = [] # 참여할 사람들
for i in range(1,6):
    person = input('참여할 사람 : ')
    list_persons.append(person)

print('아이스크림 내기 참여자 :',list_persons)

# 당첨자 뽑기
winner = generate_win(list_persons)
print(f'아이스크림 계산할 사람 : {winner}')
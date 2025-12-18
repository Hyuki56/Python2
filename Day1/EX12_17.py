''' datetime 모듈
파이썬에서 날짜와 시간을 다루는 모듈

datetime.now() : 현재 날짜와 시간 반환
date() : 매개 변수로 받은 숫자를 'YYYY-mm-dd' 형식으로 반환
time() : 매개 변수로 받은 숫자를 'HH:MM:SS' 형식으로 반환 '''

import datetime

# 현재 날짜 및 시간
present = datetime.datetime.now()
print('현재 :',present)

# 날짜
print(f'오늘 날짜 : {present.date()}')
datetime.datetime.now().date()

# 년도
print(f'지금은 {present.year}년입니다.')

# 매개 변수로 받은 수를 'YYYY-MM-DD' 형식으로 변환
birthday = datetime.date(2000, 1, 1)
print(f'생일 : {birthday}')

# 매개 변수로 받은 수를 'HH:mm:ss' 형식으로 변환
lunch_time = datetime.time(12,00,00)
print(f'점심 시간 : {lunch_time}')
'''
timedelta() : 주, 일, 시간, 분, 초 등 다양한 단위로 날짜와
        시간 간 간격을 계산하거나 특정 날짜, 시간을 조작하는데 사용
1주 : timedelta(weeks=1)
1일 : timedelta(days=1)
1시간 : timedelta(hours=1)
1분 : timedelta(minutes=1)
1초 : timedelta(seconds=1) '''

pw = input('설정할 비밀번호 입력 : ')
# 현재 시간, 날짜
today = datetime.datetime.now()
pw_expired_day = today+datetime.timedelta(days=90)

print('비밀번호 설정 완료')
print(f'비밀번호는 90일 후 {pw_expired_day}에 만료됩니다.')
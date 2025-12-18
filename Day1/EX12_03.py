''' 파일 전체가 아닌 특정 함수만 필요한 경우
# 방법
from 파일명(모듈명) import 함수명
from 파일명(모듈명) import 함수명1, 함수명2 '''

from EX12_01 import hour_to_min
from EX12_01 import min_to_sec

min = hour_to_min(7)
print(f'7시간은 {min}분')

sec = min_to_sec(13)
print(f'13분은 {sec}초')

# 모듈 내 모든 함수 import
# from 모듈명 import *
from EX12_01 import *

min = hour_to_min(6)
print(f'6시간은 {min}분')

sec = min_to_sec(12)
print(f'12분은 {sec}초')

sec = hour_to_sec(3)
print(f'3시간은 {sec}초')
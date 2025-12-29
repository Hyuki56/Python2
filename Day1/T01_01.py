''' 모듈 (module)
여러 변수, 함수, 클래스를 하나로 묶어놓은 집합으로 다른 개발자
들이 쉽게 코드를 활용할 뿐 아니라 자신의 코드도 효율적으로 관리
할 수 있음.

# 모듈 불러오기
import 모듈_이름 '''
MIN = 60 # MIN 상수
SEC = 60 # SEC 상수

# 시간을 분으로 바꿔주는 함수
def hour_to_min(hour):
    return hour * MIN

# 분을 초로 바꿔주는 함수
def min_to_sec(min):
    return min * SEC

# 시간을 초로 바꿔주는 함수
def hour_to_sec(hour):
    return min_to_sec(hour_to_min(hour))
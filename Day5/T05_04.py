''' 데이터 전처리

데이터 결측치 처리
단순 빈 값을 채우는 작업이 아니라 데이터의 특성과 격측 발생 원인을 고려해 접근해야 함

결측값(Missing Value) 확인
'''
import pandas as pd

data_dict = [
    {'사번':25001,'나이':20,'부서':'정보보호부'},
    {'사번':25002,'이름':'이영희','부서':'기술부'},
    {'사번':25003,'이름':'박민수','나이':22,},
    {'사번':25004,'이름':'정수진','나이':20,},
    {'사번':25005,'이름':'한미래','나이':23,'부서':'개발부'},
]

df = pd.DataFrame(data_dict)
print(df)

# isnull() : 결측값 여부 확인
# 결측값 수 확인 : isnull().sum()
print('\n\n---결측값 여부---')
print(df.isnull())

print('\n\n---각 열의 결측값 수---')
print(df.isnull().sum())

# 결측값 비율 확인
print('\n\n---각 열의 결측값 비율---')
print(df.isnull().mean() * 100)

# 결측값 제거 : pandas.DataFrame.dropna()
# axis : default 0(행), 1(열)
# na : Not Available의 약자 ( 값 없음, 결측치 없음 )

df_dropped_rows = df.dropna() # 결측값 행 제거
print('\n\n---결측값 포함한 행 제거---')
print(df_dropped_rows)

df_dropped_cols = df.dropna(axis=1) # 결측값 열 제거
print('\n\n---결측값 열 제거---')
print(df_dropped_cols)

# 결측값 평균으로 대체 :  fillna(mean()) (기본적으로 숫자형 데이터에만 적용)

df_fillna = df.fillna({'나이':df['나이'].mean()})
print('\n\n---결측값 평균으로 대체(나이)---')
print(df_fillna)

# 결측값 중위수로 대체 : fillna(median())
# 데이터에 이상치가 있는 경우 평균보다 중위수로 대체하는 것이 더 적합

df_median = df.fillna({'나이':df['나이'].median()})
print('\n\n---결측값 중위수로 대체 (나이)---')
print(df_median)

# 결측값 최빈값으로 대체 : fillna(mode())
# mode() : 최빈값을 계산하여 Series로 반환해주는 함수 최빈값이 여러 개일 경우 가장 첫 번째 최빈값을 선택, 범주형 데이터 타입에 적합

df_mode = df.fillna({'부서':df['부서'].mode()[0]})
print('\n\n---결측값을 최빈값으로 대체 (부서)---')
print(df_mode) # 다 동일하게 1번이니까 가나다 순으로 해서 개발부가 0번

# 중복 데이터 제거 : drop_duplicates()
data_dict = [
    {'사번':25001,'이름':'김철수','나이':20,'부서':'정보보호부'},
    {'사번':25001,'이름':'김철수','나이':20,'부서':'정보보호부'},
    {'사번':25002,'이름':'이영희','나이':21,'부서':'기술부'},
    {'사번':25003,'이름':'박민수','나이':22,'부서':'생산부'},
    {'사번':25004,'이름':'정수진','나이':20,'부서':'전략본부'},
    {'사번':25005,'이름':'한미래','나이':23,'부서':'개발부'},
    {'사번':25005,'이름':'한미래','나이':23,'부서':'개발부'},
]
print('\n\n---중복 제거 전---')
df_no_duplicate = pd.DataFrame(data_dict)
print(data_dict)

print('\n\n---중복 제거 후---')
df_duplicate = df_no_duplicate.drop_duplicates()
print(df_duplicate)

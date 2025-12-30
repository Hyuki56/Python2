import pandas as pd

data_dict = [
    {'사번':25001,'이름':'김철수','나이':20,'부서':'정보보호부'},
    {'사번':25002,'이름':'이영희','나이':21,'부서':'기술부'},
    {'사번':25003,'이름':'박민수','나이':22,'부서':'생산부'},
    {'사번':25004,'이름':'정수진','나이':20,'부서':'전략본부'},
    {'사번':25005,'이름':'한미래','나이':23,'부서':'개발부'},
]

df = pd.DataFrame(data_dict)

# 특정 칼럼 인덱싱
print('---이름 열 인덱싱---')
print(df['이름'])

# 특정 행 인덱싱
print('\n\n---세 번째 행 인덱싱---')
print(df.loc[2])

print('\n\n---나이가 21세 이상인 직원---')
print(df[df['나이']>=21])

print('\n\n---나이가 21세 이상 & 생산부인 직원')
print(df[(df['나이']>=21) & (df['부서']=='생산부')])

# 데이터 슬라이싱 : 연속적인 데이터 범위 선택
print('\n\n---처음 두 열---')
print(df.iloc[:,0:2]) # iloc > index기반 location

print('\n\n---2~4 번째 행---')
print(df.iloc[1:4,:]) # 또는 [1:4]만 해도 출력 됨

print('\n\n---2~4 번째 행의 처음 두 열---')
print(df.iloc[1:4,0:2])

print('\n\n---사번 열, 부서 열---')
print(df[['사번','부서']]) # 컬럼 여러 개 줄 땐 리스트로 묶어서

# 데이터 정렬 : df.sort_values()
# ascending : True(default, 오츰차순), False(내림차순)

print('\n\n---나이 기준 오름차순 정렬---')
print(df.sort_values('나이'))

print('\n\n---나이 기준 내림차순 정렬---')
print(df.sort_values('나이', ascending=False))

print('\n\n---나이 기준 내림차순 & 부서 기준 오름차순 정렬---')
print(df.sort_values(['나이','부서'], ascending=[False, True])) # 컬럼 여러 개 줄 땐 리스트로 묶어서
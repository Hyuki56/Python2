'''
DataFrame
Pandas에서 제공하는 2차원 배열 구조로 각 열은 Series로 구성되어 있으며 서로 다른 데이터 타입 포함 가능.
- 2차원 데이터(행은 레코드, 열은 변수 또는 속성)
- 인덱스 (행 인덱스는 기본적으로 0으로 시작, 열 이름(헤더) 존재)
- 다양한 데이터 타입 (각 열은 서로 다른 데이터 타입을 가질 수 있음)
- 데이터 조작 기능 (필터링, 그룹화, 정렬 등)'''

import pandas as pd

# 리스트 사용한 DataFrame을 생성 ( 열 이름 지정 가능 )
x = [['밀탱크', 10, '분당'], ['밀카우', 11, '서울'], ['어피치', 12, '제주']]
df = pd.DataFrame(x,columns=['이름', '나이', '지역'])
print(f' DataFrame\n{df}')

# Dictionary 사용한 DataFrame 생성 ( key : 열 이름, value : 값 )
x = {'이름' : ['밀탱크', '밀카우', '어피치'],
     '나이' : [10, 11, 12],
     '지역' : ['분당', '서울', '제주']}
df = pd.DataFrame(x)
print(f'Dictionary를 사용한 DataFrame \n{df}')

# Numpy 배열을 사용한 DataFrame 생성
import numpy as np
x = np.array([['밀탱크', 10, '분당'], ['밀카우', 11, '서울'], ['어피치', 12, '제주']])
df = pd.DataFrame(x, columns=['이름', '나이', '지역'])
print(f'Numpy 배열을 사용한 DataFrame \n{df}')


print(f'-열 이름 \n{df.columns}')
print(f'-행 인덱스 정보\n{df.index}')
print(f'-데이터 프레임의 전체적인 구조 정보 \n{df.info}')
print(f'-상위 행 반환 \n{df.head(1)}')
print(f'-하위 행 반환 \n{df.tail(2)}')

# 인덱싱 및 슬라이싱
print('\n인덱싱 및 슬라이싱')
print(df.iloc[1,1]) # iloc[행, 열] 인덱싱
print()
print(df.iloc[0:3, 1:2]) # iloc[] 슬라이싱

df = pd.DataFrame(x, columns=['이름','나이','지역'],index=['A','B','C'])
print('\n레이블 기반 인덱싱')
print(df.loc['A','지역']) # 레이블 기반 인덱싱 loc
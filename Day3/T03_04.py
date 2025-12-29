import pandas as pd
# Series
d = pd.Series([1,2,3,1,2,3], index=['a','b','a','b','a','b'])

# groupby() : 특정 기준에 따라 데이터 그룹화
x = d.groupby(level=0).sum() # 단일 인덱스라 level 0
print(f'그룹화 후 합계 \n{x}')

y = d.groupby(level=0).mean()
print(f'그룹화 후 평균 \n{x}')

# 멀티 인덱스
i = [[1,2,1,2],['a','a','b','b']]
s = pd.Series([1,2,3,4],index=i)
print(f'멀티 인덱스 \n{s}')

# agg() : 여러 집계 함수 사용
agg_g = d.groupby(level=0).agg(['sum','mean','count'])
print(f'그룹화 후 여러 집계 함수 \n{agg_g}')
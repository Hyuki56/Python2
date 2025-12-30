# 데이터 정렬
import pandas as pd
df = pd.DataFrame({
    'Name':['민지홍','강동원','밀탱크','어피치'],
    'Age':[24,45,10,11],
    'Score':[100,100,90,95]
})
# sort_values() : 특정 열 기준 정렬
print('나이 기준 오름차순 정렬')
s_df = df.sort_values(by='Age')
print(s_df)

print('나이 기준 내림차순 정렬')
s_df2 = df.sort_values(by='Age',ascending=False)
print(s_df2)

# sort_index : 행 인덱스 기준 정렬
s_df = df.sort_index()
print('행 인덱스 기준 오름차순 정렬')
print(s_df)

s_df2 = df.sort_index(ascending=False)
print('행 인덱스 기준 내림차순 정렬')
print(s_df2)

# 그룹화 및 집계
df = pd.DataFrame({
    'category':['a','b','a','b','a','b'],
    'type':['x','y','x','y','x','y'],
    'values':[1,2,3,4,5,6]
})
# groupby() : 하나 이상 열 기준 그룹화
print('\ngroupby 합')
g_sum = df.groupby('category')['values'].sum()
print(g_sum)

# 다중 열 기준 그룹화 > 다중이라 리스트로 묶어서 주기
print('\ngroupby 평균')
g_mean = df.groupby(['category', 'type'])['values'].mean()
print(g_mean)

# agg() : 여러 집계 함수 사용
print(f'\n agg() 여러 집계 함수 사용')
g_agg = df.groupby('category')['values'].agg(['sum','mean','count'])
print(g_agg)
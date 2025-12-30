import pandas as pd

# 조건을 사용한 값 수정
df = pd.DataFrame({
    '이름':['지홍','지수','지민'],
    '점수':[100,50,66],
    'Pass':[True,False,False]
})
df.loc[df['점수']>60,'Pass']= True
print(df)

# 다중 조건을 사용한 값 수정
df.loc[(df['점수'] >= 60) & (df['이름'] == '지민'), '점수'] = 10
print(df)

# 데이터 통계 및 요약 (count(열 개수), mean(평균), 표준편차(std), 최소값(min)
# 최대값(max) 사분위수
df = pd.DataFrame({'수학':[80,900,95,100,80],
                    '과학':[88,92,85,98,94]})
print(df.describe()) # 요약 통계 확인

# 열별 통계
math_mean = df['수학'].mean()
science_sum = df['과학'].sum()
print(f'수학 평균 : {math_mean}')
print(f'과학 합계 : {science_sum}')

# 병합, 결합
df1 = pd.DataFrame({
    'ID':[1,2,3],
    'Name':['밀탱크','말카우','어피치']
})
df2 = pd.DataFrame({
    'ID':[2,3,4],
    'Score':[99,88,78]
})

'''merge() : 공통 열에 대해 해당 열 기준으로 병합
how : 결합 방식(inner=교집합, outer=합집합, 
left=왼쪽 기준 병합( 오른쪽에 없는 값은 NaN ), right = 오른쪽 기준 병합 ( 왼쪽에 없는 값음 NaN )
on : 기준으로 삼을 열'''
m_df = pd.merge(df1,df2,on='ID',how="inner") # 겹쳐지는 부분이 ID, how 이너조인 = 공통적인 키만 병합(합집합), 아우터 조인
print(m_df)

# concat() : 결합
df1 = pd.DataFrame({
    'ID':[1,2,3],
    'Score':[99,88,78]
})
df2 = pd.DataFrame({
    'ID':[4,5,6],
    'Score':[99,88,78]
})

print('\nconcat() 결합 axis = 0')
# axis = 0 (기본값) : 행 방향 결합
concat_df1 = pd.concat([df1,df2], axis=0)
print(concat_df1)

# axis = 1 : 열 방향 결합
print('\n concat() 결합 axis = 1')
concat_df2 = pd.concat([df1,df2], axis=1)
print(concat_df2)
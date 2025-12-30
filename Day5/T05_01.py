'''
CSV (Comma Seprated Value)
- 값들을 쉼표(,)로  구분
- 가볍고 용량이 작음
- Pandas, Numpy에서 다루기 쉬움
- 서식(색, 굵기 등), 시트 개념 없음

데이터 저장 > CSV 형식으로 저장
pandas.DataFrame.to_csv()
'''

import pandas as pd
data_dict = [
    {'사번':25001,'이름':'김철수','나이':20,'부서':'정보보호부'},
    {'사번':25002,'이름':'이영희','나이':21,'부서':'기술부'},
    {'사번':25003,'이름':'박민수','나이':22,'부서':'생산부'},
    {'사번':25004,'이름':'정수진','나이':20,'부서':'전략본부'},
    {'사번':25005,'이름':'한미래','나이':23,'부서':'개발부'},
]

df = pd.DataFrame(data_dict)
# 데이터 CSV 형식으로 저장 > pandas.DataFrame.to_csv()
df.to_csv('data.csv',index=False,encoding='utf-8-sig')
# index : True(인덱스 포함), False(인덱스 제외)
# encoding : 데이터를 다른 표현 방식으로 변환

# Excel 형식으로 저장 > pandas.DataFrame.to_excel()
# 필요 라이브러리 pip install openpyxl
df.to_excel('data2.xlsx', index=False)

''' JSON(javascript Object Notation) 형식으로 저장
- 웹, API(Application Programming Interface) 데이터 교환에 널리 사용됨
- 파일의 데이터 구조를 표현하는 경량의 데이터 형식
'''

# JSON 형식으로 저장 > pandas.DataFrame.to_json()
df.to_json('data3.json',orient='records',force_ascii=False)



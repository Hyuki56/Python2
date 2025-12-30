# CSV 파일 불러오기 : pandas.read_csv()
import pandas as pd

# df_csv = pd.read_csv('data.csv') # read_csv() 로 불러오면 자동으로 DataFrame 형식으로 가져옴
# print(df_csv.head()) # head() 상위 5개의 내역

# 엑셀 파일 불러오기 : pandas.read_excel()
df_excel = pd.read_excel('data2.xlsx')
print('\n--엑셀 파일 불러오기--')
print(df_excel)

# JSON 파일 불러오기 : json.load()
import json
with open('data3.json','r',encoding='utf-8') as json_file:
    data_json = json.load(json_file)

df_json = pd.DataFrame(data_json)
print('\n\n--JSON파일 불러오기--')
print(df_json.head())

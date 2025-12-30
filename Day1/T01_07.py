# 다른 패키지의 모듈 사용 방법
# import 패키지명.파일명(모듈명)
# from 패키지명.파일명(모듈명) import *

from Section12_Module.EX12_07 import *

fat_calories = calculate_calories(1, 10)
print(f'지방 10g은 {fat_calories}칼로리')

protein_calories = calculate_calories(2, 20)
print(f'단백질 20g은 {protein_calories}칼로리')

carbon_calories = calculate_calories(3, 50)
print(f'탄수화물 50g은 {carbon_calories}칼로리')

other_calories = calculate_calories(10, 10)
print(other_calories)


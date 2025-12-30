# 입력된 영양소 종류와 그램 수를 기반으로 칼로리 계산
FAT = 9
PROTEIN = 4
CARBON = 4

# 1 : 지방, 2 : 단백질, 3 : 탄수화물
def calculate_calories(kind, gram):
    if kind == 1:
        return gram * FAT
    elif kind == 2:
        return gram * PROTEIN
    elif kind == 3:
        return gram * CARBON
    else:
        return "1, 2, 3만 입력하세요^^"
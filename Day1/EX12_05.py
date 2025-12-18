# 길이 단위 변환 모듈

MILES = 0.621371
KILOMETER = 1000

# km -> miles
def kilometer_to_miles(kilometer):
    return kilometer * MILES

# km -> m
def kilometer_to_meter(kilometer):
    return kilometer / KILOMETER

# m -> km
def meter_to_kilometer(meter):
    return meter * KILOMETER

# m -> miles
def meter_to_miles(meter):
    return meter * KILOMETER * MILES

# miles -> km
def miles_to_kilometer(miles):
    return miles/MILES

# miles -> m
def miles_to_meter(miles):
    return miles/MILES/KILOMETER
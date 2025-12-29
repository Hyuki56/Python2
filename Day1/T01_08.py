from Converter.Length_Converter import *
from Converter.Time_Converter import *

kilometer = 700
meter = 30
miles = 310.6855

hours = 6
mins = 25

mins_from_hours = hour_to_min(7)
print(f'7시간은 {mins_from_hours}분')

sec_from_min = min_to_sec(mins)
print(f'{mins}분은 {sec_from_min}초')
print()

miles_from_kilometer = kilometer_to_miles(kilometer)
print(f'{kilometer}km는 {miles_from_kilometer}마일')

kilometer_from_meter = meter_to_kilometer(meter)
print(f'{meter}m는 {kilometer_from_meter}km')

kilomter_from_miles = miles_to_kilometer(miles)
print(f'{miles}마일은 {kilomter_from_miles}km')
from EX12_05 import *

kilometer = 500
meter = 50
miles = 310.6855

miles_from_kilometer = kilometer_to_miles(kilometer)
print(f'{kilometer}km는 {miles_from_kilometer}miles')

kilometer_from_meter = meter_to_kilometer(meter)
print(f'{meter}m는 {kilometer_from_meter}km')

kilometer_from_miles = miles_to_kilometer(miles)
print(f'{miles}마일은 {kilometer_from_miles}km')
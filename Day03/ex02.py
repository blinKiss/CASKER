# 모듈을 import 하는 방법

# import 모듈
import converter
# import 모듈 as 별칭
import converter as cvt
# 파일이름(모듈).함수()
m1 = converter.kilometer_to_miles(1000)
print(m1)

# 별칭.함수()
m2 = cvt.kilometer_to_miles(100)
print(m2)

# 파일(모듈) 내부의 함수를 포함
# from converter import kilometer_to_miles
# from converter import gram_to_pound
# from converter import kilometer_to_miles

# converter 모듈 안의 모든 함수를 포함
# * : 모든 항목
# from converter import *
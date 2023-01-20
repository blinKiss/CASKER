'''
    표준 모듈
    1. math     : 수학 연산관련 모듈
    2. random   : 랜덤 수 생성 모듈
    3. time     : 시간 처리 모듈
    4. datetime : 날짜/시간 처리 모듈
'''
import math

# pi 원주율
print('PI : {}'.format(math.pi))

# ceil() 올림
print('1.1의 올림 : {}'.format(math.ceil(1.1)))

# floor() 내림
print('1.9의 내림 : {}'.format(math.floor(1.9)))

# round() 반올림 - Math 모듈 외 기본 내장함수 math 안씀
# 파이썬의 반올림 함수는 ex 올림 내림 차이가 동일한 경우 짝수값으로 반올림 ex) 1.5 = 2, 2.5 = 2 // .5면 짝수로 반환
# 인자를 따로 지정해주지 않으면 소수 첫째자리에서 반올림 ex) 3.7 = 4
# round(a,b) = a는 값, b는 소수 몇째자리까지 나타낼 것인지 기본 0이고, 1이면 소수 둘째자리에서 반올림하여 첫째자리까지 반환  ex) 2.56, 1 = 2.6
print('2.6의 소수점 첫째자리 반올림 : {}'.format(round(2.6)))
print('2.56의 소수점 둘째자리 반올림하여 첫째자리 까지만 표시 :{}'.format(round(2.56, 1)))

# trunc() 절삭 (특정 자리수 이하를 제거)
print('1.9의 절삭 : {}'.format(math.trunc(1.9)))

# sqrt() 제곱근
print('9의 제곱 : {}'.format(math.sqrt(9)))

# pow(a,b) a의 b제곱
print('3의 2제곱 : {}'.format(math.pow(3, 2)))

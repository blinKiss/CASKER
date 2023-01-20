from secure import *
# 사용자 정보를 마스킹하기

name = '김휴먼'
cn = '800422-1234567'
phone = '010-1234-5678'

print(name)
print(cn)
print(phone)
print()


print(secure_name(name))
print(secure_cn(cn))
print(secure_phone(phone))
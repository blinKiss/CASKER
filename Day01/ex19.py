# 논리 연산자
# and   : A and B 와 같은 조건에서,
#         A 와 B 모두 True면, 결과가 True이다
# 쇼트서킷
# A and B : A 가 False면 B 는 검사하지 않는다

# or    : A or B 와 같은 조건에서
#         A 와 B 둘 중 하나의 조건이라도 True면, 결과가 True이다
# 쇼트서킷
# A or B : A 가 True면 B 는 검사하지 않는다 

# not   : True면 False로, False면 True로 변경한다
a = 10
b = 5

print('{} > 7 and {} > 7 : {}'.format(a, b, a > 7 and b > 7))
print('{} > 7 or {} > 7 : {}'.format(a, b, a > 7 or b > 7))

print('not : {} : {}'.format(a, not a)) # 0 이외의 정수는 True, 0 은 False
print('not : {} : {}'.format(0, not 0))




name = input('이름 : ')
age = input('나이 : ')

# 기본 출력
print('이름 : ', name, sep='')
print('나이 : ', age, sep='')

# 형식 문자열 - format
print('이름 : {}'.format(name))
print('나이 : {}'.format(age))

# f-strings
print(f'이름 : {name}')
print(f'나이 : {age}')
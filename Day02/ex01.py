# 파이썬 제어문
# 제어문
# 1. 조건문
#  - 조건에 따라 프로그램의 실행흐름을 변경하는 키워드
# 2. 반복문
# - 조건에 따라 실행문을 반복 실행하는 문장

# 조건문
# if
#   if 조건식 : 
#   (들여쓰기) 조건식의 결과가 참일 때 실행문

# * 들여쓰기
# 1. 공백(띄어쓰기)나 탭(tab)을 통해서 들여쓰기를 수행
# 2. 공백의 개수는 상관없음(일반적으로 4개 또는 2개)
# 3. 탭은 1개만 사용해야한다
# 4. 같은 영역은 들여쓰기를 통일해야한다

age = input("당신은 몇 살 입니까?")
age = int(age)

# 숫자형으로 연산하기 위해서는 형 변환을 해야한다
if age >= 20:
    print('성인입니다')
    print('나이 : {}'.format(age))
else:
    print('청소년 입니다')
    print('나이 : {}'.format(age))
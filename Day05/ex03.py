'''
    예외 처리
    
    예외 (exception)?
    : 프로그램 실행 중 예상치 못하게 발생한 오류
    - 예외 발생 시, 프로그램 진행 중단
    - 예외 발생 가능성이 있는 문장을 파악하여 대응 가능
    
    ex)
    - 숫자를 0으로 나누는 경우
    - 접근할 수 없는 index에 접근하는 경우 
'''

# 숫자를 0으로 나누는 경우

print('X / Y')
X = int(input('X : '))
Y = int(input('Y : '))

'''
    예외처리문
    
    try:
        예외 발생 가능성 문장
    except 예외 클래스:
        예외 발생 시 처리할 문장
    else:
        예외 발생
'''
try:
    result = X / Y
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
else:
    print(result)

'''
    자주 보게 되는 예외 클래스들
    - SyntaxError
    - TypeError
    - IndexError
    - NameError
    - KeyError
    - ...
'''




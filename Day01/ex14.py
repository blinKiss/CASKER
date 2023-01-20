# f-strings 형식 문자열
# f'{변수명}' 형식으로 문자열 안에 표현식을 바로 사용하여 출력한다.

from datetime import *

time = datetime.today().year
age = datetime.today().year - 1987 + 1

print(f'{time}년엔 {age}살이 됩니다')
print(f'{time+1}년엔 {age+1}살이 됩니다')
print(f'{datetime.today().year+2}년엔 {age+2}살이 됩니다')
print(f'{time+3}년엔 {age+3}살이 됩니다')

print(type(f'{time+3}년엔 {age+3}살이 됩니다'))
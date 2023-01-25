# finally문
# 예외 처리문에서 예외 발생 여부와 관련없이 실행되는 블록

try:
    file = open('nofile.txt', 'r')
    line = file.readline()
except IOError:
    print('파일 입출력 시, 예외가 발생하였습니다')
else:
    print(line)
finally:
    file.close()    # 파일 메모리 자원 해제
'''
    파일 입출력
    
    - 텍스트틀 파일 생성하기
'''


# 파일 저장 경로
path = 'C:/Users/denim/git/CASKER/Day03/'

# at : 추가모드 + 텍스트모드
file = open(path + 'hello.txt', 'at', encoding='UTF-8')


# 파일 내에서 출력 : write()
file.write('\n')
file.write('이어서 내용을 추가합니다')
file.write('\n')
file.write('텍스트 파일 내용 추가 모드 : at')
print('파일에 새로운 내용을 추가하였습니다')


# 파일 닫기
file.close()
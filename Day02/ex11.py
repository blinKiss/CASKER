# 딕셔너리 반복하기

eng_dict = {
    'coffee'    : '커피',
    'human'     : '휴먼',
    'star'      : '별',
    'space'     : '우주',
}


for word in eng_dict:
    print('{}는 한글로? \t: {}'.format(word, eng_dict.get(word) ))
    
# 딕셔너리.get(key) : key에 해당하는 값을 가져오는 함수
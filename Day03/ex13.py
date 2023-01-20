'''
    CSV (Comma Separated Value)
    : 콤마(,) 분리한 값들
    
    
    ex)
        등번호,이름,주소,전화번호
        7,송태섭,서울시 종로구,010-1111-2222
        10,강백호,서울시 마포구,011-1234-5678
        4,채치수,서울시 용산구,016-0987-6543
        11,서태웅,서울시 송파구,017-4837-1213
        14,정대만,서울시 광진구,019-5783-9845
'''

import csv

path = path = 'C:/Users/denim/git/CASKER/Day03/'
file = path + 'test.csv'

# open(파일경로, 모드, 옵션)
with open(file, 'w', newline='', encoding='UTF-8') as file:
    # delimiter : 구분기호
    # writer(파일객체, delimiter="구분기호")
    # : 파일을 작성하는 기능을 가진 writer 객체를 반환
    csv_maker = csv.writer(file, delimiter=',')
    
    # writer 객체가 가진 기능 : writerow()
    # : 파일객체에 한 줄씩 데이터를 작성하는 함수
    csv_maker.writerow(['등번호','이름','주소','전화번호'])
    csv_maker.writerow([4,'채치수','서울시 용산구','016-0987-6543'])
    csv_maker.writerow([7,'송태섭','서울시 종로구','010-1111-2222'])
    csv_maker.writerow([10,'강백호','서울시 마포구','010-1234-5678'])
    csv_maker.writerow([11,'서태웅','서울시 송파구','017-4837-1213'])
    csv_maker.writerow([14,'정대만','서울시 광진구','019-5783-9845'])

    
print('파일 생성 완료')
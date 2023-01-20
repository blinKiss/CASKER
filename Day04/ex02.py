'''
- 클래스 선언
    
    class 클래스명:
        클래스 내용
        
    # 생성자
    : 객체가 생성될 때, 실행되는 메소드
    def __init__(self, 매개변수):
        생성자 내용
        
    # self : 객체 자신을 가리키는 키워드(딕셔너리)
    # self.(변수), self.(메소드)
    
    # 소멸자
    : 객체가 소멸될 때, 실행되는 메소드
    def __del__(self):
        소멸자 내용
        
    # 메소드
    # : 클래스가 정의된 함수
    def 메소드명(self, 매개변수):
        메소드 내용
'''

'''
    # 객체 생성
    # 객체 변수명 = 클래스명()    # 클래스명() --> 생성자 함수
    # 인스턴스 : 클래스를 통하여 생성된 객체
'''

class Person:
    
    # 생성자
    # 파이썬 생성자는 여러개 정의할 수 없다(오버로딩x)
    # def __init__(self):
    #    print('Person 객체 생성...')
        
    # 생성자
    # - 정의한 생성자의 매개변수에 디폴트 매개변수를 설정하여 오버로딩을 구현한다
    def __init__(self=None, name=None, age=None, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성...')
        
    # 소멸자
    def __del__(self):
        print('Person 객체 소멸...')
        
    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'.format(self.name, self.age, self.tel))
    
# Person 객체 생성
person = Person()

# 객체의 변수 접근
person.name = '은구슬'
person.age = 20
person.tel = '011-5329-1104'

print('이름 : ', person.name)
print('나이 : ', person.age)
print('전화번호 : ', person.tel)

person2 = Person('유지민', 15, '011-2775-0426')
print( person2.name)
print( person2.age)
print( person2.tel)

person3 = Person('김혜미', 18, '010-****-0707')
person3.show_info()
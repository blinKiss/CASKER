class Student:
    
    def __init__(self, no, name, major):
        self.no = no
        self.name = name
        self.major = major
        
    # 특수한 이름의 메소드
    # __(이름)__ 형태로 특수한 이름의 메소드들이 있다
    # : 미리 정의된 이름이며, 특수한 상황에서 호출되도록 정의되어있다

    # __str__ : str() 함수를 호출할 때, 자동으로 호출
    def __str__(self):
        return '{} / {} / {}'.format(self.no, self.name, self.major)
    
    # 객체의 정보가 같은지 확인
    def __eq__(self, obj):
        return self.major == obj.major
    
    def __ne__(self, obj):
        return self.major != obj.major
    
    
# 객체 리스트
students = [
            Student(107, '김연화', '도예과'),
            Student(101, '박민희', '교육학과'),
            Student(104, '이은영', '영문과'),
            Student(109, '이진희', '교육학과')
           ]

for student in students:
    # str(객체) : 해당 객체의 __str__ 메소드를 호출하는 메소드
    print( str(student))
    

# == 기호를 이용하여 두 객체를 비교하면,
# 해당 객체의 __eq__ 메소드가 호출된다
print( students[1] == students[2])
print( students[1] == students[3])

# != 기호를 이용하여 두 객체를 비교하면,
# 해당 객체의 __ne__ 메소드가 호출된다
print( students[1] != students[2])
print( students[1] != students[3])
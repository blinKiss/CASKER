# getter, setter
# - getter : 변수를 가져오는 메소드
# - setter : 변수의 값을 지정하는 메소드


class Person:
    
    # getter
    def get_name(self):
        return self.name
    
    # setter
    def set_name(self, value):
        self.name = value
        

p = Person()

p.set_name('권진아')
print('p - name : {}'.format(p.get_name()))
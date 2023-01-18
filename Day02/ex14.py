'''
시퀀스 내장 함수

1. enumerate() 함수
    : 리스트와 함께 사용하여,
    (index, 요소) 형태로 튜플로 반환하는 함수
    
    ex) for item in enumerate( ['a','b','c'])
        print(item)
        (결과)
        (0, 'a')
        (1, 'b')
        (2, 'c')


2. range() 함수
    : 전달받은 값에 따라서 특정 범위에 데이터를 반환하는 함수

    i) range(끝)        
    : 0부터 (끝-1)에 지정하는 번호까지 정수를 생성
    
    ii) range(시작, 끝)
    : 시작과 끝(5-1) 사이에 모든 정수를 생성

    iii) range(시작, 끝, 단계)
    : 시작부터 (끝-1) 사이에 수들을 단계의 크기만큼 증감하여 생성
    

3. len() 함수
    : 함수에 전달된 객체의 길이(개수) 반환하는 함수
    ex) li = [1,2,3,4]
        len[li] --> 4
       
   
4. sorted() 함수
    : 반복가능한 객체를 오름차순으로 정렬한 결과를 반환하는 함수
    ex) li = [10,3,9,2,5]
        sorted(li) --> [2,3,5,9,10]        


5. zip() 함수
    : 여러개의 반복가능한 객체들을 요소끼리 묶어서 반환하는 함수
    ex) names = [ 'C', 'JAVA' 'PYTHON']
        scroes = [ 100, 90, 80 ] 
        zip( names, scores)
        --> ('C', 100),
            ('JAVA', 90),
            ('PYTHON', 80)

'''

# C언어, 파이썬, 자바
# 0, 1, 2
# enumerate(prog)
'''
(0, 'C언어')
(1, '파이썬')
(2, '자바')
'''

prog = ['C언어', '파이썬', '자바']
for item in enumerate(prog):
    print(item)
    
# range(10) : 0 1 2 ~ 9
for i in range(10):
    print(i, end=' ')

print()

# range(1,11) : 1 2 3 ~ 10
for i in range(1,11):
    print(i, end=' ')

print()

# range(1, 20, 2) - range(시작, 끝, 증감치) 1~19 까지 홀수
print('1부터 20까지의 숫자 중 홀수만 출력 : ', end='')
for i in range(1, 20, 2):
    print(i, end=' ')
    
print()

# range(2, 21, 2) - 2~20까지 짝수
print('1부터 20까지의 숫자 중 짝수만 출력 : ', end='')
for i in range(2, 21, 2):
    print(i, end=' ')
    
print()    

# len
li = ['월', '화', '수', '목', '금', '토', '일']
print(li)
print('li의 요소의 개수 : {}'.format(len(li)))

# sorted
# sorted(리스트, reverse=True) : 내림차순
# sorted(리스트, reverse=False) : 오름차순

scores = [100, 90, 65, 80, 70]
print(scores)
print(sorted(scores))
print('내림차순 :', sorted(scores, reverse=True))
# print('오름차순 : ', sorted(scores, reverse=False))

# sort
# - 해당 리스트를 정렬하여 갱신하는 함수
# 리스트.sort(reverse=True) : 내림차순
# 리스트.sort(reverse=False) : 오름차순
# scores.sort(reverse=True)
# print('내림차순 : ', scores )
scores.sort(reverse=False)
print('오름차순 :', scores )


# zip
names = ['s1','s2','s3','s4','s5']

for student in zip(names, scores):
    print(student)
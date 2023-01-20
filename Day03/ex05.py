# random
import random

# random() : 0.0xxx ~ 0.9xxx 임의의 실수
print('0.0000 ~ 0.9999 까지의 실수 중 임의의 수 : {}'.format(random.random()))

# randint(a, b) : a이상 b이하의 임의의 정수
print('1이상 10이하의 정수 중 임의의 수 : {}'.format(random.randint(1, 10)))

# randrange(a, b, c) : a이상 b미만 c만큼 증가하는 임의의 정수
print('1부터 10까지 2씩 증가하는 정수 중 임의의 수 : {}'.format(random.randrange(1, 10, 2)))


# choice(A) : 시퀀스 자료형에 속한 요소 중 임의의 요소를 반환하는 함수
seasons = ['봄', '여름', '가을', '겨울']
print('내가 좋아하는 계절은 {}입니다'.format(random.choice(seasons)))

# sample(A, N) : 시퀀스 자료형에 속한 요소 중 지정한 개수의 요소를 임의로 반환하는 함수
#                A 중의 N 개의 임의의 요소
lotto = range(1, 46) # 1~45 정수 생성
print('이번 주 당첨 번호는 {}'.format(random.sample(lotto, 6)))

# shuffle(A) : 시퀀스 자료형에 속한 요소들의 순서를 임의로 섞는 함수
#              A 에 속한 요소들의 순서를 섞는다
trump = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
random.shuffle(trump)

print('카드를 섞은 결과는? : {}'.format(trump))
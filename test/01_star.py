
'''
별찍기
# N : 5

*
**
***
****
*****

'''
N = input('N : ')
N = int(N)
print()
for i in range(0, N):
    for j in range(0, i+1):
        print('*', end='')
    print()
    
'''
N : 5
    *
   ***
  *****
 *******
*********
'''


for i in range(0, N):
    for j in range(1, N-i):
        print(' ', end='')
    for k in range(0, i*2+1):
        print('*', end='')
    print()
    
# 선생님 답
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(' ', end='')
#     for k in range(1, i*2):
#         print('*', end='')
#     print()
p.144 리스트 내포(list comprehensive)
(java)배열 <---> (python)리스트

a = [1, 2, 3, 4]
# 리스트 타입, 원소가 x, 빈(empty)\
result = []
# print(type(a))
# 출력값 : class 'list'
# print(len('안녕하세요'))


for i in a:
    print(i)
    #반복할 목록 a들이 한 번씩 순회하며 i로 들어간다. 그 안에서 원소 갯수만큼 반복.

'''
for num in a:
    result.append(num*3)
print('result : ', result)
'''
# print(a*3) 하면 1,2,3,4,1,2,3,4,1,2,3,4,
# result.append(num3)하면 3,6,9,12

a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)
# 출력값: 3, 6, 9, 12 같은 값 뽑아내는 다른 방법

random_list = []
# .append() : 배열에 값을 추가하는 명령어
# 반복문을 다룰 줄 안다 : while, for
for i in range(10):
    print(i)
#1에서 10까지. 10에서 -1한 만큼 반복해 뽑아낸다

# 랜덤모듈(난수발생) - 파이참, 가상환경 (venv) 설정되어있기 때문에 가능. 파이썬 셋팅할 때 되어있음

import random
random_list = []
for i in range(10):
        random_list.append(random.randint(1,10))

print(random_list)
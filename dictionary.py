# 리스트 < 튜플 : 튜플의 속도가 더 빠르다
# 리스트, 튜플, 딕셔너리, 셋
# list, tuple, dict
# p.72 / 85/ 88/ 97
# 리스트 vs 튜플 : 수정이 가능 vs 수정 불가능
# 튜플의 선언
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1, type(t1)) # 출력값: () <class 'tuple')
print(t2)           # 출력값: (1,2)
print(t3)           # 출력값: (1,2,3)
print(t4, type(t4)) # 출력값: (1,2,3) <class 'tuple'>
print(t5)           # 출력값: ('a', 'b', ('ab', 'cd'))

# 튜플의 값을 수정, 삭제할 때 (p. 86)
t6 = (1, 2, 'a', 'b')
# t1[0] = 99 # 오류가 뜬다.
# del t6[0] ??????

t7 = list(t6)
t7[0] = 99
print(t7)

# 튜플 자체로 수정할 수 없고 리스트 형태로 바꿔야만 수정 가능함
# 튜플 --> 리스트 변경 --> 원소를 조작 -->튜플

# del t1[0]
# 튜플은 수정도 되지 않고 삭제도 되지 않는다.
# t2 = list(t1)
# #t2[0] = 99
# print(t2)

# 튜플 인덱싱 vs 리스트 인덱싱
# print(t3[5) #데이터 없는데 접근하라고 했기 때문에 오류 뜬다
list1 = [1, 3, 5, 7, 9]
print(list1[0])
# 출력값: 1

# list1 = [1, 3, 5, 7, 9]
# print(list1[9])
# 출력값: 9번째는 없기에 오류 뜬다 list index out of range

# 튜플 슬라이싱
print(t3[0:2]) #출력값: (1, 2)

print ("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
# 튜플 연산
print(t3+t5) # 출력값: (1, 2, 3, 'a', 'b', ('ab', 'cd'))
print(t3 * 3) # 출력값: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 글자 수
print('튜플 t5 길이 : ',len(t5)) # 출력값: 튜플 t5 길이 :  3

# 리스트 < 튜플 : 튜플의 속도가 더 빠르다

# 반복문
# 리스트 : 비어있는 리스트에 넣을 수 있었음. append 이용.
# 튜플 : 빈 걸로 만들면 수정할 수 없기에 넣을 수 없음.
empty=[]
for i in range(10):
    empty.append(i)

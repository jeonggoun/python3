# p. 72 리스트 자료형
# 배열(array) - 시퀀스
# 빈 리스트 <--- mutable 변경 가능한 데이터 타입
a = []
b = [1, 2, 3, 'AA', 'BB', ['Life', 'is', 'egg']]
#list() - 리스트 타입으로 캐스팅(casting) <--> 형변환

# 1. 인덱싱(index) - 값을 가리키는
# index 0 1 2 3 4
str1 = '안녕하세요'
print(str1[0])
# 출력값 : 안
print(str1[1])
# 출력값 : 녕
print(b[5][0])
# 출력값 : Life
# print(b[5][0] + b[0])
# 문자+숫자 같이 출력하려 하니 오류가 난다. formatting 필요. (ex) print(b[5][0] + b[0]) + str()

# 1. 인덱싱(index) - 값을 가리키는 방법, 음수인덱스(-1, -2,...)
print(b[-1])
# 출력값 : ['Life', 'is', 'egg']

# 멤버쉽 테스트 : in, not in <-> True, False
print('안' in str1)
# 출력값 : True
print('AA' in b)
# 출력값 : True

# 2. 슬라이싱 (p. 75) : .slice() <-> [시작:끝값:단계]
a = [1, 2, 3, 4, 5]
# >>> : 명령 프롬프트 (CLI)
print(a[0:2])
# 출력값 : [1, 2]
# 뒤에 있는 인덱스 번호는 포함되지 않는다
print(a[2:])
# 출력값 : [3, 4, 5] 콜론 뒤의 값을 생략할 수 있다.

b = [4, 5, 6]
print(a+b)
# 출력값 : [1, 2, 3, 4, 5, 4, 5, 6]
print(b*3)
# 출력값 : [4, 5, 6, 4, 5, 6, 4, 5, 6]
print(len(b))
# 출력값 : 3 원소(요소)

# 반복문
empty_list = []
for i in range(10):
    empty_list.append(i)
print(empty_list)
# 0에서 9까지 10번 반복. 그리고 값을 i에 대입
# 출력값 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# random 모듈을 불러올 수도 있음.

empty_list = []
for i in range(10):
    empty_list.append(i**2)
print(empty_list)
# 출력값 : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 리스트의 수정
empty_list[0]='감'
empty_list[-1]=100
print('----------수정된 리스트의 값----------')
print(empty_list)

'''
출력값
----------수정된 리스트의 값----------
['감', 1, 4, 9, 16, 25, 36, 49, 64, 100]
'''
# 값이 없는 index에 접근하려 하면 오류가 뜬다

'''
리스트의 삭제
1. del          <-- (인덱스) 값 제거
2. .remove()    <-- 값 제거 
3. .pop()       <-- 마지막 원소를 제거, 기존 리스트를 반환
4. clear()      <-- 완전히 비워내는
'''

#리스트에 요소(element)를 추가하는 명령???????????????
empty_list = []
for i in range(10):
    empty_list.append(i)
print(empty_list)

del empty_list[9]
print('----------변경된 리스트의 값----------')
print(empty_list)
'''
출력값
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
----------변경된 리스트의 값----------
[0, 1, 2, 3, 4, 5, 6, 7, 8]
'''

'''
# 리스트의 삭제
2. .remove()    <-- 값 제거  
※ 첫번째로 나오는 값
'''


empty_list = []
for i in range(10):
    empty_list.append(i % 2)
print(empty_list)
# 출력값 : [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# empty_list.remove(1)
# print(empty_list)
# 출력값 : [0, 0, 1, 0, 1, 0, 1, 0, 1] 1 하나가 사라짐

'''
리스트의 삭제
3. .pop() <- 마지막 원소를 제거, 기존 리스트를 반환 (p.83)
리스트의 맨 마지막 요소를 돌려주고, 그 요소는 삭제한다.
.pop(x) : x번째 요소를 돌려주고 그 요소는 삭제한다.
'''
empty_list = []
for i in range(10):
    empty_list.append(i % 2)
print(empty_list)
# 출력값 : [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
empty_list.pop()
print(empty_list)
# 출력값 : [0, 1, 0, 1, 0, 1, 0, 1, 0]



empty_list = []
for i in range(10):
    empty_list.append(i % 2)
print(empty_list)
# 출력값 : [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# empty_list.pop(2)
# print(empty_list)
# # 출력값 : [0, 1, 1, 0, 1, 0, 1, 0, 1]


print('리스트 요소의 합 : ',sum(empty_list))
# 출력값 : 5

# sum이 없었다면
print(empty_list)
total = 0
for number in empty_list:
    total += number
print('리스트 요소의 합 : ', total)
# 출력값 : 리스트 요소의 합 :  5

'''
리스트 관련 함수
.1. sum() : 리스트 내의 합(sum)
2. .sort() : 순차정렬
3. .reversed() : 역순정렬
4. .index() : 인덱스번호
5. .appen() : 리스트의 요소를 (리스트 끝) 추가(1)
6. extend() : 여러개의 요소값을 추가(2)
7. .insert(인덱스, 값) : (원하는 인덱스 위치에) 요소를 추가(3)
8. .coumd() : 요소의 갯수
'''

#git으로 파일 버전관리 시작!!

empty_list = []
for i in range(10):
    empty_list.append(i**2)
print(empty_list)
# 출력값 : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 1. sum() : 리스트 내의 합(sum)
print('합 : ',sum(empty_list))
# 출력값 : 합 :  285

# 3. .reversed() : 역순정렬
print('-역순정렬-')
print(empty_list[::-1])
# 슬라이싱 기능으로 역순 정렬하는 방법
# 출력값 : [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
empty_list.reverse()
print(empty_list)
# reverse 이용해 역순 정렬하는 방법
# 출력값 : [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]

# 4. .index() : 인덱스번호
print(empty_list.index(36))
# 몇 번째 인덱스에 있는지 숫자로 알려줌
# 출력값 : 3

# 5. .append() : 리스트의 요소를 (리스트 끝) 추가(1)
empty_list.append(99)
print(empty_list)
# 출력값 : [81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 99]

# 7. .insert(인덱스, 값) : (원하는 인덱스 위치에) 요소를 추가(3)
empty_list.insert(0,109)
print(empty_list)
# 출력값 : [109, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 99]

# 6. extend() : 여러개의 요소값을 추가(2)
empty_list.extend(['A', 'B', 'C'])
print(empty_list)
# 출력값 : [109, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 99, 'A', 'B', 'C']

# 리스트의 삭제. 완전히 비어낸다.
empty_list.clear()
print(empty_list)
# 안에 있는 항목들을 삭제했다
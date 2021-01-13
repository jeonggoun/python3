# 딕셔너리 자료형 (p.88)
# 리스트 == 배열 [,]
# 튜플 - 값의 수정(삭제, 변경) (,)
# 딕셔너리 = 객체 (키:값) {,}

# 홍길동, 생일 1월 13일, 성별 남자, 키, 시력
person = ['홍길동', '0113', '남', 175, 1.0, 1.5]
# 이렇게 보면 값을 유추하기 어려움

# 빈 딕셔너리 생성
person1 = {}
person1['id']='abcd1234'
person1['nick']='big apple'
person1['level']=99
person1['hp']=1000
person1['mp']=50
print(person1) # 출력값: {'id': 'abcd1234', 'nick': 'big apple', 'level': 99, 'hp': 1000, 'mp': 50}
# 불편한 방법이기는 함

# 딕셔너리, 초기화
person2 = {
    'name': '홍길동',
    'birth': '0113',
    'gender': '남',
    'height': 175,
}
# 왼쪽이 key 오른쪽이 value

# 반복문
for property in person1:
    print(property, ':', person1[property])

'''
↓출력값↓

id : abcd1234
nick : big apple
level : 99
hp : 1000
mp : 50
'''
# p. 102 불 자료형

# 불, 불리언 / bool, boolean

# True, False 값이 딱 두가지. 참, 거짓.

# 명시적인 표현
is_true = True # <---- true
is_false = False # <-- false
# 다른 언어에서는 소문자로 true, false로 많이 사용

# 비교 연산자 : >, >=, <, <=, ==, !=
# 논리 연산자 : and, or, not
print(4 > 5)
print(type(is_true))
print(1==1)
print(1 is 1)

'''
 p.103 자료형의 참과 거짓 (표)
 불린 값 True : 명령 실행
 불린 값 False : 명령 실행하지 않음
 '' or "" - 공백 문자
 [],(),{} - 리스트, 튜플, 딕셔너리 (=원소나 값이 없는 상태) false로 판단
 None, 0 = false로 판단
 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있을 때("",[],(),{})는 거짓.
'''

# p.104
a = [1, 2, 3, 4]
print(type(a))
# 인덱싱, 슬라이싱 사용할 수 있다.
'''
while a:
    print(a) 반복해 수행하기 때문에 다운될 수 있음..
'''
# 변수=초깃값
# while 조건문(식):
#   수행할 문장(코드)
#   변수의 증감식

'''
while True:
    print('안녕하세요')
'''
"""
while 4 < 5:
    print('안녕하세요')
"""

# 멤버쉽테스트.
# 문자열에서도 연산자 확인할 수 있다.
print("안" in "안녕하세요")
print("안" not in "안녕하세요")


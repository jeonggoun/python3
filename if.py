# p.117 if 조건문
'''
타 프로그래밍 언어 vs      파이썬
------------------------------------
if(조건식) {         if 조건실:
...실행코드...          ...실행코드...
}
if(조건식 {          if 조건식:
...
}else{
....
}
'''
'''
money = True
if money:
    print('택시를 타고 간다')
else:
    print('걸어 간다.'),
'''

# p.121 비교 연산자 사용한 조건문
# >, <, >=, <=, ==, !=
if 4>3:
    print('4는 3보다 크다')
else:
    print('4는 3보다 크지 않다')
# true이므로 '4는 3보다 크다' 출력
if 5>4>3:
    print('4는 3보다 크고 5보다 작다')
else:
    print('4는 3보다 크지 ..않다')

'''
사용자에게 숫자를 하나 입력받고, 이 숫자가 홀수/짝수 여부를 판단하고 내용을 출력하는 조건문을 작성해봅시다.
'''
# input_num = input('숫자를 하나 입력하세요') - 문자열로 값을 변환
# int() : 숫자형으로 변화 (casting, 캐스팅 - 형 변환)
# 홀수 : 1,3,5,7,.... 2로 나눈 나머지 값이 1
# 짝수 : 2,4,6,7,.... 2로 나눈 나머지 값이 0
'''
input_num = input('숫자를 하나 입력해 보세요') #값을 문자열로 받는다
input_num = int(input_num) #숫자로 변환
if input_num % 2 == 0:
    print(f'입력한 숫자 {input_num}은 짝수입니다')
else:
    print(f'입력한 숫자 {input_num}은 홀수입니다')
# 나머지라는 연산자 : %
'''
# p.125 조건문에서 아무 일도 하지 않게 설정하고 싶다면 if... pass > 코드 미완성일 때 쓸 수 있음


'''
input_num2 = input('숫자를 입력하세요')
print(input_num2, type(input_num2))
# string, 문자열이라고 뜬다
'''


input_num2 = input('숫자를 입력하세요')
last_char = input_num2[-1]
# 가장 끝자리 -1 가져옴. string
print(last_char)

if last_char in '02468':
    print('짝수를 입력했습니다.')
else:
    print('홀수를 입력했습니다.')

# 굳이 문자형에서 숫자형으로 변환하지 않아도 파이썬이 알아서 처리
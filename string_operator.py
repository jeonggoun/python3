# p.49 문자열도 연결할 수 있는 연산자가 있다.
'''
숫자연산자 : +, -, *, /, %, **, //
문자연산자 : + (연결)
'''
head = "Python"
tail = " is fun!"
print(head+tail)

# 문자열 연산자 : * (횟수반복)
a = "python"
print('='*50)
print(a*10)
print(10*a)
# 앞에 써도 뒤에 써도 상관X

# len() : 문자열의 길이를 구하는 함수
# p. 51
# 인덱싱 : 몇 번째 문자(열)을 가리키는 것
# python : 갯수 6개
# 012345
print(len(head))
print(head[0])
print(head[1])
print(head[2])
print(head[3])
print(head[4])
print(head[5])
# 0부터 시작하기 때문에 갯수-1개만큼 값을 갖게 된다
# print() 줄바꿈이 있다.
# end="" end 옵션을 붙이면 붙여서 출력된다
print(head[0], end="")
print(head[1], end="")
print(head[2], end="")
print(head[3], end="")
print(head[4], end="")
print(head[5])

# p.53 / 슬라이싱 : 잘라내는 것

string_a = "Life is too short, you need Python"
string_b = "LIFE IS TOO SHORT, YOU NEED PYTHON"
# upper(), lower()
print(string_a.upper())
# upper 데이터를 대문자로 변환해서 출력
print(string_b.lower())

string_c = string_a[0]+string_a[1]+string_a[2]+string_a[3]
print(string_c)

# 대괄호 사용하면 더 쉽게 출력
print(string_a[0:4])
# 마지막 수의 -1 만큼만 포함된다. 0부터 시작되기 때문

# python만 출력한다면?

# [시작:끝(포함x)]
# 뒤부터 출력하고 싶으면 음수 사용
# [시작:끝:단계]
print(string_a[0:])
print(string_a[28:])
print(string_a[-6:-1])
print(string_a[-6])
print(string_a[0:34:3])

# in - 멤버쉽 테스트
# 문자열 내부에 어떤 문자열이 있는지 테스트
message_text = "안녕하세요, 파이썬"
print('파이썬' in message_text)
print('python' in message_text)

msg_text = 'hello python'
print('python' in msg_text)
# Boolean, Bool , 불(부울)
print(5<7)
print(10 == '10')

# if만 이용해서 홀수, 짝수

input_num = input('숫자를 입력하세요')
last_char = input_num[-1]
if last_char in '02468':
    print('입력한 숫자는 짝수입니다')

if last_char in '13579':
    print('입력한 숫자는 홀수입니다')

# 이렇게도 사용 가능. 잘 사용하지는 않지만
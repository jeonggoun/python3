# p.130 while 반복문
# 제어문 > 반복문 > while, for (다른 언어 do while 있음)

'''
while 조건문:
    반복 수행할 문장1
    반복 수행할 문장2
    .....문장.....
    증감식
'''

# 변수 --> 의미있는 단어 (키워드x) 조합
'''
i = 1
while i <= 10:
    print(f"안녕하세요, {i}번째 고객님")
    i += 1
'''
'''
i = 1
num_sum = 0
while i <= 100:
    num_sum += i
    print(i)
    i += 1
print("1~100까지 숫자의 총합 : ",num_sum)
# 거짓이 되면 끝나는 것. 증감식이 빠지게 되면 계속 출력된다.
'''

# 구구단
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...계속...
2 x 9 = 18
'''

# Q. 구구단의 합을 구하여, 반복문 끝나면 출력해 보세요!

j = 1
dan = int(input('몇 단을 알고 싶으신가요?'))
dan_sum = 0

while j<10:
    dan_sum += dan*j
    print(f'{dan} x {j} = {dan*j}')
    j += 1 # j = j+ 1

print(f'{dan}단의 합 : {dan_sum}')

# p. 137 무한 루프. 반복문 사용할 때 주의
# p. 138 
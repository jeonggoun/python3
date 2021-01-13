# p.138 for문
'''
for 변수 in 리스트(튜플, 문자열) :
    수행할 코드1
    수행할 코드2
    ...계속...
'''
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# list()
# print(test_list), type(test_list)

# for문을 이용해서 1~10까지 숫자를 출력해봅니다
# for i in range(10):     #숫자 정수로 써야 함.
#     i += 1
#     print(i)

# range.. 무엇인가...? 1. 하나의 정수 2. 콤마를 이용해 시작값, 끝 값 3. 시간, 끝, 단계

# for i in range(1,10):
#     print(i)
#     #시작하는 값 1에서 10에서 1을 뺀 값까지 나온다
gugudan_sum = 0
for i in range(1,10):
    print(f'2 x {i} = {2*i}')
    # in range 흔하게 사용
    gugudan_sum += 2 * i
    print('2단의 합 : ',gugudan_sum)

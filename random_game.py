# random 모듈을 이용한 (난수 발생) 임의의 숫자값 맞추기 게임
# 1~10 사이의 난수를 발생, 사용가자 입력(input)한 값과 비교(==)
# 난수를 맞추면 게임종료 + 맞췄습니다. 출력. 또는, 계속 입력하도록
# 종료 Q 입력시 즉시 종료

# Anaconda3 : 100개 이상의 모듈이 이미 설치가 됨. 지금 없으니 있는 모듈 사용.

# .upper(): 문자를 대문자로 바꾸는 함수
# .lower(): 문자를 소문자로 바꾸는 함수

# import random
# while True: #while true-계속 물어본다.
#     user_input = input('1~10 사이의 숫자를 입력하세요(게임종료 : Q) ')
#     if user_input.upper() == 'Q': # .upper(): 문자를 대문자로 바꾸는 함수 # .lower(): 문자를 소문자로 바꾸는 함수
#         print('사용자가 게임을 종료했습니다')
#         break;
#         #만약에, q가 입력되면 break. (반복문을 즉시 중단하는 코드)
#     com_input = random.randrange(1,10) #난수발생(1~10) randrange는 -1된 숫자
#     print('컴퓨터 : ',com_input)
#     if int(user_input) == com_input: #input은 문자이기 때문에 int를 이용해 숫자로 변환
#         print('딩동댕! 맞혔습니다.')
#         break;
#     else:
#         print('땡, 틀렸습니다. 다시 시도해 보세요!')

# Quiz. 랜덤값과 사용자 입력값을 비교, 랜덤값을 유추할 수 있도록 코드를 수정해 보세요!
# ex) 값이 큽니다. 값이 적습니다 등? 맞으면, 게임 끝

import random, time
start_time = time.perf_counter() #시작과 끝나는 시간 사이의 차이만 알려줌
com_input = random.randrange(1,10) #난수발생(1~10) randrange는 -1된 숫자
while True: #while true-계속 물어본다.
    user_input = input('1~100 사이의 숫자를 입력하세요(게임종료 : Q) ')
    if user_input.upper() == 'Q': # .upper(): 문자를 대문자로 바꾸는 함수 # .lower(): 문자를 소문자로 바꾸는 함수
        print('사용자가 게임을 종료했습니다')
        end_time = time.perf_counter()
        break
        #만약에, q가 입력되면 break. (반복문을 즉시 중단하는 코드)
    if int(user_input) == com_input: #input은 문자이기 때문에 int를 이용해 숫자로 변환
        print('딩동댕! 맞혔습니다.')
        end_time = time.perf_counter()
        break
    elif int(user_input) < com_input:
        print('값이 큽니다')
    else:
        print('값이 작습니다')
diff_time = end_time - start_time
print('-'*30)
print(f'{diff_time:.1f}초 걸렸습니다.')
print('-'*30)
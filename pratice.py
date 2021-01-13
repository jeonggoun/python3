import random, time
start_time = time.perf_counter() #시작과 끝나는 시간 사이의 차이만 알려줌
com_input = random.randrange(1,10) #난수발생(1~10) randrange는 -1된 숫자
while True: #while true-계속 물어본다.
    user_input = input('1~10 사이의 숫자를 입력하세요(게임종료 : Q) ')
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

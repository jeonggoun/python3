# 2. 문자열 포맷팅(p.57) : %, format(), f-string(ver3.6이상 사용)
# p.59 %d : 정수
print('I eat %d apple' % 3)
print("I run %f km" % 42.195)
# 소수점 이하 자릿수를 지정
print("I run %.3f km" % 42.195)
print("I run %.2f km" % 42.195)
# ※ 파이썬 버전이 v2, v3 - print " vs print()

# type() - 데이터의 종류 확인, id() - 변수의 메모리 주소를 확인
# 승률
win_rate = 95
# 게임 수
game_count = 1000
msg_text = '나는 평균 100게임의 승률이 80% 이상이다'
print('나는 평균 %d 게임의 승률이 %d%% 이상이다' % (game_count, win_rate))
print(msg_text)
# 정수일 때 %d %뒤에 % 문자 자체 쓸 것이기 때문에 %% p.59
# 값이 2개 이상일 때는 괄호로 묶어 쓴다
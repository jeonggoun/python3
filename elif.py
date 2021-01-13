# p.125 elif
# if ~ else : 하나의 조건을 비교, (참)실행, (거짓) 실행 x
# if ~ elif : 여러가지 조건을 비교


# 성적처리 - 국어, 영어, 수학
# 입력을 받아서, 총점과 평균
# 점수 구간 : A, B, C
# A : 90점 이상
# B : 80~89점
# C : 70~79점

# p.125 elif 형태
'''
kor = int(input('국어 점수?'))
eng = int(input('영어 점수?'))
math = int(input('수학 점수?'))
score_sum = kor+eng+math
avg = score_sum // 3

print('-'*30)

if avg >=90:
    print('A 학점 입니다')
elif 80<=avg<90:
    print('B 학점 입니다')
elif 70<=avg<80:
    print('C 학점 입니다')
else:
    print('좀 더 노력해야 합니다.')
'''

# p.123 논리연산자 : and, or, not <-> True, False

'''
이번 달이 몇 월인지 입력을 받아서,
해당하는 계절을 출력해 보세요
봄- 3~5 / 3, 4, 5
여름- 6~8 / 6, 7, 8
가을- 9~11 / 9, 10, 11
겨울- 12~2 / 12, 1, 2 
'''

now_month =  int(input('현재는 몇 월입니까?'))
if now_month >=3 and now_month <=5:
    #    3<=now_month<=5:
    print('새싹이 돋아나는, 봄이네요!')
elif now_month >=6 and now_month <=8:
    print('바다로 떠나는, 여름이네요!')
elif now_month >=9 and now_month <=11:
    print('하늘이 높고 독서하기 좋은, 가을이네요!')
else:
    print('눈의 계절, 겨울이네요!')


# p. 139 for문의 응용
'''
총 5명의 학생이 시험을 보고, 점수가 60점 넘으면 합격, 그렇지 않으면 불합격을 출력하시오
'''
'''
variable = 1개
array = 여러 개
'''

marks = [90, 25, 67, 45, 80]
number = 0
marks_sum = 0
for i in marks:
    number += 1
    marks_sum += i
    print(f'{number}번 학생의 점수 : {i}')
    if i >= 60:
        print(f'{number}번 학생의 결과 : 합격')
    else:
        print(f'{number}번 학생의 결과 : 불합격')
# / vs // 차이 : float vs int
marks_avg = marks_sum / 5
print(f'평균점수 : {marks_avg:.2f}')
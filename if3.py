import datetime

now_date = datetime.datetime.now()
print(now_date)

# 특정 정보 응용 가능

now_date = datetime.datetime.now()
# AM, PM 바꾸기. 24제로 되어있기 때문에 12시간으로 바꿔야 함
print('현재는 {}년 {}월 {}일 입니다'.format(now_date.year, now_date.month, now_date.day))
print('현재는 {}시, {}분 입니다').format(now_date.hour, now_date.minute)
'''
print(now_date.year)
print(now_date.month)
print(now_date.day)
print(now_date.hour)
print(now_date.minute)
# 원하는 시간 날짜 개체에서 정보 가져올 수 있다
'''
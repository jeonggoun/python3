# .format()  함수를 이용한 포맷팅
# p.62
# I eat 3 apples. 출력
print('I eat{0} apples.'.format(3))
print('I eat {0} apples and {1} bananas.'.format(3,4))
print('I eat {1} apples and {0} bananas.'.format(3,4))
# (3,4)에서 첫 번째 값이 0, 두 번째 값이 1을 나타낸다. 써도 되고 안 써도 되는데 쓰게 되면 순서 바꿀 수 있음.
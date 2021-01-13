print("문자열 출력 방법")
print('문자열 출력 방법')
# 가급적이면 혼용해서 사용하지 않도록. 하지만 같이 사용해야 할 때
print("I'm fine , thanks you!")
print("I\"m fine , thanks you!")
# print("I"m fine , thanks you!") >error
# 같은 따옴표를 사용하게 되면 오류가 난다 이때 \역슬래시 사용. 이런 문자를 이스케이프 코드(문자)라고 함.
'''
print("번호     이름     사는곳")
print("1       강아라    북구")
print("2       김현우    서구")
print("3       김혜인    광산구")
'''
print("번호\t이름\t사는곳")
#이스케이프 코드 \t 문자열 사이 탭 간격 줄 때 사용
print("1\t강아라\t북구")
print("2\t김현우\t북구")
print("3\t김혜인\t북구")

print("문장의 줄을 바꾸어 \n출력할 때 사용합니다.")
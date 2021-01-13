'''
    변수의 자료형
    1. 숫자형 / int, float, complex
    2. 문자(열)형 / string
    3. 논리형 / boolean
'''

# 숫자형 데이터
a = 10
# 문자(열)형 데이터
'''
pet_name = "금동이"
pet_age = 3
pet_type = "birds"
pet_weight = 8
# python 3.6 이상 도입된 f-string 방식
print("금동이라는 새를 키운 지 몇 년이 되었는데, 벌써 3살이고 몸무게는 8kg이 되었습니다.")
print(f"{pet_name}라는 {pet_type}를 키운 지 몇 년이 되었는데, 벌써 {pet_age}살이고 몸무게는 {pet_weight}kg이 되었습니다.")
print(pet_name,"는 ",pet_age,"살 이고, 몸무게는",pet_weight,"kg 입니다");
print(pet_name+"는 "+pet_age+"살 이고, 몸무게는"+pet_weight+"kg 입니다");
# +는 문자를 연결하기 때문에 숫자를 연결할 때는 str으로 감싸줘야 한다.

print(pet_name+"는 "+str(pet_age)+"살 이고, 몸무게는"+str(pet_weight)+"kg 입니다");
'''
# + 대신 ,를 사용하는 경우 출력은 잘 되지만 약간 띄어쓰기가 된다.
# + : 덧셈연산자, (문자) 연결 연산자
# print(text1+text2)
# html, css - "" 사용, javascript, phthon, php - '' 사용
# str() : 데이터를 문자로 출력해 주는 함수.

python_string =  'life is short, you need python'
# len() 함수
print('문자열 길이값', len(python_string))
# 문자열 인덱스/index - 문자열 데이터의 하나하나 값을 주소/번지로 구분하는 것
# [?] ?번째 번지수에 있는 문자를 가져와. -? 역방향으로, 뒤에서 ?번째의 문자를 출력
# life is short, you need python
# 1234 56 789...
print(python_string[5])
python_string1 = python_string[-2]
# 변수 - 변하는 데이터, 변할 수 있는
# 문자(열) 변경 금지
python_string1 = '0'
print(python_string)
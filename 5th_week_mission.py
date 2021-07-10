# 5주차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[4주차 복습]
1. 자료형의 정의와 종류(기본 4가지 형태)
2. 변수 정의와 활용
3. 연산자: 산술연산자(7가지), 문자열연산, 복합할당연산자
'''


## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기
'''
print(5>8)  #False
print(3<8)  #True
print(10>=7)    #True
print(200>=751) #False
print(5==11)    #False
print(5!=5) #False
print("포항항!항하항항!" == "포항항!항하항항!")   #True
print("illililillllllilil" != "illililillllllilil") #False
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10) #True
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "옵치도 갓겜이다" == "옵치도 갓겜이다") #True
print(not 5==5) #False
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print(4 <6 and 10 >= 10)    #True
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야!") #True
print(not 5==5) #False
'''

#[입력과 자료형 변환]
## mission1>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
'''
x = input("x를 입력하세요 >>")
y = input("y를 입력하세요 >>")

result = x + y
print(result)
'''
## mission2>> mission1에서 제대로된 값이 나오도록 코드를 수정해보자.
'''
x = int(input("x를 입력하세요 >>"))
y = int(input("y를 입력하세요 >>"))

result = x + y
print(result)
'''
## mission3>> 출생년도를 입력하고 나이를 출력해보자.
'''
year=int(input("출생년도를 입력하세요 >>"))

age = 2021 - year + 1
print("당신의 나이는 %d입니다." %age)
print(f"당신의 나이는 {age}입니다.")
'''
# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행
## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자
'''
subscriber = int(input("구독자 수를 입력하세요 >>"))

if subscriber<1000:
    print("수익창출을 할 수 없습니다.")
else:
    print("수익창출을 할 수 있습니다.")
'''
## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자
'''
money = int(input("가지고 있는 돈을 입력하시오."))

if money>=20000:
    print("오늘 저녁은 치킨이닭!")
elif money>=10000:
    print("이제는 고오급 음식인 떡볶이 ㅎㅎ")
elif money>=2000:
    print("그래도 굶지는 않는 편의점 삼각김밥!")
else:
    print("한입만!")
'''




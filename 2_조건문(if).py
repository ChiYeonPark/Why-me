# 비교연산자, 논리연산자
# 싹 다 긁은다음 컨트롤+/ -> 전체 주석처리
# 다른 언어 -> 변수와 선언을 따로. 파이썬은 동시에
# 초기화 -> 첫 작업. 변수를 초기화 (a = 1) 과 같이.

print(1 < 2)
print(2 > 3)

print(1 <= 1)
print(3 >= 2)

print(1 == 2)
# -> 1은 2와 같다. 등호를 2개 씀. False라고 뜸
print(1 != 2)
# -> 1은 2가 아니다.

# 논리 연산자
print(True or False)
print(True and False)
print(not False)

# 귀여운.. 함수.
# 명령어 in ->  H가 HeLLO 안에 있니?...
print("H" in "Hello")
print("Q" in "Hello")
print("Q" not in "Hello")

# 알고리즘 = 조건에 따라 경우의 수를 나누는 것
# 제어문 -> 조건문(if/switch(다른 언어에서)), 반복문(while/for). 두 개 밖에 없음

country = input("Are you Korean?\n[1] Yes\n[2] No\n")
# 여기서 한국인이기 때문에 1을 입력하면, "1"이 입력된 걸로 인식이 됨. (1과 문자열 "1"은 다르잖아..)
# 그래서 밑에서 "1"을 받은 걸로 계산하는 것.
# 1을 입력하면 첫 번째 if절에서 걸려서 탈출. elif와 else가 실행이 되지 않음
# 2를 입력하면 첫 번째 if절에서 걸리지 않고, 2번째 elif에서 걸려서 Umm... Bye가 출력. elif -> 무한정 ㅇㅋ
# 보통 가장 쉽게 걸러낼 수 있는 조건을 제일 윗쪽에 배치 함.
if country == "1":
    print("한국인이시구나~ㅎ")
elif country == "2":
    print("Umm... Bye.")
else:
    print("Please answer properly!")


# int를 사용해야함
# a = 1 a = 2 print(a) 시 -> 2로 출력 됨. 아래있는게 위에 있는걸 덮어씌움.
money = input("돈 얼마 있어? : ")
money = int(money)

if money >= 7000:
    print("택시타고 가자!")
elif 5000 <= money < 7000:
    print("흠 좀 애매하네...")
else:
    print("걸어가자..ㅎ")


# 자료형 -> 숫자, 문자열, 리스트, 딕셔너리, 불 5개..


# 불(Boolean)
# TRUE / FALSE
# is_ <- 는 그냥 불 작업을 할 때 넣는 관습적인.. 다른걸로 넣어도 ㄱㅊ음
student = input("학생이신가요?\n[1] 네\n[2] 아니오\n")

if student == "1":
    is_student = True
else:
    is_student = False

# -여기서부터 프린트 처리
if is_student == True:  # == True:가 없어도 true로 출력된다.
    print("학생이시군요!")
else:
    print("학생이 아니시군요.")

    # TRUE = 1 = 값이 있다
    # FALSE = 0 = 값이 없다

# != -> 틀리다.
answer = 25

guess = int(input("저 몇살이게요? : "))

if answer != guess:
    print("땡!")
else:
    print("눈썰미가 좋으시네!")

    # pass
    card = True

if card:  # if card == True:
    pass
else:
    print("헉 카드 두고 왔어!")

    # pass이기 때문에 그냥 아무것도 출력되지 않음.

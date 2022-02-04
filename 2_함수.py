# definition의 약자. 가장 기본 형태
# def (): <- 고정 형태.
# 함수는 무조건 괄호가 뒤에 붙어야 함.
# 호출 -> 함수를 부르는 것.. 진짜로 그냥 호출임.. 세이 이리와바.,, 이런거..
# 호출을 하기 전에 위에 먼저 함수를 선언 해주어야 함.


def say():
    print("I'm saying!")


say()

# 매개변수 (name)<- 이 매개변수. name이라는 자리에 변수를 저장할거야!


def greet(name):
    print(f"안녕하세요, {name}님!")


# --여기까지 함수 선언(정의)
# name에 무조건 값을 받도록 되어있는 것. 뒷쪽에 greet("포뇨")가 반드시 들어가야 함(할당 되어야 함)

greet("포뇨")
# -여기서 호출

# 더하기 함수
def add(a, b):
    print(a + b)


add(1, 3)
# 매개변수가 두 개. 형태를 맞춰주면 됨.
# a에 알아서 1이 들어가고, b에 알아서 3이 들어감. 따로 (b=3 a=2) 이런 식으로 지정도 가능 함


# -
# return. 함수는 다 return값을 가지고 있음.
# return -> 반환한다. 리턴 텍스트 = 텍스트 값을 반환한다.
# return = 한 가지 값을 여러 번 쓸 수 있게 해주는 것. 내가 보낸 값을 처리를 해서 새로운 값으로 다시..
# print = 그냥 그 값을 출력.
def echo(text):
    return text


echo("안녕!")
print(echo("안녕!"))


# -
# 여기서의 return은 처음으로 돌아가는 느낌. return -> 함수를 종료시키고 처음으로 돌림.
# break -> for문, 즉 반복문 탈출
# cuntinue는 반복문 윗쪽으로 올라가고 다시, pass는 넘어가서 if문 바깥쪽 계산
# return -> 함수 탈출. 함수를 종료하는 함수..
# #pass -> if문, 즉 조건문 탈출
# if - pass \ while/for - continue, break \ def - return


def meockgeum(num):
    if num == 1:
        print("먹금합니다.")
        return
    else:
        print("먹금 실패!")


meockgeum(1)
meockgeum(2)

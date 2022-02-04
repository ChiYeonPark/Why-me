# 기본
# while True:
#     print("안녕?")
# 조건이 맞다면 반복적으로 출력
# 잘못된 구문임.. 안녕이 미친듯이 나옴.. 컨트롤+c로 멈추기..


# -
# i = 변수. 항상 바꿔도 됨. i라는 변수에 0을 할당한 상태. while 안에 들어감
# i가 10보다 작을 때, print를 하고 계속 1씩 더해주기.
i = 0

while i < 10:
    print(f"i={i} | 아직 10 안됐음!")
    i += 1


# -
# if문과 결합
dabjeongneo = 2

while dabjeongneo != 1:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아? : ")
    if dabjeongneo == "1":
        print("흐흠 그럴 줄 알았어! *^-^*")
    else:
        pass
    # while 문에서 pass가 되면 if문에서만 탈출하기 때문에(본인을 감싸고 있는 가장 가까운 테두리만 탈출)
    # 바로 while문으로 다시 들어가버림.


# break -> 가장 가까이 있는 while문을 탈출해버림.
# 이게 while 제일 처음했던 잘못 짠 while문처럼 계속 반복되어 나온,
# 1을 입력하면 break되어 while문을 탈출하게 됨.
while True:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아? : ")
    if dabjeongneo == "1":
        print("흐흠 그럴 줄 알았어! *^-^*")
        break
    else:
        pass


# -
# continue
# continue를 만나면 자기를 감싸고 있는 가장 가까운 while문의 처음으로 돌아감
# pass는 다음으로 넘어가는 것. 둘이 다름.
# 바로 위와 최종 형태는 같음(사용자는 차이를 느끼지 못함.)
while True:
    dabjeongneo = input("1번이랑 2번 중에 뭐가 좋아? : ")
    if dabjeongneo != "1":
        continue
    else:
        print("흐흠 그럴 줄 알았어! *^-^*")
        break

# 기본
for i in range(1, 11):
    print(i)
# 여기서도 i는 관습적인 것. number 넣어도 되고.. 아무거나 가능.
# 똑같이만 맞춰주면 됨.

# range의 형태
# range(start, end+1)
# range(1, 101)
# range를 출력하려면 for문 안에 넣어주어야 함.
# 1~10까지의 집합을 순서대로 꺼내주는 것.

# -

# list
family = ["엄마", "아빠", "나", "동생"]

for member in family:
    print(member)

# list -> 반복 가능한 개체 = 문자열도 가능함. "Hello" -> H, e, l, l, o
# 순서가 존재. 0번째 -> 엄마. 순서대로 아빠, 나, 동생 순서대로..

# 리스트 예시
heights = [150, 160, 170, 180]
total = 0

for height in heights:
    total += height
# -> 0에 150을 더하고
# -> 그 후에 160을 또 더하고..
# total -> 임의로 지어준 것.. **초기화를 했다는 것에 집중하기**

print(f"평균 : {total/4}cm")
# -
print(f"평균 : {total/len(heights)}")
# len -> list에 사용하는 함수. len*length -> height라는 리스트 안에 들어있는 요소의 갯수를 가져오게 됨.
# 위의 예시는 4개라는게 딱 보이지만 그게 아닐 때, 그리고 리스트 안 요소의 갯수가 늘어날 때..
# len이 4를 대체한 것
txt = "Hello"
print(len(txt))
# Hello의 길이(갯수)가 출력 됨.

#\n 줄 바꾸기
name = input("당신을 뭐라고 부르면 될까요?\n")
print(f"만나서 반가워요, {name}님.")

#int -> 영어 'integer'(정수)의 약자
#f -> formatting의 약자. 변수를 문자열로 바꾸는 포맷팅
birth = input("언제 태어나셨나요? YYYY로 입력해주세요.\n")
age = 2022 + 1 - int(birth)
print(f"{name}님은 {age}세 이네요. 그치요? 아니면 어떡하지..")

#답지. 보기 쉽게 int를 하나하나 나눠놓은 것
year = input("Your Birthyear? : ")
year = int(year)
age = 2022 - year + 1
print(f"You are {age}!")

#GUI -> 그래픽화 해서 보여주는 것
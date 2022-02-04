# 라이브러리 import

# import keyboard

white = " "
position = " ■"
print(position)
while True:
    if keyboard.read_key() == "d":
        white += " "
        print(white + position)
    elif keyboard.read_key() == "a":
        white = white.replace(" ", "", 1)
        print(white + position)

        # 사실 -> 버튼을 누르면 공백이 추가되는 것이고 <-를 누르면 공백이 삭제되는 것에 불과

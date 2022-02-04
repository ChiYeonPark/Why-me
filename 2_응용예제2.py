import sys
import time

text = "안녕하세요..."

for letter in text:
    sys.stdout.write(letter)  # print 출력 과정에 관한 줄
    sys.stdout.flush()
    time.sleep(0.1)

    # 0.1초 후에 하나씩 출력


def typing(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

"""
# 직각삼각형
for i in range(1, 6):
    for j in range (6 - i):
        print("*", end = "")
    print("")
"""

"""
# 역직각삼각형
for i in range(6, 1):
    print("*" * i)
"""

"""
# 이등변삼각형
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
"""

"""
# n = 5 # 삼각형의 높이를 설정
for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
"""

"""
# 5x5 출력
num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []
"""

"""
# 세로로 출력
num = 0
line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = []
"""

"""
# 역순 출력
num = 26
line = []
for i in range(5):
    for j in range(5):
        num += -1
        line.append(num)
    print(line)
    line = []
"""

"""
# 가위바위보 게임
import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print("무승부")
        return
    elif (
    (user_choice == '1' and pcnum == '3') or
    (user_choice == '2' and pcnum == '1') or
    (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return

print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
pcnum = get_computer_choice()

determine_winner(chnum)
"""

"""
# 파일 생성
# f = open("new.txt", 'w')

f = open("temp.txt", 'w')
f.close()
"""

"""
# 파일 쓰기
file = open("temp.txt", "w")

# flie.write("hello")
file.write("hello")
file.write("world")

file.close()
"""

"""
# 1 ~ 100
flie = open("temp.txt", 'w')

for i in range(100) :
    flie.write(f"(i)\n")

file.close()
"""

"""
# “c:/User/Catholic/temp.txt” _개인pc 호환

f = open("C:\\Users\\user\\rabbit\\rabbit\\temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")

f.close()
"""

"""
# 추가 쓰기
f = open("C:\\Users\\user\\rabbit\\rabbit\\temp.txt", "a")

f.write("hello\n")
f.write("world")

f.close()
"""

"""
# 파일 읽기
file = open("temp.txt", "r")
res = file.read()
print(res)

file.close()
"""

"""
# 다른 경로 파일 읽기
file = open("C:\\Users\\user\\rabbit\\rabbit\\temp.txt", "r")
res = file.read()
print(res)

file.close()
"""

"""
# readline
# file = open("temp.txt", "r")
file = open("temp.txt", "r")

for i in range(110) :
    res = file.readline()
    print(res)

file.close()
"""

"""
# readlines 읽기
file = open("temp.txt", "r")
res = file.readlines()
print(res)

file.close()
"""

"""
# readlines 읽기
file = open("temp.txt", "r")
line = file.readlines()
for l in line :
	print(l)

file.close()
"""

"""
# file object
f= open("temp.txt", "r")
for line in f :
	print(line)

f.close()
"""
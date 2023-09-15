"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  
"""

"""
a = 5
b = 5
print(a is b) 
print(a is not b) 
"""

"""
a = 3
b = 3.0

print(a == b)
print(a is b) 
print(a is not b) 
"""

"""
a = [3 , 5, 1]
b = a

print(a is b) 
print(a is not b) 
"""

"""
a = [3 , 5, 1]
b = a

print(a is b) 

a[0] = 2

print(a, b) 
print(a is b) 
"""

"""
x = 2 ** 3 ** 2
print(x)    
"""

# a = 2 + 3 * 4 
# print(a)

# a =10 / 5 / 2
# print(a)

# a = 2 ** (3 ** 2)
# print(a) 

# a = 10 % 3 % 2
# print(a)

# a = 1 + 2 > 3 and 4 - 1 < 2
# print(a)

# a = not False and True
# a = not True or False and True
# print(a)

# a = 1 & 2 | 3 ^ 4
# print(a)

# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# print(a)

# a = 2 * -3 // 2
# print(a)

# a = 1 == 2 
# a = 1 == 2 != 3
# print(a)

"""
x = 10
# x = 0
# x = -1

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")
"""

"""
# if 짝수, 홀수
num = 23
if num % 2 == 0:
    print("짝수")
else: 
    print("홀수")
"""

"""
# if 두 수 비교
a = 2
b = 3
if a == b:
    print("같습니다")
else:
    print("다릅니다")
"""

"""
# if a or b 인지
char = "a" 

if char == "a" or char == "b":
    print("'a' 또는 'b'입니다.")

else:
    print("'a' 또는 'b'가 아닙니다.")
"""

"""
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
"""

"""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
"""

"""
# for 0 ~ 9 출력
for i in range(10):
    print(i)
"""

"""
# for 문자열 낱자 출력
for char in "python":
    print(char)
"""

"""
# for 역순 출력
fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit)
"""

"""
# for 역순 출력
fruits = ["apple", "banana", "cherry"]

for fruit in sorted(fruits, reverse=True):
    print(fruit)
"""

"""
# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
"""

"""
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
"""

"""
for i in range(10):
    if i == 7:
        print("break", 1)
        break
    elif i == 1:
        print("continue", 1)
        continue
    else:
        print("pass", 1)
        pass

    print(i)
"""

"""
i = 1

while i <= 5:
    print(i)
    i += 1
"""

"""
# while 0 ~ 9 출력
i = 0

while i <= 9:
    print(i)
    i += 1
"""

"""
# while 문자열 낱자 출력
str_word = "python"
i = 0
while i < len(str_word):
    print(str_word[i])
    i += 1
"""

"""
# while 1 ~ 10 총합 출력
sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1

print(sum)
"""

"""
# while 1 ~ 100 짝수, 홀수 출력
i = 1

while i <= 100:
    if i % 2 == 0:
        print("짝수: ", i)
    elif i % 2 == 1:
        print("홀수: ", i)
    i += 1
"""

"""
# while 1 ~ 100 7의 배수만 출력
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1
"""
# 무한루프시 ctrl + c
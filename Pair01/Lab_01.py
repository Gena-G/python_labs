# 1
# a
Number1 = int(input("Type in a full number: "))
EvenOrOdd = Number1 % 2
if EvenOrOdd > 0:
    print("Odd")
else:
    print("Even")

# b
Number2 = int(input("Type in your age: "))
if Number2 >= 18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітній!")

# c
Number3 = int(input("Type in the R of a circle: "))
pi = 3.14
l = Number3 * pi
s = Number3 ** 2 * pi
print(l)
print(s)

# d
a = int(input())
b = int(input())
if a > b:
    print(a)
elif a == b:
    print("They're equal")
else:
    print(b)

# 2
x, y = map(int, input().split(" "))
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
else:
    print("I dunno, middle?")

# 3
age = int(min(input("Please type in your age:"), 120))
print(age, "рік")
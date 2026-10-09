#1
# pi1 = 3.14159

# def circle(r):
#     return pi1 * r ** 2

# def rect(w, h):
#     return w * h

# def trian(a, h):
#     return a * h / 2

# def main():
#     fig = input("Фігура: ")

#     if fig == "круг":
#         r = int(input("Радіус: "))
#         res = circle(r)
#         name = "круга"
#     elif fig == "прямокутник":
#         w = int(input("ширина: "))
#         h = int(input("висота: "))
#         res = rect(w, h)
#         name = "прямокутника"
#     elif fig == "трикутник":
#         a = int(input("основа: "))
#         h = int(input("висота: "))
#         res = trian(a, h)
#         name = "трикутника"
#     else:
#         print("I dunno")
#         return

#     print("Площа " + name + ":", res)

# main()


#2
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1): # Found this math online and I think it works?
#         if n % i == 0:
#             return False
#     return True

# def divisors(n):
#     divs = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divs.append(i)
#     return divs

# def digit_sum(n):
#     sum1 = 0
#     while n > 0:
#         sum1 += n % 10
#         n //= 10
#     return sum1

# def main():
#     n = int(input("N = "))

#     if is_prime(n):
#         print("Просте число: так")
#     else:
#         print("Просте число: ні")
#     print("Дільники:", divisors(n))
#     print("Сума цифр:", digit_sum(n))

# main()


# 3
# def average(grades):
#     return sum(grades) / len(grades)

# def minimum(grades):
#     return min(grades)

# def maximum(grades):
#     return max(grades)

# def count_above(grades, value):
#     count = 0
#     for g in grades:
#         if g > value:
#             count += 1
#     return count

# def main():
#     grades = []
#     parts = input("Оцінки: ").split()
#     for i in parts:
#         grades.append(int(i))
#     lim = int(input("Поріг: "))

#     print("Середній бал:", average(grades))
#     print("Мінімальна:", minimum(grades))
#     print("Максимальна:", maximum(grades))
#     print("Вище " + str(lim) + ":", count_above(grades, lim))

# main()


# 4
# def length(password):
#     return len(password) >= 8

# def digit(password):
#     for c in password:
#         if c.isdigit():
#             return True
#     return False

# def upper(password):
#     for c in password:
#         if c.isupper():
#             return True
#     return False

# def lower(password):
#     for c in password:
#         if c.islower():
#             return True
#     return False

# def special(password):
#     for c in password:
#         if not c.isalpha() and not c.isdigit():
#             return True
#     return False

# def validate_password(password):
#     errors = []
#     if not length(password):
#         errors.append("Min 8")
#     if not digit(password):
#         errors.append("No digit")
#     if not upper(password):
#         errors.append("No upper")
#     if not lower(password):
#         errors.append("No little letter")
#     if not special(password):
#         errors.append("немає спеціального символу") # gotta satisfy that shown example.

#     if len(errors) == 0:
#         ok = True
#     else:
#         ok = False
#     return ok, errors

# def main():
#     password = input("Password: ")
#     ok, errors = validate_password(password)

#     if ok:
#         print("Пароль надійний.")
#     else:
#         print("Пароль не відповідає вимогам.")
#         for le in errors: # why le? Cause I felt like it.
#             print("Не виконано: " + le)

# main()
# # 1
# N = int(input("Type in a N: "))
# countN = 0
# sumN = 0
# for i in range(1, N+1):
#     if i % 3 == 0 or i % 5 == 0:
#         countN += 1
#         sumN += i
# print("Кількість:", countN, "Сума", sumN)
# if countN > 0:
#     print("Середнє: ", round(sumN / countN, 2)) # Me when I finally find the command to make the digit round up be like:

# # 2
# n = int(input("Type in a n: "))
# min_digit = 9
# max_digit = 0
# dcount = 0
# dsum = 0
# if n == 0:
#     dcount = 1
#     min_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     if digit < min_digit:
#         min_digit = digit
#     dsum += digit
#     n = n // 10
#     dcount += 1

# print("Кількість цифр:", dcount)
# print("Сума цифр:", dsum)
# print("Найбільша цифра:", max_digit)
# print("Найменша цифра:", min_digit)

# #3
# A = int(input("Type in number: "))
# Numbers = []
# for i in range(1, A+1):
#     Nuhuh = True
#     t = i
#     while t > 0:
#         digit = t % 10
#         if digit == 0 or i % digit != 0:
#             Nuhuh = False
#             break
#         t = t // 10
#     if Nuhuh == True: Numbers.append(i)
# print(Numbers)

# # 4
# width = int(input("width: "))
# height = int(input("height: "))
# border_char = input("контур: ")
# fill_char = input("всередині: ")

# if width < 3 or height < 3:
#     print("error. min — 3x3.")
# else:
#     for i in range(height):
#         row = ""
#         for col in range(width):
#             if i == 0 or i == height - 1 or col == 0 or col == width - 1:
#                 row += border_char
#             else:
#                 row += fill_char
#         print(row)
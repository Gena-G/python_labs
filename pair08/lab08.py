# #1
# a = input("A: ")
# b = input("B: ")
# op = input("Операція: ")

# try:
#     a = float(a)
#     b = float(b)
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         print(a / b)
#     else:
#         print("Error. What ya tryna to do?")
# except ValueError:
#     print("Error: Dunno. Not a number maybe.")
# except ZeroDivisionError:
#     print("Помилка: на нуль ділити не можна.")

# #2
# def input_grade():
#     while True:
#         try:
#             g = int(input("Оцінка: "))
#         except ValueError:
#             print("Помилка: потрібно ввести ціле число.")
#             continue
#         try:
#             if g < 1 or g > 12:
#                 raise ValueError # Well I just found out that I can just like raise em. Well without text that is and so on
#             return g
#         except ValueError:
#             print("Помилка: оцінка повинна бути від 1 до 12.")

# g = input_grade()
# print("Прийнято:", g)

# #3
# students = ["Ivan", "Olena", "Petro", "Maria"]
# grades = {"Math": 10, "IT": 9, "History": 11, "Biochemistry": 112} #Average Хім Біо be like:

# c = input("1 - учень, 2 - предмет: ")

# if c == "1":
#     try:
#         i = int(input("Індекс: "))
#         if i < 0:
#             raise IndexError # I mean if I put in negatives it kinda worked so I would assume.
#         print(students[i])
#     except ValueError:
#         print("Error: That better be a whole number boy.")
#     except IndexError:
#         print("Помилка: учня з таким індексом немає.")
# elif c == "2":
#     s = input("Class: ").strip().lower()
#     try:
#         print(grades[s])
#     except KeyError:
#         print("Error: Nuh uh, No such class in this town.")
# else:
#     print("Error: Something went wrong. Probabaly.")

# #4
# good = []
# bad = 0

# try:
#     with open('students.txt', 'r', encoding="utf-8") as file:
#         for number, line in enumerate(file, start=1):
#             parts = line.strip().split(';')
#             if len(parts) != 2:
#                 print(f'Line {number} skipped: wrong line format teehee.')
#                 bad += 1
#                 continue
#             name, grade = parts
#             try:
#                 grade = int(grade)
#             except ValueError:
#                 print(f'Рядок {number} пропущено: бал не є числом.')
#                 bad += 1
#                 continue
#             if grade < 0 or grade > 100:
#                 print(f'Рядок {number} пропущено: бал поза діапазоном.')
#                 bad += 1
#                 continue
#             good.append([grade, name])
# except FileNotFoundError:
#     print('Error: Who stole my students file?')
# else:
#     good.sort(reverse=True)

#     with open('report.txt', 'w', encoding="utf-8") as file:
#         for grade, name in good:
#             file.write(f'{name};{grade}\n')

#     print('Правильних записів:', len(good))
#     print('Пропущено:', bad)
#     print('Створено report.txt')
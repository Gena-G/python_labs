# if 7 > 5:
#     print("ok")

# n = int("Number")
# print(n)

# try:
#     age = int(input("Please input ur age: "))
#     print("your age is: ", age)
# except ValueError:
#     print("Enter ur age in numbaaahs")
# #ValueError - correct operation but wrong type of data

# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     res = a / b
#     print(res)
# except ValueError:
#     print("A and B must be digits")
# except ZeroDivisionError:
#     print("No diving by 0")
# finally:
#     print("You probably didn't break it. Good")

# while True:
#     try:
#         grade = int(input("Enter your grade: "))
#         if grade < 1 or grade > 12:
#             raise ValueError("grade must be between 1-12")
#         print(f"Your grade is {grade}")
#         break
#     except ValueError as error_limit:
#         print(f"Error: {ValueError}")

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except:
#             print("Please o thy lod give me an int.")

# n = int_input("Number please: ")
# print(n)

# def int_input(message):
#     while True:
#         try:
#             grade = int(input("Enter your grade: "))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Grade must be between 1 and 12")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = int_input()
# print(f"Your grade of {grade} got accpeteedf w fwf")

# price = {
#     'apple': 10,
#     'banana': 20
# }

# product = input('Enter product name ')
# try:
#     print(price[product])
# except KeyError:
#     print('Nuh uh')

# product = input('Enter product name: ')
# price = price.get(product, "Product no no")

# try:
#     with open('data.txt', 'r', encoding='utf-8') as f:
#         data = f.read
#         print(data)
# except FileNotFoundError:
#     print('file nono')

# line = "Ivan;95"
# parts = line.strip.split(';')
# if len(parts) != 2:
#     print('nuhuh')
# else:
#     name = parts[0]
#     grade = parts[1]
#     try:
#         grade_int = int(grade)
#         if grade_int < 0 or grade_int > 100:
#             raise ValueError("Not between 1 and 100")
#     except ValueError as e:
#         print(f'error: {e}')
#     else:
#         print(f'correct: {name} - {grade_int}')

# lines = [
#     'Ivan;95',
#     'Liza;hello',
#     'Vadymka;100'
# ]

# for line_number, line in enumerate(lines, start=1):
#     parts = line.strip().split(';')
#     if len != 2:
#         print(f'Line number {line_number} has error')
#         continue
#     name = parts[0]
#     try:
#         score = int(parts[1])
#     except ValueError:
#         print(f'Line {line_number} skipped, wrong bal')
#         continue
#     print(f'Correct: {name} - {score}')
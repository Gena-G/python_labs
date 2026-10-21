#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'{self.width} × {self.height}: площа = {self.area()}, периметр = {self.perimeter()}')
# rect1 = Rectangle(5, 3)
# rect2 = Rectangle(10, 4)
# rect1.info()
# rect2.info()

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self, grade):
#         if grade > 12 or grade < 1:
#             print(f'Оцінка {grade} не додається.')
#         else:
#             self.grades.append(grade)
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         else:
#             return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {round(self.average(), 2)}'
# s1 = Student("Ivan Petrenko")
# s1.add_grade(10)
# s1.add_grade(12)
# s1.add_grade(15)
# s1.add_grade(9)
# print(s1)

#3
# class Student: #Well it didn't say anything about changing it now did it? Simply told me to take the same class. I did.
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         else:
#             return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'{self.name} - {round(self.average(), 2)}'

# Students = [
#     Student("Anna", [5, 4, 7, 12, 11]),
#     Student("Ivan", [6, 8, 2, 12, 10]),
#     Student("Olha", [8, 7, 7, 11, 11]),
#     Student("Kali", [9, 10, 11, 12, 11]),
#     Student("Malkuth", [7, 3, 7, 10, 9])
# ]
# for s in Students:
#     print(s)
# BestofTheBestofTheBest = []
# for stu in Students:
#     if len(BestofTheBestofTheBest) == 0:
#         BestofTheBestofTheBest.append(stu)
#     elif stu.average() > BestofTheBestofTheBest[0].average():
#         BestofTheBestofTheBest.clear()
#         BestofTheBestofTheBest.append(stu)
#     elif stu.average() == BestofTheBestofTheBest[0].average():
#         BestofTheBestofTheBest.append(stu)
# for i in BestofTheBestofTheBest:
#     print(f'Найкращий результат: {i.name} — {round(i.average(), 2)}')

#4
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount <= 0:
#             print('Broke much?')
#         else:
#             self.balance += amount
#     def withdraw(self, amount):
#         if amount <= 0:
#             print('U tryna to scam the bank?')
#         elif amount > self.balance:
#             print(f'Помилка: недостатньо коштів для -{amount}')
#         else:
#             self.balance -= amount
#     def info(self):
#         print(f'{self.owner}: баланс {self.balance}')

# ivan = Wallet("Ivan", 1000)
# ivan.deposit(500)
# ivan.withdraw(300)
# ivan.withdraw(2000)
# ivan.deposit(0)

# olha = Wallet("Olha", 700)
# olha.withdraw(200)
# olha.deposit(100)
# olha.withdraw(-50)
# olha.withdraw(5000)

# ivan.info()
# olha.info()
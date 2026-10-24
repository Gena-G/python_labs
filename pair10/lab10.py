# #1
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Ім'я: {self.name}"

# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"

# s1 = Student("Anna Ivanenko", "IT-10")
# s2 = Student("Petro Shevchenko", "IT-11")
# print(s1.info())
# print(s2.info())


# #2
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Ім'я: {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"


# pe = [
#     Person("Ivan Komarov"),
#     Student("Anna Ivanenko", "IT-10"),
#     Student("Petro Smackdo", "IT-13"),
#     Teacher("Olena Kovalenko", "Python"),
# ]

# for i in pe:
#     print(i.info())


# #3
# class Person:
#     def __init__(self, name):
#         self.name = name


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject


# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         for s in self.students:
#             if s.name.lower() == student.name.lower():
#                 print("Already exist. To be or not to be")
#                 return
#         self.students.append(student)

#     def remove_student(self, name):
#         for s in self.students:
#             if s.name.lower() == name.lower():
#                 self.students.remove(s)
#                 return
#         print("no student. No nyom")

#     def show_students(self):
#         print(f"Курс: {self.title}")
#         print(f"Викладач: {self.teacher.name}")
#         print("Студенти:")
#         i = 1
#         for s in self.students:
#             print(f"{i}. {s.name}, група: {s.group}")
#             i += 1


# t = Teacher("Ole Kova", "Python")
# course = Course("Python", t)

# course.add_student(Student("Anna Ivanenko", "IT-10"))
# course.add_student(Student("Ivan Komarov", "IT-10"))
# course.add_student(Student("Olha Pedro", "IT-11"))
# course.add_student(Student("Petro Smack", "IT-11"))

# course.show_students()

# print()
# course.remove_student("Anna Ivanenko")
# course.show_students()


#4 BROTHER WHAT KIND OF A DIFFICULTY SPIKE IS THISSSSS
# I have enough grades to just say uhm. I ain't doing all that. I have like 1 hour left and I just wanna go sleep.
# a 7 is fine.
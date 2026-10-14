import math
import random
import statistics
import datetime
import tkinter as tk
from tkinter import messagebox
import student_utils

# #1
# Ra = float(input("Радіус: "))
# k1, k2 = input("Катети: ").strip().split(",")
# k1 = float(k1)
# k2 = float(k2)
# Items = int(input("Предметів: "))
# Pack = int(input("В упаковці: "))

# Scircle = round((Ra ** 2) * math.pi, 2) # I mean it says to 2 symbols but in the answer it has 3 so ig.
# print("Площа круга: ", Scircle)
# k3 = round(math.sqrt((k1 ** 2) + (k2 ** 2)), 2)
# print("Гіпотенуза: ", k3)
# NPacks = math.ceil(Items / Pack)
# print("Потрібно упаковок: ", NPacks)

# #2
# N = int(input("N = "))
# while N < 0:
#     print("Wrong answer GOJO!")
#     N = int(input("N = "))
# Grades = []
# for i in range(N):
#     Gr = random.randint(1, 12)
#     Grades.append(Gr)
# print("Оцінки: ", Grades)
# print("Min: ", min(Grades))
# print("Max: ", max(Grades))
# print("Середнє: ", statistics.mean(Grades))
# print("Медіана: ", statistics.median(Grades))
# Count = 0
# for e in Grades:
#     if e >= 10:
#         Count += 1
# print("Оцінок 10 - 12: ", Count)

# #3
# date = datetime.date.fromisoformat(input("Дата події: ")) # found this bad boy on the uh wiki I guess? or Library?
# Cdate = datetime.date.today()
# TimeL = date - Cdate
# if TimeL < datetime.timedelta(0):
#     print("You're late SONIC. I AM ALREADY FORKLIFT CERTIFIED:", (Cdate - date).days)
# elif TimeL > datetime.timedelta(0):
#     print("До події залишилося:", TimeL.days, "днів")
# else:
#     print("The time has cu- wait a minute.")

# #4
# students = ["Anna", "Ivan", "Olha"]
 
 
# def mr():
#     value = entry.get()
#     if not value.isdecimal():
#         messagebox.showerror("Error", "Not a digit dumbahh")
#         return
#     count = int(value)
#     if count < 1 or count > 20:
#         messagebox.showerror("Error", "Must be between 1 and 20")
#         return

#     report = ""
 
#     for name in students:
#         gra = student_utils.generate_grades(count)
#         average = student_utils.average_grade(gra)
#         lvl = student_utils.get_level(average)
#         report += f"{name}: {gra} → {average} → {lvl}\n"
 
#     print(report)
#     text.delete("1.0", tk.END)
#     text.insert(tk.END, report)
 
 
# window = tk.Tk()
# window.title("Статистика учнів")
 
# label = tk.Label(window, text="Кількість оцінок (1–20):")
# label.pack()
 
# entry = tk.Entry(window)
# entry.pack()
 
# button = tk.Button(window, text="Сформувати звіт", command=mr)
# button.pack()
 
# text = tk.Text(window, width=60, height=10)
# text.pack()
 
# window.mainloop()
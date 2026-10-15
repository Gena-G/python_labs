import math
import statistics as stat
from math import * #Used often
import random #Barely used
from datetime import date
import demo
import tkinter as Tk

# print(math.sqrt(81))

# a = [10, 15, 8, 9, 11, 12]
# print(f'Average: {stat.mean(a)}')
# r = int(input("r = "))
# circle_area = round(pi * pow(r, 2),2)
# print(circle_area)

# balls = 25
# n = 6
# print(f"Fully filled boxes: {floor(balls / n)}")
# print(f"Boxes: {ceil(balls / n)}")

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 100))
# print(f"Random: {numbers}")

# selected = random.choice(numbers)
# print(f"Selection from that: {selected}")

# print(f"Today: {date.today()}")

# print(demo.square(5))
# print(demo.is_even(7))
# print(demo.average(numbers))

def text():
    text = "hello world"
    lbl_text["text"] = text

def clear(event):
    lbl_text["text"] = ""

window = Tk()
window.title("my first window")
window.geometry('500x400')
window.resizable(False, False)
window['bg']='FFFFFF'
label = Tk.Label(window, text = "Super Puper Duper Buper Program", font=("Arial, 18"), bg="FFFFFF", pady = 20)
# label.place(x=0, y=0)
label.pack()
frame = Tk.Frame(window, bg="FFFFFF")
frame.pack()
bt1 = Tk.Button(frame, text="OK", width=7, activebackground="lightgreen", command=text)
bt1.grid(row=0, column=0, padx = 10)
bt2 = Tk.Button(frame, text="NuhUh", width=7)
bt2.grid(row=0, column=2, padx = 10, activebackground="lightgreen")

bt2.bind("<Button-1>", clear)

lbl_text = Tk.Label(frame, text = "", font=("Arial, 18"), bg="FFFFFF", pady=20)
lbl_text.grid(row=0, column=0, columnspan=2)

window.mainloop
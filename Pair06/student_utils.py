import random

def generate_grades(count):
    return [random.randint(1, 12) for i in range(count)]
def average_grade(grades):
    return round(sum(grades) / len(grades), 2)
def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"
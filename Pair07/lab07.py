#1
# lines = []
# with open('text.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         lines.append(line.strip())

# words = 0
# chars = 0
# lo = ''
# lo_number = 0

# for number, line in enumerate(lines, start=1):
#     words += len(line.split())
#     chars += len(line)
#     if len(line) > len(lo):
#         lo = line
#         lo_number = number

# print(f'Рядків: {len(lines)}')
# print(f'Слів: {words}')
# print(f'Символів: {chars}')
# print(f'Найдовший рядок: №{lo_number}, {len(lo)} символів')
# print(f'Текст: {lo}')

#2
# lines = []
# with open('text.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         lines.append(line.strip())

# part = input('\nФрагмент: ').lower()
# found = False

# for number, line in enumerate(lines, start=1):
#     if part in line.lower():
#         print(f'{number}: {line}')
#         found = True
# if not found:
#     print('Its not there man.')

#3
# botanic = []
# with open('students.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         name, grade = line.strip().split(';')
#         if int(grade) > 80:
#             botanic.append([int(grade), name])

# botanic.sort(reverse=True) # Well the first time it kinda sorted them by names so I just uh. Flipped it. Works nicely.

# with open('result.txt', 'w', encoding="utf-8") as file:
#     for grade, name in botanic:
#         file.write(f'{name};{grade}\n')

#4
# def read_grades(filename):
#     data = {}
#     with open(filename, 'r', encoding="utf-8") as file:
#         for line in file:
#             if line.strip():
#                 name, subject, grade = line.strip().split(';')
#                 if name not in data:
#                     data[name] = []
#                 data[name].append(int(grade))
#     return data

# def average(grades):
#     return sum(grades) / len(grades)

# data = read_grades('grades.csv')

# stats = []
# for name, grades in data.items():
#     stats.append([round(average(grades), 2), name, len(grades)])
# stats.sort(reverse=True)

# best_avg = 0
# for avg, name, count in stats:
#     if avg > best_avg:
#         best_avg = avg

# best_names = []
# for avg, name, count in stats:
#     if avg == best_avg:
#         best_names.append(name)

# with open('report.txt', 'w', encoding="utf-8") as file:
#     for avg, name, count in stats:
#         file.write(f'{name} — оцінок: {count} — середній: {avg}\n')
#     file.write(f'Найкращий результат: {" та ".join(best_names)} — {best_avg}\n')
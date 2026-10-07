# #1
# nums = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# posit = []
# neg = []
# even = []
# m3 = []

# for i in nums:
#     if i > 0:
#         posit.append(i)
#     if i < 0:
#         neg.append(i)
#     if i % 2 == 0:
#         even.append(i)
#     if i % 3 == 0:
#         m3.append(i)

# min1 = min(nums)
# max1 = max(nums)
# sum1 = sum(nums)
# avr1 = sum1 / len(nums)

# print("Додатні:", posit)
# print("Від'ємні:", neg)
# print("Парні:", even)
# print("Кратні 3:", m3)
# print("Min:", min1, "; Max:", max1, "; Sum:", sum1, "; Average:", round(avr1, 2))

# #2
# group1 = {'Anna', 'Ivan', 'Olha'}
# group2 = {'Ivan', 'Maksym', 'Olha'}

# common = group1 & group2
# only1 = group1 - group2
# only2 = group2 - group1
# unique = group1 | group2

# print("Спільні: " + ", ".join(common))
# print("Тільки group1: " + ", ".join(only1))
# print("Тільки group2: " + ", ".join(only2))
# print("Усі: " + ", ".join(unique))

# #3
# prices = {
#     "bread": 10,
#     "milk": 48,
#     "apple": 11,
#     "banana": 12,
#     "tea": 75
# }

# prices["coffee"] = 101

# search = input()
# price = prices.get(search)
# if price is not None:
#     print("Found: ", search,  price, " grn")
# else:
#     print("Not found")

# min_price = float(input("Min: "))
# max_price = float(input("Max: "))
# for item, itemp in prices.items():
#     if min_price <= itemp <= max_price:
#         print(item, " - ", itemp, " grn")

# #4
# group_info = ('10-IT', '2026/2027')

# journal = {}

# students = [
#     ("Anna", [10, 11, 12, 9, 10]),
#     ("Ivan", [8, 9, 10, 11, 9])
# ]

# for name, g in students:
#     valid = True
#     if len(g) != 5:
#         valid = False
#     else:
#         for mark in g:
#             if mark < 1 or mark > 12:
#                 valid = False
#                 break
    
#     if valid:
#         journal[name] = g
#     else:
#         print("bruh")

# print(group_info[0], "-", group_info[1])

# averages = []
# for n1, g1 in journal.items():
#     avg = sum(g1) / len(g1)
#     averages.append((avg, n1))

# sort1 = sorted(averages, reverse=True)

# for avg, n in sort1:
#     print(n, "—", round(avg, 2))

# top_avg, top_name = sort1[0]
# print("Найкращий результат:", top_name, "—", round(top_avg, 2))
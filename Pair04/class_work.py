# Collections are structures of data which allow to save sets of information.
# list, arranged changable collection
# grades = [12, 4, "6", 9]
# numbers = []
# numbers2 = list()
# print(grades[2])
# # print(grades[5])
# print(len(grades))
# grades[2] = 6
# print(grades)
# numbers.append(5)
# numbers.append(6)
# numbers.append("6")
# numbers.insert(1, 2)
# numbers.insert(10, 2) # if no 10th or 9th or so on index then just to the end of the list.
# numbers.extend([4, 2, 3, "4"]) # into the end.
# numbers.remove("6") # specifically this one or error. Also only the first one it find from start.

# numbers.pop(-1) # delete this index.
# del numbers[1] # also ^
# del numbers # this specific list is gonna die

# numbers.clear() # erase everything inside expect erasing the list :D
# print(numbers.count(5)) # counts how much 5s
# print(numbers.index(6)) # search for index of first 6

# print(20 in numbers) # True or Not>
# len()
# min()
# max()
# sum()
# average = sum(numbers) / len(numbers)

# numbers.sort() # changes the list from smallest tpo highest
# numbers.sort(reverse = True)
# print(sorted(numbers))
# numbers.reverse()

# print(numbers[1:3]) # start stop
# print(numbers[::-1]) # step

# for number in numbers:
#     print(number)

# print(numbers)

# digits = [-1, 0, 4, -5, 3, -6]
# positive = []
# parni = []
# for digit in digits:
#     if digit > 0:
#         positive.append(digit)
#     if digit % 2 == 0:
#         parni.append(digit)
# print(positive)

#tuple - кортеж
# rgb = (255, 0, 0)
# r, g, b = rgb
# print(r, g, b)

# data = ()
# a = (1,)
# # rgb[1] = 255

# point = (4, -6)
# point = point + (4,)
# print(point)
# a = (30, 40)
# b = (50, 60)
# c = a + b
# c = a[:1] + b[::]
# print(c)
# c.count()
# c.index()
# len()

# # set - множина order of UNIQUE elements. goes in alphabet order and yara yara
# subjects = {"Python", "HTML", "CSS", "JavaScript"}
# print(subjects)
# data = {}
# print(type(data))
# data2 = set()
# data2.add("Python")
# data2.update(["HTML", "CSS"])

# data2.remove("HTML") # error if not there
# data2.discard("HTML") # no error
# deleted = data2.pop()
# # clear()
# if "Python" in subjects:
#     print("Python")
# print(data2)

# dictionaries
# student = {
#     "name": "Ivan",
#     "age": "18"
# }
# names = ["Ivan", "Olha", "Marina", "Stas", "Vadym", "Irina"]
# new_names = set(names)
# print(new_names)

# names1 = {"Ivan", "Marina"}
# names2 = {"Stas", "Vadym", "Ivan"}

# names3 = names1 | names2
# names4 = names1 & names2
# names5 = names1 - names2
# names6 = names2 - names1 # not the same as above

# print(names3)
# print(names4)
# print(names5)
# print(names6)

# products = ["bread", "milk", "apple", "banana"]
# prices = [30, 50, 50, 80]

# prices = {
#     "bread": 50,
#     "milk": 70,
#     "apple": 70,
#     "banana": 90
# }
# student = {}
# student = dict()

# prices["tea"] = 75
# prices["bread"] = 35

# prices.update(
#     {
#         "juice": 50,
#         "coffee": 70
#     }
# )
# deleted = prices.pop("milk")
# del prices["milk"]

# .get()
# .value()
# .key()
# .items()

# for key, value in prices():
#     print(key)
#     print(value)

# print(prices["bread"])
# print(prices)
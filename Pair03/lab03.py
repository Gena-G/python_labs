# # 1
# Pyth = input("Text: ").lower()
# PSymbols = len(Pyth)
# PLetters = 0
# Numbers = 0
# Spaces = 0
# Vowels = 0
# gol = "aeiou"
# for ch in Pyth:
#     if ch.isalpha():
#         PLetters += 1
#     if ch.isdigit():
#         Numbers += 1
#     if ch.isspace(): # Just found out this specific command exists. Why?
#         Spaces += 1
#     if ch in gol:
#         Vowels += 1
# Wordies = Pyth.split()
# Words = len(Wordies)
# print(
#     "Символів: " + str(PSymbols),
#     "Літер: " + str(PLetters),
#     "Цифр: " + str(Numbers),
#     "Пробілів: " + str(Spaces),
#     "Голосних: " + str(Vowels),
#     "Слів: " + str(Words),
#     sep="\n",
# )


# # 2
# Name = input("Name: ").lower().title()
# NWords = Name.split()
# Intials = []
# if len(NWords) == 3:
#     for word in NWords[1:3]:
#         for char in word:
#             if char.isupper():
#                 Intials.append(char)
#     print(NWords[0], Intials[0] + "." + Intials[1] + ".")
# else:
#     print("No")


# # 3
# s1 = input("Введіть перший рядок: ").strip().lower()
# s2 = input("Введіть другий рядок: ").strip().lower()

# c1 = "".join(s1.split())
# c2 = "".join(s2.split())

# anagram = len(c1) == len(c2)

# if anagram:
#     temp2 = c2
#     for char in c1:
#         if char in temp2:
#             temp2 = temp2.replace(char, "", 1)
#         else:
#             anagram = False
#             break
#     if len(temp2) != 0:
#         anagram = False

# if anagram:
#     print("Рядки є анаграмами.")
# else:
#     print("Рядки не є анаграмами.")


# # 4
# text = input("Sentance: ")
# twords = text.split()

# max_len = len(twords[0])
# min_len = len(twords[0])

# for w in twords:
#     if len(w) > max_len:
#         max_len = len(w)
#     if len(w) < min_len:
#         min_len = len(w)

# l_words = []
# s_words = []

# for w in twords:
#     if len(w) == max_len and w not in l_words:
#         l_words.append(w)
#     if len(w) == min_len and w not in s_words:
#         s_words.append(w)

# unique = []
# for w in twords:
#     w2 = w.lower()
#     if w2 not in unique:
#         unique.append(w2)

# print(
#     "Найдовші: " + ", ".join(l_words),
#     "Найкоротші: " + ", ".join(s_words),
#     "Унікальних слів: " + str(len(unique)),
#     sep="\n",
# )

# t = input("Яке слово замінити: ")
# rep = input("На яке слово замінити: ")

# newtext = text.replace(t, rep)
# print("Після заміни: " + newtext) # All of this is probably so unoptimized.
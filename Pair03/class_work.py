# name = "TheG"
# age = "16"
# print(len(name))
# print(name[0])
# print(name[4])
# print(name[len(name) - 1])

# text = input()
# if len(text) > 0:
#     print(text[0])
# else:
#     print("Aw hell naw dog ya tweaking")

# text = "hello world"
# # print(text[:5]) # everything to 5.
# # print(text[6:]) # From 6 to end
# # print(text[::2])
# # print(text[::-1])

# # string is the unchangeable type.

# print(text.upper())
# print(text.lower())
# print(text.title()) # all words start with an upper letter
# print(text.capitalize()) # Only 1. ^


# text = "      Python       "
# print(text.lstrip()) # left
# print(text.rstrip()) # right
# print(text.strip()) # Bye bye to spaces

# user_login = "admin"
# login = input("Type in login: ").strip().lower()
# if user_login == login:
#     print("Welcome " + user_login)

# text = "Python"
# for char in text:
#     print(char)

# password = input()
# digits = 0
# u_letter = 0
# if len(password) >= 8:
#     for char in password:
#         if char.isdigit():
#             digits += 1
#         if char.isupper():
#             u_letter += 1
#     if digits >= 2 and u_letter >= 2:
#         print("Password is secure")
#     else:
#         print("Password is unsecure about it's feelings.")
# else:
#     print("Ur abotta to get hacked. 8 digits+")

# password.isdigit()
# password.isupper()
# password.islower()
# password.isalpha()
# password.isalnum()

# golosni = "aeyuio"
# count = 0
# text = input("Input text: ").lower
# for ch in text:
#     if ch in text:
#         count += 1
# print(count)

# text = "Hello world!! PYTHON IS LE BESt!!"
# words = text.split()
# print(words)
# result = "-".join(words)
# print(result)
# new_text = text.replace("Python", "JavaScript")

# text = input().lower().strip()
# if text == text[::-1]:
#     print("Palindrom")
# else: print("nuhuh")

# text = input().strip().lower()
# words = text.split()
# max_w = words[0]
# for w in words:
#     if len(max_w) < len(w):
#         max_w = w
# print(max_w)
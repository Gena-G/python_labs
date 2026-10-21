# book_dict = {
#     "title": "Кобзар",
#     "author": "Тарас Шевченко",
#     "copies": 15
# }
# print(book_dict["title"])

# class Book:
#     def __init__(self, title, price, copies): #Starts the work of this class.
#         self.title = title
#         self.price = price
#         self.copies = copies
#     def avaliable(self):
#         return self.copies > 0

# book1 = Book("Кобзар", 450, 15)
# book2 = Book("Лісова пісня", 500, 0)
# print("First:", book1.title)
# print("First cost:", book1.price)
# print("Second:", book2.title, book2.price)
# print(f"Avaliable - {book1.avaliable()}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def info(self):
        print(f"Rectangle size: {self.width}x{self.height}")
        print(f"S={self.area()}")
        print(f"P={self.perimeter()}")

a = int(input("Type in width of Rectangle:"))
b = int(input("Type in height of Rectangle:"))
rectangle = Rectangle(a,b)
print(f"info - {rectangle.info()}")
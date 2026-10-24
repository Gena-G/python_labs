class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f'name {self.name}.'
    
class Student(Person):
    def __init__(self, name, group):
        super().__init__(name) # hacking into parent class.... 50%.... 70%... 0%....
        self.group = group
    def info(self):
        return f'name {self.name}, {self.group}'

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'Name {self.name}, Subject = {self.subject}'

# person = Person("Vadym")
# student = Student("Liza", "10ME")

people = [Person("Vadym"), Student("Liza", "10ME"), Teacher('Ivan', 'IT')]
for person in people:
    print(person.info)
person2 = Person("Illia")
print(isinstance(person2, Person))
# print(person.info())
# print(student.info())
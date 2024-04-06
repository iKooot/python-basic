class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender.lower()
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nGender: {self.gender}\nAge: {self.age}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}\nRecord book: {self.record_book}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
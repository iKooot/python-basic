class GroupSizeExceededException(Exception):
    def __init__(self, message="Group size exceeds the maximum limit"):
        self.message = message
        super().__init__(self.message)


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


class Group:
    MAX_GROUP_SIZE = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        print(len(self.group))
        if len(self.group) >= self.MAX_GROUP_SIZE:
            raise GroupSizeExceededException()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is None:
            return "I cant remove the student! Because i cant find him"
        self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n '.join([name.first_name for name in self.group])
        return f'Number:{self.number}\n {all_students}'

gr = Group('PD1')

for el in range(11):
    st = Student('Male', el, 'example', 'example', 'example')
    gr.add_student(st)




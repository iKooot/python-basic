from exaption import GroupSizeExceededException

class Group:
    MAX_GROUP_SIZE = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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
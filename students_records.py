#from csv_handler import CSVHandler
#rom student import Student

class StudentRecords:
    def __init__(self):
        self.students = {}

    def add_student(self, email, first_name, last_name):
        if email not in self.students:
            self.students[email] = Student(email, first_name, last_name)

    def delete_student(self, email):
        if email in self.students:
            del self.students[email]

    def update_student(self, email, new_first_name, new_last_name):
        if email in self.students:
            self.students[email].first_name = new_first_name
            self.students[email].last_name = new_last_name
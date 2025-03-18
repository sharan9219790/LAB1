class Student:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.courses = {}  # {course_id: (grade, marks)}

    def add_course(self, course_id, grade, marks):
        self.courses[course_id] = (grade, marks)

    def update_grade(self, course_id, new_grade, new_marks):
        if course_id in self.courses:
            self.courses[course_id] = (new_grade, new_marks)

    def get_average_marks(self):
        return sum(m for _, m in self.courses.values()) / len(self.courses) if self.courses else 0

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) - Courses: {self.courses}"

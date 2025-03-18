class Course:
    def __init__(self, course_id, course_name, professor_id, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.professor_id = professor_id
        self.credits = credits
        self.students = {}  # {student_email: (grade, marks)}

    def assign_grade(self, student_email, grade, marks):
        self.students[student_email] = (grade, marks)

    def __str__(self):
        return f"{self.course_name} (ID: {self.course_id}, Professor: {self.professor_id}, Credits: {self.credits})"

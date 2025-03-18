class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def __str__(self):
        return f"Grade {self.grade} (Range: {self.marks_range})"

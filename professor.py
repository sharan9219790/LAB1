class Professor:
    def __init__(self, professor_id, name, email, rank):
        self.professor_id = professor_id
        self.name = name
        self.email = email
        self.rank = rank
        self.courses = []  # List of course IDs

    def add_course(self, course_id):
        self.courses.append(course_id)

    def __str__(self):
        return f"Professor {self.name} ({self.email}) - Courses: {self.courses}"

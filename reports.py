class Reports:
    @staticmethod
    def student_report(email, students):
        """Generate a report for a specific student."""
        student = students.get(email)  # Correctly fetch student from dictionary
        if student:
            return f"📄 Student Report: {student}"
        return "❌ Student not found!"

    @staticmethod
    def course_report(course_id, students):
        """Generate a course-wise report listing all students."""
        report = f"📊 Course {course_id} Report:\n"
        for student in students.values():
            if course_id in student.courses:
                report += f"{student.first_name} {student.last_name}: {student.courses[course_id]}\n"
        return report if report != f"📊 Course {course_id} Report:\n" else "❌ No students found for this course."

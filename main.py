from student import Student
from professor import Professor
from course import Course
from grades import Grades
from login_user import LoginUser
from csv_handler import CSVHandler
from reports import Reports
from stat_all import Stats  

def search_student(email, students):
    """Search for a student by email and display their details."""
    student = students.get(email)
    if student:
        print(f"Found Student: {student}")
    else:
        print("Student not found!")

def sort_students_by_marks(students, course_id):
    """Sort students by their marks in a given course."""
    sorted_students = sorted(students.values(), key=lambda s: s.courses.get(course_id, (None, 0))[1], reverse=True)
    print(f"📊 Sorted Students for {course_id}:")
    for student in sorted_students:
        print(student)

def main():
    # Load student data from CSV
    students = {}
    student_data = CSVHandler.load_from_csv("data/students.csv")
    
    for row in student_data[1:]:  # Skip header row
        if len(row) != 6:
            print(f"Skipping malformed row: {row}")
            continue

        email, first_name, last_name, course_id, grade, marks = row
        if email not in students:
            students[email] = Student(email, first_name, last_name)
        students[email].add_course(course_id, grade, int(marks))

    print(f"Successfully loaded {len(students)} student records.")

    # Example: Search for a student
    search_student("alice@example.com", students)

    # Example: Sort students by marks in a course
    sort_students_by_marks(students, "DATA200")

    #Example: Generate reports
    print(Reports.student_report("alice@example.com", students))
    print(Reports.course_report("DATA200", students))

    #Example: Calculate course statistics
    print(Stats.get_course_statistics(students, "DATA200"))

    #Example: Add a new student
    new_student = Student("bob@example.com", "Bob", "Johnson")
    new_student.add_course("DATA201", "B+", 88)
    students[new_student.email] = new_student
    print(f"Added Student: {new_student}")

    # Save updated student data back to CSV
    updated_data = [["Email", "First Name", "Last Name", "Course ID", "Grade", "Marks"]]
    for student in students.values():
        for course_id, (grade, marks) in student.courses.items():
            updated_data.append([student.email, student.first_name, student.last_name, course_id, grade, marks])

    CSVHandler.save_to_csv("data/students.csv", updated_data)
    print(" Student data updated successfully!")

    #  Example: User Login Test
    LoginUser.register_user("admin@example.com", "SecurePass123!", "admin")
    LoginUser.authenticate("admin@example.com", "SecurePass123!")

if __name__ == "__main__":
    main()

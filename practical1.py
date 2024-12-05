def input_students(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students
def input_courses(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(courses, students):
    marks = {}
    for course in courses:
        course_name = course[1]
        marks[course_name] = {}
        print(f"Input marks for course: {course_name}")
        for student in students:
            student_id, student_name, _ = student
            mark = float(input(f"Enter marks for {student_name} (Student ID: {student_id}): "))
            marks[course_name][student_id] = mark  # Store marks using student ID as key
    return marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(marks, students, course_name):
    print(f"Marks for course: {course_name}")
    for student in students:
        student_id, student_name, _ = student
        mark = marks.get(course_name, {}).get(student_id, "No marks available")
        print(f"Student: {student_name}, Marks: {mark}")

def main():
    num_students = int(input("Enter number of students: "))
    students = input_students(num_students)
    num_courses = int(input("Enter number of courses: "))
    courses = input_courses(num_courses)
    marks = input_marks(courses, students)
    list_courses(courses)
    list_students(students)
    course_to_check = input("Enter the course name to show marks: ")
    show_student_marks(marks, students, course_to_check)
if __name__ == "__main__":
    main()

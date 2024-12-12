class Person:
    def __init__(self, person_id, name, dob):
        self._person_id = person_id
        self._name = name
        self._dob = dob

    def input(self):
        self._person_id = input("Enter ID: ")
        self._name = input("Enter name: ")
        self._dob = input("Enter Date of Birth (DD/MM/YYYY): ")

    def list(self):
        print(f"ID: {self._person_id}, Name: {self._name}, DoB: {self._dob}")

    def get_id(self):
        return self._person_id

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)

class Course:
    def __init__(self, course_id, course_name):
        self._course_id = course_id
        self._course_name = course_name

    def input(self):
        self._course_id = input("Enter course ID: ")
        self._course_name = input("Enter course name: ")

    def list(self):
        print(f"ID: {self._course_id}, Name: {self._course_name}")

    def get_name(self):
        return self._course_name

class School:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}

    def add_person(self, person):
        self._students.append(person)

    def add_course(self, course):
        self._courses.append(course)

    def input_students(self, num_students):
        for _ in range(num_students):
            student = Student(None, None, None)
            student.input()
            self.add_person(student)

    def input_courses(self, num_courses):
        for _ in range(num_courses):
            course = Course(None, None)
            course.input()
            self.add_course(course)

    def input_marks(self):
        for course in self._courses:
            self._marks[course.get_name()] = {}
            print(f"Input marks for course: {course.get_name()}")
            for student in self._students:
                mark = float(input(f"Enter marks for {student._name} (Student ID: {student.get_id()}): "))
                self._marks[course.get_name()][student.get_id()] = mark

    def list_courses(self):
        print("Courses:")
        for course in self._courses:
            course.list()

    def list_students(self):
        print("Students:")
        for student in self._students:
            student.list()

    def show_student_marks(self, course_name):
        print(f"Marks for course: {course_name}")
        for student in self._students:
            mark = self._marks.get(course_name, {}).get(student.get_id(), "No marks available")
            print(f"Student: {student._name}, Marks: {mark}")

def main():
    school = School()

    num_students = int(input("Enter number of students: "))
    school.input_students(num_students)

    num_courses = int(input("Enter number of courses: "))
    school.input_courses(num_courses)

    school.input_marks()

    school.list_courses()
    school.list_students()

    course_to_check = input("Enter the course name to show marks: ")
    school.show_student_marks(course_to_check)

if __name__ == "__main__":
    main()

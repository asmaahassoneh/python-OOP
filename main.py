from school import Student, Professor, GraduateStudent, Course


def main() -> None:
    try:
        student1 = Student("Asmaa", "101", [90, 95])
        student2 = Student("Tala", "102", [90])
        student3 = Student("Ali", "103", [88, 95])
        student4 = Student("Ahmad", "104", [65, 70])

        grad_student = GraduateStudent("Lina", "201", [92, 94], "AI in Education")

        students = [student1, student2, student3, student4, grad_student]

        professor = Professor("Dr. Anas Toma")

        professor.assign_grade(student1, 100)
        professor.assign_grade(student2, 85)
        professor.assign_grade(grad_student, 98)

        course = Course("Python OOP")

        for student in students:
            course.add_student(student)

        print("=== Students ===")
        for student in students:
            print(student)

        print("\n=== Individual Averages ===")
        for student in students:
            print(f"{student.name}: {student.get_average()}")

        print("\n=== GPA ===")
        for student in students:
            print(f"{student.name}: {student.gpa}")

        print("\n=== Course Info ===")
        print(course)
        print(f"Course Average: {course.get_average_grade()}")

        print("\n=== Encapsulation Test ===")
        grades_copy = student1.grades
        grades_copy.append(0)

        print("Modified external list:", grades_copy)
        print("Actual student grades:", student1.grades)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

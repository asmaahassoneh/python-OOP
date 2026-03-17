from student import Student


def main() -> None:
    try:
        # Create students
        student1 = Student("Asmaa", "101", [90, 95])
        student2 = Student("Tala", "102", [90])
        student3 = Student("Ali", "103", [88, 95])
        student4 = Student("Ahmad", "104", [65, 70])

        students = [student1, student2, student3, student4]

        student1.add_grade(100)

        print("=== Students ===")
        for student in students:
            print(student)

        print("\n=== Averages ===")
        for student in students:
            print(f"{student.name}: {student.get_average()}")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
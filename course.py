from student import Student


class Course:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Course name must be a non-empty string")

        self.name = name
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise ValueError("Course can only contain Student objects")

        if student in self.students:
            raise ValueError("Student already enrolled in the course")

        self.students.append(student)

    def get_average_grade(self) -> float:
        if not self.students:
            return 0.0

        total = sum(student.get_average() for student in self.students)
        return round(total / len(self.students), 2)

    def __str__(self) -> str:
        return f"Course({self.name}, Students: {len(self.students)})"

    def __repr__(self) -> str:
        return f"Course(name={self.name!r}, students={self.students!r})"

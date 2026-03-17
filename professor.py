from student import Student


class Professor:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        self.name = name.strip()

    def assign_grade(self, student: Student, grade: float) -> None:
        if not isinstance(student, Student):
            raise ValueError("Professor can only assign grades to Student objects")
        student.add_grade(grade)

    def __repr__(self) -> str:
        return f"Professor(name={self.name!r})"

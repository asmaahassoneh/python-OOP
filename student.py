class Student:
    used_ids = set()

    def __init__(self, name: str, student_id: str, grades: list[float]) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string")

        name = name.strip()
        student_id = student_id.strip()

        if student_id in Student.used_ids:
            raise ValueError("Student ID must be unique")

        if not isinstance(grades, list) or not grades:
            raise ValueError("Grades must be a non-empty list")

        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise ValueError("Each grade must be a number")
            if not 0 <= grade <= 100:
                raise ValueError("Each grade must be between 0 and 100")

        self._name = name
        self._student_id = student_id
        self._grades = grades.copy()

        Student.used_ids.add(student_id)

    @property
    def name(self) -> str:
        return self._name

    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def grades(self) -> list[float]:
        return self._grades.copy()

    def add_grade(self, grade: float) -> None:
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")

        self._grades.append(grade)

    def get_average(self) -> float:
        return round(sum(self._grades) / len(self._grades), 2)

    def __str__(self) -> str:
        return (
            f"Student(ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Grades: {self.grades}, "
            f"Average: {self.get_average()})"
        )

    def __repr__(self) -> str:
        return (
            f"Student(name={self.name!r}, "
            f"student_id={self.student_id!r}, "
            f"grades={self.grades!r})"
        )

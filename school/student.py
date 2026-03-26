class Student:
    used_ids = set()

    def __init__(
        self,
        name: str,
        student_id: str,
        grades: list[float],
    ) -> None:
        self.name = name
        self.student_id = student_id
        self._grades = []

        if not isinstance(grades, list) or not grades:
            raise ValueError("Grades must be a non-empty list")

        for grade in grades:
            self.add_grade(grade)

        Student.used_ids.add(self._student_id)

    @classmethod
    def from_single_grade(
        cls,
        name: str,
        student_id: str,
        grade: float,
    ) -> "Student":
        return cls(name, student_id, [grade])

    @staticmethod
    def is_passing(grade: float) -> bool:
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        return grade >= 60

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Student ID must be a non-empty string")

        value = value.strip()

        if hasattr(self, "_student_id"):
            if value != self._student_id and value in Student.used_ids:
                raise ValueError("Student ID must be unique")
            Student.used_ids.discard(self._student_id)
        else:
            if value in Student.used_ids:
                raise ValueError("Student ID must be unique")

        self._student_id = value

    @property
    def grades(self) -> list[float]:
        return self._grades.copy()

    @property
    def gpa(self) -> float:
        return round((self.get_average() / 100) * 4, 2)

    def add_grade(self, grade: float) -> None:
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")

        self._grades.append(grade)

    def get_average(self) -> float:
        return round(sum(self._grades) / len(self._grades), 2)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id

    def __str__(self) -> str:
        return (
            f"Student(ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Grades: {self.grades}, "
            f"Average: {self.get_average()}, "
            f"GPA: {self.gpa})"
        )

    def __repr__(self) -> str:
        return (
            f"Student(name={self.name!r}, "
            f"student_id={self.student_id!r}, "
            f"grades={self.grades!r})"
        )

from school.student import Student


class GraduateStudent(Student):
    def __init__(
        self, name: str, student_id: str, grades: list[float], thesis_title: str
    ):
        super().__init__(name, student_id, grades)

        if not isinstance(thesis_title, str) or not thesis_title.strip():
            raise ValueError("Thesis title must be a non-empty string")

        self.thesis_title = thesis_title.strip()

    def __str__(self) -> str:
        return super().__str__() + f", Thesis: {self.thesis_title}"

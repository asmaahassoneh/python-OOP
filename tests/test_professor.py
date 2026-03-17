import pytest

from student import Student
from professor import Professor


@pytest.fixture(autouse=True)
def reset_student_ids():
    Student.used_ids.clear()


def test_create_professor_success():
    professor = Professor("Dr. Haneen")

    assert professor.name == "Dr. Haneen"


def test_invalid_professor_name():
    with pytest.raises(ValueError, match="Name must be a non-empty string"):
        Professor("")


def test_assign_grade_success():
    professor = Professor("Dr. Haneen")
    student = Student("Asmaa", "101", [90, 95])

    professor.assign_grade(student, 100)

    assert student.grades == [90, 95, 100]


def test_assign_grade_updates_average():
    professor = Professor("Dr. Haneen")
    student = Student("Asmaa", "101", [80, 90])

    professor.assign_grade(student, 100)

    assert student.get_average() == 90.0


def test_assign_invalid_grade_type():
    professor = Professor("Dr. Haneen")
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Grade must be a number"):
        professor.assign_grade(student, "A")


def test_assign_invalid_grade_range():
    professor = Professor("Dr. Haneen")
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Grade must be between 0 and 100"):
        professor.assign_grade(student, 120)


def test_assign_grade_invalid_student():
    professor = Professor("Dr. Haneen")

    with pytest.raises(ValueError, match="Student objects"):
        professor.assign_grade("not a student", 90)

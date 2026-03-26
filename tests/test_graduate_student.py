import pytest

from school.student import Student
from school.graduate_student import GraduateStudent


@pytest.fixture(autouse=True)
def reset_student_ids():
    Student.used_ids.clear()


def test_create_graduate_student_success():
    student = GraduateStudent(
        "Asmaa",
        "201",
        [90, 95],
        "AI in Education",
    )

    assert student.name == "Asmaa"
    assert student.student_id == "201"
    assert student.grades == [90, 95]
    assert student.thesis_title == "AI in Education"


def test_graduate_student_is_student():
    student = GraduateStudent(
        "Asmaa",
        "201",
        [90, 95],
        "AI in Education",
    )

    assert isinstance(student, GraduateStudent)
    assert isinstance(student, Student)


def test_invalid_thesis_title():
    with pytest.raises(
        ValueError,
        match="Thesis title must be a non-empty string",
    ):
        GraduateStudent("Asmaa", "201", [90, 95], "")


def test_graduate_student_inherits_add_grade():
    student = GraduateStudent(
        "Asmaa",
        "201",
        [90, 95],
        "AI in Education",
    )

    student.add_grade(100)

    assert student.grades == [90, 95, 100]


def test_graduate_student_get_average():
    student = GraduateStudent(
        "Asmaa",
        "201",
        [90, 95, 100],
        "AI in Education",
    )

    assert student.get_average() == 95.0


def test_graduate_student_str_method():
    student = GraduateStudent(
        "Asmaa",
        "201",
        [90, 95],
        "AI in Education",
    )

    assert str(student) == (
        "Student(ID: 201, Name: Asmaa, Grades: [90, 95], Average: 92.5, GPA: 3.7), "
        "Thesis: AI in Education"
    )


def test_graduate_student_repr_inherits():
    student = GraduateStudent("Asmaa", "201", [90, 95], "AI")

    assert "GraduateStudent" not in repr(student)

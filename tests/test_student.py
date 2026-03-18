import pytest
from student import Student


@pytest.fixture(autouse=True)
def reset_student_ids():
    Student.used_ids.clear()


def test_create_student_success():
    student = Student("Asmaa", "101", [90, 95])

    assert student.name == "Asmaa"
    assert student.student_id == "101"
    assert student.grades == [90, 95]


def test_add_grade_success():
    student = Student("Asmaa", "101", [90, 95])

    student.add_grade(100)

    assert student.grades == [90, 95, 100]


def test_get_average():
    student = Student("Asmaa", "101", [90, 95, 100])

    assert student.get_average() == 95.0


def test_str_method():
    student = Student("Asmaa", "101", [90, 95])

    assert str(student) == (
        "Student(ID: 101, Name: Asmaa, Grades: [90, 95], Average: 92.5)"
    )


def test_invalid_name():
    with pytest.raises(ValueError, match="Name must be a non-empty string"):
        Student("", "101", [90, 95])


def test_invalid_student_id():
    with pytest.raises(ValueError, match="Student ID must be a non-empty string"):
        Student("Asmaa", "", [90, 95])


def test_duplicate_student_id():
    Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Student ID must be unique"):
        Student("Ali", "101", [80, 85])


def test_empty_grades():
    with pytest.raises(ValueError, match="Grades must be a non-empty list"):
        Student("Asmaa", "101", [])


def test_invalid_grade_in_init_type():
    with pytest.raises(ValueError, match="Each grade must be a number"):
        Student("Asmaa", "101", [90, "A"])


def test_invalid_grade_in_init_range():
    with pytest.raises(ValueError, match="Each grade must be between 0 and 100"):
        Student("Asmaa", "101", [90, 150])


def test_add_invalid_grade_type():
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Grade must be a number"):
        student.add_grade("A")


def test_add_invalid_grade_range():
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Grade must be between 0 and 100"):
        student.add_grade(120)


def test_grades_list_is_copied():
    grades = [90, 95]
    student = Student("Asmaa", "101", grades)

    grades.append(100)

    assert student.grades == [90, 95]


def test_integer_grades_allowed():
    student = Student("Asmaa", "101", [90, 100, 80])

    assert student.get_average() == 90.0


def test_float_grades_allowed():
    student = Student("Asmaa", "101", [89.5, 90.5])

    assert student.get_average() == 90.0


def test_boundary_grades():
    student = Student("Asmaa", "101", [0, 100])

    assert student.grades == [0, 100]
    assert student.get_average() == 50.0


def test_name_and_id_are_stripped():
    student = Student("  Asmaa  ", " 101 ", [90, 95])

    assert student.name == "Asmaa"
    assert student.student_id == "101"


def test_average_is_rounded_to_two_decimals():
    student = Student("Asmaa", "101", [90, 91, 92])

    assert student.get_average() == 91.0


def test_repr_method():
    student = Student("Asmaa", "101", [90, 95])

    assert repr(student) == ("Student(name='Asmaa', student_id='101', grades=[90, 95])")


def test_student_equality_different_ids():
    s1 = Student("Asmaa", "101", [90])
    s2 = Student("Ali", "102", [80])

    assert s1 != s2


def test_student_equality_same_object():
    s1 = Student("Asmaa", "101", [90])

    assert s1 == s1


def test_student_equality_with_non_student():
    s1 = Student("Asmaa", "101", [90])

    assert s1 != "not a student"


def test_gpa_property():
    student = Student("Asmaa", "101", [100, 100])

    assert student.gpa == 4.0

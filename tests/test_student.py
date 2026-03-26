import pytest
from school.student import Student


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
        "Student(ID: 101, Name: Asmaa, Grades: [90, 95], Average: 92.5, GPA: 3.7)"
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
    with pytest.raises(ValueError, match="Grade must be a number"):
        Student("Asmaa", "101", [90, "A"])


def test_invalid_grade_in_init_range():
    with pytest.raises(ValueError, match="Grade must be between 0 and 100"):
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


def test_from_single_grade_classmethod():
    student = Student.from_single_grade("Asmaa", "101", 95)

    assert isinstance(student, Student)
    assert student.name == "Asmaa"
    assert student.student_id == "101"
    assert student.grades == [95]


def test_is_passing_true():
    assert Student.is_passing(60) is True
    assert Student.is_passing(85) is True


def test_is_passing_false():
    assert Student.is_passing(59) is False
    assert Student.is_passing(0) is False


def test_is_passing_invalid_type():
    with pytest.raises(ValueError, match="Grade must be a number"):
        Student.is_passing("A")


def test_name_setter_success():
    student = Student("Asmaa", "101", [90, 95])

    student.name = "  Ali  "

    assert student.name == "Ali"


def test_name_setter_invalid():
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Name must be a non-empty string"):
        student.name = ""


def test_student_id_setter_success():
    student = Student("Asmaa", "101", [90, 95])

    student.student_id = "202"

    assert student.student_id == "202"


def test_student_id_setter_strips_spaces():
    student = Student("Asmaa", "101", [90, 95])

    student.student_id = " 202 "

    assert student.student_id == "202"


def test_student_id_setter_invalid():
    student = Student("Asmaa", "101", [90, 95])

    with pytest.raises(ValueError, match="Student ID must be a non-empty string"):
        student.student_id = ""


def test_student_id_setter_duplicate():
    student1 = Student("Asmaa", "101", [90, 95])
    student2 = Student("Ali", "102", [80, 85])

    with pytest.raises(ValueError, match="Student ID must be unique"):
        student2.student_id = "101"


def test_gpa_updates_automatically_after_adding_grade():
    student = Student("Asmaa", "101", [100])

    assert student.gpa == 4.0

    student.add_grade(50)

    assert student.gpa == 3.0

import pytest

from student import Student
from course import Course


@pytest.fixture(autouse=True)
def reset_student_ids():
    Student.used_ids.clear()


def test_create_course_success():
    course = Course("Python OOP")

    assert course.name == "Python OOP"
    assert course.students == []


def test_invalid_course_name():
    with pytest.raises(
        ValueError,
        match="Course name must be a non-empty string",
    ):
        Course("")


def test_add_student_success():
    course = Course("Python OOP")
    student = Student("Asmaa", "101", [90, 95])

    course.add_student(student)

    assert course.students == [student]


def test_add_multiple_students():
    course = Course("Python OOP")
    student1 = Student("Asmaa", "101", [90, 95])
    student2 = Student("Ali", "102", [80, 85])

    course.add_student(student1)
    course.add_student(student2)

    assert course.students == [student1, student2]


def test_course_contains_student_objects():
    course = Course("Python OOP")
    student = Student("Asmaa", "101", [90, 95])

    course.add_student(student)

    assert isinstance(course.students[0], Student)


def test_get_average_grade_empty_course():
    course = Course("Python OOP")

    assert course.get_average_grade() == 0.0


def test_get_average_grade_with_one_student():
    course = Course("Python OOP")
    student = Student("Asmaa", "101", [90, 95])

    course.add_student(student)

    assert course.get_average_grade() == 92.5


def test_get_average_grade_with_multiple_students():
    course = Course("Python OOP")
    student1 = Student("Asmaa", "101", [90, 95])
    student2 = Student("Ali", "102", [80, 100])

    course.add_student(student1)
    course.add_student(student2)

    assert course.get_average_grade() == 91.25


def test_course_str_method():
    course = Course("Python OOP")

    assert str(course) == "Course(Python OOP, Students: 0)"


def test_course_str_method_after_adding_students():
    course = Course("Python OOP")
    student1 = Student("Asmaa", "101", [90, 95])
    student2 = Student("Ali", "102", [80, 100])

    course.add_student(student1)
    course.add_student(student2)

    assert str(course) == "Course(Python OOP, Students: 2)"


def test_add_invalid_student_type():
    course = Course("Python OOP")

    with pytest.raises(
        ValueError,
        match="Course can only contain Student objects",
    ):
        course.add_student("not a student")


def test_add_none_as_student():
    course = Course("Python OOP")

    with pytest.raises(
        ValueError,
        match="Course can only contain Student objects",
    ):
        course.add_student(None)


def test_add_duplicate_student():
    course = Course("Python OOP")
    student = Student("Asmaa", "101", [90, 95])

    course.add_student(student)

    with pytest.raises(ValueError, match="already enrolled"):
        course.add_student(student)


def test_course_average_rounding():
    course = Course("Python OOP")
    student1 = Student("A", "101", [90, 91])
    student2 = Student("B", "102", [89, 90])

    course.add_student(student1)
    course.add_student(student2)

    assert course.get_average_grade() == 90.0

# 🎓 Student Management System (OOP)

This project demonstrates Object-Oriented Programming (OOP) concepts in Python by modeling a simple student management system.

---

## 📌 Features

- Create and manage students with grades
- Calculate student averages and GPA
- Support for graduate students with thesis titles
- Professor assigns grades to students
- Course contains multiple students using composition
- Course supports iteration
- Student equality comparison based on ID
- Structured into a Python package (`school`)
- Full test coverage using **pytest**
- Dependency management using `requirements.txt`

---

## 🧱 Project Structure
```
```text
OOP/
├── main.py
├── requirements.txt
├── school/
│   ├── __init__.py
│   ├── student.py
│   ├── graduate_student.py
│   ├── professor.py
│   └── course.py
└── tests/
│   ├── test_student.py
│   ├── test_graduate_student.py
│   ├── test_professor.py
│   └── test_course.py
│
├── .gitignore
└── README.md
```

---

## 🧠 OOP Concepts Used

### 1. Encapsulation
- Private attributes (`_name`, `_student_id`, `_grades`)
- Access via `@property`
- Grades list is protected using `.copy()`

### 2. Inheritance
- `GraduateStudent` extends `Student`
- Adds `thesis_title`

### 3. Method Overriding
- `GraduateStudent.__str__()` extends base behavior

### 4. Composition
- `Course` contains a list of `Student` objects

---

## 👨‍🎓 Classes Overview

### Student
- Attributes: `name`, `student_id`, `grades`
- Methods:
  - `add_grade()`
  - `get_average()`
  - `__str__()`
- Property:
  - `gpa`

### GraduateStudent
- Inherits from `Student`
- Adds:
  - `thesis_title`

### Professor
- Assigns grades to students using:
  - `assign_grade(student, grade)`

### Course
- Contains students
- Methods:
  - `add_student()`
  - `get_average_grade()`
- Supports iteration:
  - `for student in course`
---

## ▶️ How to Run

Run the main program:

```bash
python main.py
```
---
# Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run linting and formatting:

```bash
flake8 .
black .
```

## 🧪 Running Tests

```bash
python -m pytest 
```
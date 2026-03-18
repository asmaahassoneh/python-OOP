# 🎓 Student Management System (OOP)

This project demonstrates Object-Oriented Programming (OOP) concepts in Python by modeling a simple student management system.

---

## 📌 Features

- Create and manage students with grades
- Calculate student averages
- Support for graduate students with thesis titles
- Professor assigns grades to students
- Course contains multiple students (composition)
- Full test coverage using **pytest**

---

## 🧱 Project Structure
.
├── student.py
├── graduate_student.py
├── professor.py
├── course.py
├── main.py
├── tests/
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

Install required tools:

```bash
pip install flake8 black pytest
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
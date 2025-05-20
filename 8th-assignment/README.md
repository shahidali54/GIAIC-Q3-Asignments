# 🎓 Student Management System (CLI Based)

This is a **Command-Line Interface (CLI)** based Student Management System built using Python and the [Rich](https://github.com/Textualize/rich) library for beautiful formatting and user interaction.

## 🚀 Features

- 🔐 **OOP Principles**: Uses Inheritance, Encapsulation, and proper class structures.
- 📝 **Student Management**:
  - Add a student with name, roll number, and marks.
  - View all students in a styled table.
  - Search a student by roll number.
  - Update student marks with validation.
  - Calculate class average.
- 👨‍🏫 **Teacher Management**:
  - Add a teacher with name, employee ID, and subject.
  - View all teachers in a styled table.
- 💾 **Data Persistence**: All data is saved and loaded from a JSON file (`student_data.json`).
- ✨ **Rich UI in Terminal**: Styled prompts, tables, spinners, and colored messages using the Rich library.

## 📦 Requirements

- Python 3.7+
- `rich` library

Install required package via pip:

```bash
pip install rich
```

## ▶️ How to Run

```bash
python main.py
```

Make sure `main.py` is the file where the code is saved.

## 📁 File Structure

```
project/
│
├── main.py              # Main CLI application
├── student_data.json    # Auto-generated database file
└── README.md            # This file
```

## 🛠️ Object-Oriented Concepts Used

- **Encapsulation**: Private attributes with getters/setters
- **Inheritance**: `Student` and `Teacher` inherit from `Person`
- **Abstraction**: Data is handled via class methods
- **Polymorphism**: Not explicitly used but structure allows for extension

## 📊 Demo Screenshots

> Sample screenshots can be added using terminal capture tools or rich output (optional).

---

Created with ❤️ using Python and Rich.
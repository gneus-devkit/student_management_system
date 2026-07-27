# Student Management System

A command-line based Student Management System written in Python that allows educators to manage classrooms, track student grades, and record attendance — all persisted to a local JSON file.

## Features

- **Classroom Management** — Create, list, and remove classrooms.
- **Student Management** — Add new students to a classroom and view existing students.
- **Grade Tracking** — Record grades for each student and automatically calculate overall averages.
- **Attendance Tracking** — Mark students as present or absent and compute overall attendance percentages.
- **Student Reports** — View a detailed report for any student including grades and attendance history.
- **Data Persistence** — All classroom and student data is saved to a local JSON file (`classes.json`) so it survives between sessions.

## Requirements

- **Python 3.8+** (uses only the standard library — no external dependencies)

## Installation

1. **Clone or download** this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **No additional setup is required.** The project uses only Python's built-in modules (`json`, `os`, `datetime`, `input`).

## Usage

Run the main script from the project directory:

```bash
python main.py
```

### Main Menu

Once launched, you'll be presented with the main menu:

```
Welcome to the Student Management System:

(1) Classrooms
(2) Classroom List
(3) Remove Class
(0) Exit
```

- **(1) Classrooms** — Enter a classroom name. If it doesn't exist, you'll be prompted to create it. Once inside, you can manage students.
- **(2) Classroom List** — View all existing classrooms.
- **(3) Remove Class** — Delete a classroom and all its student data.
- **(0) Exit** — Quit the application.

### Classroom Menu

After entering a classroom, you'll see:

```
what would you like to do:

(1) New student
(2) Existing student
(3) Classlist
(4) Clear Class
(0) Exit
```

- **(1) New student** — Add a new student by entering their name and age.
- **(2) Existing student** — Select an existing student to manage their grades, attendance, or view their report.
- **(3) Classlist** — Print a summary of all students in the classroom.
- **(4) Clear Class** — Remove all students from the classroom (with confirmation).
- **(0) Exit** — Return to the main menu.

### Student Menu

After selecting an existing student, you'll see:

```
What would you like to do:

(1) Attendance
(2) Add grade
(3) View student
(4) Delete student
(0) Exit to last menu
```

- **(1) Attendance** — Mark the student as present or absent for the current day.
- **(2) Add grade** — Enter a numeric grade for the student.
- **(3) View student** — Display the student's full report (name, age, grades, attendance, and overall averages).
- **(4) Delete student** — Remove the student from the classroom (with confirmation).
- **(0) Exit to last menu** — Return to the previous menu.

## Project Structure

```
student-management-system/
├── main.py            # Entry point — CLI menu system and data persistence
├── students.py        # Student class: grades, attendance, and calculations
├── classroom.py       # Classroom class: student collection and serialization
├── classes.py         # Classes container class
├── menu.py            # Input helper functions for student operations
├── student_report.py  # Student report display function
├── classes.json       # Data file (auto-created on first run)
├── README.md          # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore rules
```

## Data Persistence

All data is stored in `classes.json` in the project root. The file is automatically created on the first run if it doesn't exist. Each classroom is stored as a dictionary key, with its value containing a list of student records (name, age, grades, attendance, and computed averages).

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

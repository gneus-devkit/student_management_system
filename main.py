from menu import create_student, add_grade, attendance
from student_report import view_student
from classroom import Classroom
from sort import sort_students_by_name, sort_students_by_grade, sort_students_by_attendance
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "classes.json")
def load_classes():
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump({}, f)
    with open(DATA_PATH, "r") as f:
        classroom_dict = json.load(f)
    return classroom_dict

def save_classes(classroom_dict):
    with open(DATA_PATH, "w") as f:
        json.dump(classroom_dict, f)

def main_menu():
    classroom_dict = load_classes()
    
    response = input("\nWelcome to the Student Management System:\n\n(1) Classrooms\n(2) Classroom List\n(3) Remove Class\n(0) Exit\n\n").lower().strip() 
    if response in ["1", "classrooms", "classroom"]:
        classroom_name = input("\nEnter the classroom name:\n\n").lower().strip()
        
        if classroom_name not in classroom_dict:
            create = input(f"\nClassroom '{classroom_name}' does not exist. Create it? (Y/n):\n\n").lower().strip()
            if create not in ["y", "", " "]:
                print(f"Classroom '{classroom_name}' was not created.")
                return main_menu()
            elif create in ["y", "", " "]:
                classroom_dict[classroom_name] = Classroom().to_dict()
                save_classes(classroom_dict)
            else:
                return main_menu()
        classroom_obj = Classroom.from_dict(classroom_dict[classroom_name])
        secondary_router(classroom_name, classroom_obj)
    
    elif response in ["2", "classroom list", "list"]:
        print("\nClassroom List:\n")
        for classroom_name in classroom_dict.keys():
            print(f"- {classroom_name}")
            return main_menu()
        
    elif response in ["3", "remove class", "delete class"]:
        classroom_name = input("\nEnter the classroom name to remove:\n\n").lower().strip()
        if classroom_name in classroom_dict:
            del classroom_dict[classroom_name]
            save_classes(classroom_dict)
            print(f"Classroom '{classroom_name}' has been removed.")
        else:
            print(f"Classroom '{classroom_name}' not found.")
        return main_menu()
    
    elif response in ["0", "exit"]:
        exit()

def secondary_router(classroom_name, classroom):
    response = input("\nwhat would you like to do:\n\n(1) New student\n(2) Existing student\n(3) Classlist\n(4) Clear Class\n(0) Exit\n\n").lower().strip()
    if response in ["1", "new", "new student"]:
        student = create_student()
        classroom.add_student(student)
        save = input("\nSave student (Y/n):\n\n").lower().strip()
        if save in ["y", "", " "]:
            classroom_dict = load_classes()
            classroom_from_file = Classroom.from_dict(classroom_dict[classroom_name])
            classroom_from_file.add_student(student)
            classroom = classroom_from_file
            classroom_dict[classroom_name] = classroom.to_dict()
            save_classes(classroom_dict)
            print("Student saved successfully!")
        secondary_router(classroom_name, classroom)
    
    elif response in ["2", "existing", "exist"]:
        existing_student(classroom_name, classroom)
    elif response in ["3", "classlist", "class"]:
        decision = input("\nHow would you like to sort the classlist:\n\n(1) Name\n(2) Grade\n(3) Attendance\n(0) Exit\n\n").lower().strip()
        if decision in ["1", "name"]:
            sort_students_by_name(classroom)
        elif decision in ["2", "grade"]:
            sort_students_by_grade(classroom)
        elif decision in ["3", "attendance"]:
            sort_students_by_attendance(classroom)
        elif decision in ["0", "exit"]:
            main_menu()
        else:
            print("Invalid option. Returning to the previous menu.")
        return secondary_router(classroom_name, classroom)
        
    elif response in ["4", "clear class", "clear"]:
        confirm = input(f"\nAre you sure you want to clear all students from '{classroom_name}'? (Y/n):\n\n").lower().strip()
        if confirm in ["y", "", " "]:
            classroom.class_list = []
            classroom_dict = load_classes()
            classroom_dict[classroom_name] = classroom.to_dict()
            save_classes(classroom_dict)
            print(f"Classroom '{classroom_name}' has been cleared.")
        return secondary_router(classroom_name, classroom)

def existing_student(classroom_name, classroom):
    student_name = input("\nEnter the student's name:\n(0) Return to main menu\n\n").lower().strip()
    if student_name == "0":
        secondary_router(classroom_name, classroom)
    
    for student in classroom.class_list:
        if student.name.lower() == student_name:
            selected_student = student
            break
    else:
        print("Student not found.")
        return existing_student(classroom_name, classroom)
    
    student_menu(selected_student, classroom_name, classroom)
    
def student_menu(selected_student, classroom_name, classroom):
    response = input("\nWhat would you like to do:\n\n(1) Attendance\n(2) Add grade\n(3) View student\n(4) Delete student\n(0) Exit to last menu\n\n").lower().strip()
    
    if response in ["1", "add attendance", "attendance"]:
        attendance(selected_student)
        save = input("\nSave attendance (Y/n):\n\n").lower().strip()
        if save not in ["y", "", " "]:
            return student_menu(selected_student, classroom_name, classroom)
        else:
            classroom_dict = load_classes()
            classroom_dict[classroom_name] = classroom.to_dict()
            save_classes(classroom_dict)
            print("Attendance saved successfully!")
        return student_menu(selected_student, classroom_name, classroom)
    
    elif response in ["2", "add grade", "grade"]:
        add_grade(selected_student)
        save = input("\nSave grade (Y/n):\n\n").lower().strip()
        if save not in ["y", "", " "]:
            return student_menu(selected_student, classroom_name, classroom)
        else:
            classroom_dict = load_classes()
            classroom_dict[classroom_name] = classroom.to_dict()
            save_classes(classroom_dict)
            print("Grade saved successfully!")
        return student_menu(selected_student, classroom_name, classroom)
    
    elif response in ["3", "view student", "view", "student"]:
        view_student(selected_student)
        return student_menu(selected_student, classroom_name, classroom)
    
    elif response in ["4", "delete", "delete student"]:
        from menu import delete_student
        save = input("\nSave deletion (Y/n):\n\n").lower().strip()
        if save not in ["y", "", " "]:
            return student_menu(selected_student, classroom_name, classroom)
        else:
            delete_student(selected_student, classroom)
            classroom_dict = load_classes()
            classroom_dict[classroom_name] = classroom.to_dict()
            save_classes(classroom_dict)
            return secondary_router(classroom_name, classroom)
    
    elif response in ["0", "exit", "last menu", "back", "return", "main menu", "menu"]:
        existing_student(classroom_name, classroom)


main_menu()
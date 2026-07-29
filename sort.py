from operator import attrgetter

from classroom import Classroom

def sort_students_by_name(classroom):
    classroom_list = []
    for student in classroom.class_list:
        classroom_list.append(f"Name: {student.name}, Age: {student.age}, Overall Grade: {student.overall_grade}, Overall Attendance: {student.overall_attendance}")
    sorted_list = sorted(classroom_list, key=lambda x: x.split(",")[0].split(":")[1].strip())
    for student_info in sorted_list:
        print(student_info)

def sort_students_by_grade(classroom):
    classroom_list = []
    for student in classroom.class_list:
        classroom_list.append(f"Name: {student.name}, Age: {student.age}, Overall Grade: {student.overall_grade}, Overall Attendance: {student.overall_attendance}")
    sorted_list = sorted(classroom_list, key=lambda x: float(x.split(",")[2].split(":")[1].strip()), reverse=True)
    for student_info in sorted_list:
        print(student_info)

def sort_students_by_attendance(classroom):
    classroom_list = []
    for student in classroom.class_list:
        classroom_list.append(f"Name: {student.name}, Age: {student.age}, Overall Grade: {student.overall_grade}, Overall Attendance: {student.overall_attendance}")
    sorted_list = sorted(classroom_list, key=lambda x: float(x.split(",")[3].split(":")[1].strip()), reverse=True)
    for student_info in sorted_list:
        print(student_info)
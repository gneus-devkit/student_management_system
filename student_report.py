def view_student(student):
    print(f"{'Name:':<15}{student.name}")
    print(f"{'Age:':<15}{student.age}")
    print(f"{'Grade:':<15}{student.overall_grade}")
    print(f"{'All Grades:':<15}{student.grade_list}")
    print(f"{'Attendance:':<15}{student.overall_attendance}")
    print(f"{'Attendance list:':<15}{student.attendance_list}")
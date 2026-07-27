class Classroom:
    @classmethod
    def from_dict(cls, data):
        classroom = cls()
        for student_data in data.get("class_list", []):
            from students import Student
            student = Student(student_data["_name"], student_data["_age"])
            student.grade_list = student_data.get("grade_list", [])
            student.attendance_list = student_data.get("attendance_list", {})
            student.overall_grade = student_data.get("overall_grade", 0)
            student.overall_attendance = student_data.get("overall_attendance", 0)
            classroom.add_student(student)
        return classroom
    
    def __init__(self):
        self.class_list = []
        
    def add_student(self, student):
        self.class_list.append(student)

    def remove_student(self, student):
        if student in self.class_list:
            self.class_list.remove(student)
        else:
            print(f"Student {student.name} not found.")
    
    def to_dict(self):
        return {
            "class_list": [
                {
                    "_name": student._name,
                    "_age": student._age,
                    "grade_list": student.grade_list,
                    "attendance_list": student.attendance_list,
                    "overall_grade": student.overall_grade,
                    "overall_attendance": student.overall_attendance
                } for student in self.class_list
            ]
        }
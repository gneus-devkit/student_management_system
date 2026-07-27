from students import Student

def create_student():
    name = input("\nStudent name:\n\n").capitalize().strip()
    age = int(input("\nStudent age:\n\n").strip())
    student = Student(name, age)
    return student

def add_grade(student):
    grade = input("\nStudent's grade:\n\n").strip()
    student.add_grade(grade)
    
def attendance(student):
    attend = input("\nDid the student attend class today:\n\n").lower().strip()
    student.student_attended(attend)

            
def delete_student(student, classroom):
    classroom.remove_student(student)
    print(f"Student {student.name} has been deleted from the classroom.")
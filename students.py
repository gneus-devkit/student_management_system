from datetime import date

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.grade_list = []
        self.attendance_list = {} 
        self.overall_grade = 0
        self.overall_attendance = 0

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
        
    def add_grade(self, grade):
        self.grade_list.append(float(grade))
        self.calculate_grade()
        return self.overall_grade
        
    def student_attended(self, attend):
        today = date.today()
        today_formatted = today.strftime("%m %d, %Y")
        try:
            if attend.lower() in ["yes", "y", "true"]:
                self.attendance_list[today_formatted] = 1
            elif attend.lower() in ["no", "n", "false"]:
                self.attendance_list[today_formatted] = 0
            else:
                print("Invalid input. Please try again.")
            self.calculate_attendence()
            return self.overall_attendance
        except Exception as e:
            print(f"An error occurred: {e}")
            return self.overall_attendance
        
        
    def calculate_grade(self):
        self.overall_grade = sum(self.grade_list)/len(self.grade_list) if self.grade_list else 0
        
    def calculate_attendence(self):
        self.overall_attendance = (sum(self.attendance_list.values())/len(self.attendance_list))*100 if self.attendance_list else 0
        
        
if __name__ == "__main__":
    student = Student("Chris", 14)
    student.student_attended("yes")
    student.add_grade(95)
    student.student_attended("yes")
    student.add_grade(85)
    student.student_attended("yes")
    student.add_grade(72)
    student.add_grade(0)
    print(student.grade_list)
    print(student.attendance_list)
    print(student.overall_attendance)
    print(student.overall_grade)
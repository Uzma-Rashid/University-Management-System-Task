class Person:
    def __init__(self,name, age, gender ):
        self.name = name
        self.age= age
        self.gender= gender
       
    
    def set_details(self):
        self.name=input("Enter your name ")
        self.age = input("Enter your age ")
        self.gender = input("Enter your gender ")


    def get_details(self):
        print("Name " + self.name)
        print("Age " + self.age)
        print("Gender " + self.gender)
        

class Student(Person):
    def __init__(self,name,age,gender, student_id, course):
        super().__init__(name,age,gender)
        self.student_id=student_id
        self.course=course
        self.grades=[]
    
    def set_student_details(self, student_id, course):
        self.student_id=student_id
        self.course = course 

    def add_grade(self,grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def get_student_summary(self):
        print ("Student ID: "+ self.student_id)
        print("Course " + self.course)
        print("Average grade: " + str(self.calculate_average_grade()))

    def get_mentor(self, Professor):
        return Professor.name
        

class Professor(Person):
    def __init__(self,name,age,gender,staff_id,department,salary):
        super().__init__(name,age,gender)
        self.staff_id = staff_id
        self.department = department
        self.salary=salary 
        self.mentored_students = []

    def set_professor_details(self,staff_id, department, salary):
        self.staff_id=staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, Student, feedback):
        print(f"feedback for {Student.name}: {feedback}")

    def increase_salary(self, percentage):
        self.salary + self.salary * (percentage/100)

    def get_professor_summary(self):
        print(self.get_details())   
        print("Staff ID: " + str(self.staff_id))
        print("Department "+ str(self.department))
        print("Salary: " + str(self.salary))

    def mentor_student(self,Student):
        self.mentored_students.append(Student.name)
        print(f"Professor {self.name} is now mentoring Student {Student.name} on {Student.course}")

    def get_mentored_students(self):
        return self.mentored_students
    
class Administrator(Person):
    def __init__(self,name,age,gender,admin_id,office, years_of_service):
        super().__init__(name,age,gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    def set_admin_details(self,admin_id,office, years_of_service):
        self.admin_id = admin_id
        self.office=office
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service += 1
    
    def get_admin_summary(self):
        return f"{self.get_details()}, Admin ID: {self.admin_id}, Office: {self.office}, Years of service: {self.years_of_service}"

student1 = Student("Farwar", "19", "Female","GHY89", "Chemistry")
student2=Student("Sofia", "19","Female", "APN97", "Biology")
professor1 = Professor("Mr Smith", "50", "male", "PO892", "Maths", 60000)
professor2 = Professor("Mr Carter", "40", "male", "TRS892", "Economics", 65000)  
admin = Administrator("Mrs Akhtar", "30", "Female", "AIGD89", "Room U04", 3)
student1.add_grade(100)
student1.add_grade(70)
student2.add_grade(80)

professor1.give_feedback(student1, "Good job!")
professor1.increase_salary(20)

admin.increment_service_years()

print(student1.get_student_summary())
print(student2.get_student_summary())
print(professor1.get_professor_summary())
print(professor2.get_professor_summary())
print(admin.get_admin_summary())

professor1.mentor_student(student1)
print(student1.get_mentor(professor1))
print(professor1.get_mentored_students())

professor2.mentor_student(student2)
print(student2.get_mentor(professor2))
print(professor2.get_mentored_students())


    
    


    
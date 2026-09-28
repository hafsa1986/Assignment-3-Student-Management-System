#Student Management System using Python OOP concepts:
# Parent Class
class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email     # private attribute (Encapsulation)
        self.age = age
        self.department = department
    
    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Age:", self.age)
        print("Department:", self.department)
    
    def calculate_result(self, *marks):   # Method Overloading using *args
        if marks:
            avg = sum(marks) / len(marks)
            print("Average Marks:", avg)
        else:
            print("No marks provided.")
    
    def get_student_type(self):
        return "General Student"


# Child Class: UndergraduateStudent
class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)  # Parent constructor
        self.semester = semester
    
    # Method overriding
    def get_student_type(self):
        return "Undergraduate Student"
    
    def display_info(self):
        super().display_info()   # Parent method running
        print("Semester:", self.semester)


# Child Class: GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)  # Parent constructor
        self.research_topic = research_topic
    
    # Method overriding
    def get_student_type(self):
        return "Graduate Student"
    
    def display_info(self):
        super().display_info()   # Parent method running
        print("Research Topic:", self.research_topic)

# Making and using objects

# Undergraduate Student
student1 = UndergraduateStudent("Hafsa", "U501", "hafsa@mail.com", 22, "CSE", "5th")
student1.display_info()
print("Type:", student1.get_student_type())
student1.calculate_result(80, 85, 90)

# Graduate Student
student2 = GraduateStudent("Fatima", "G201", "fatima@gmail.com", 25, "EEE", "AI Research")
student2.display_info()
print("Type:", student2.get_student_type())
student2.calculate_result(88, 92, 95, 85)


class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grade:{self.grade}")
    def update_grade(self, grade):
        self.grade = grade

student = Student("John",20,"B")
print("Before grade update:")
student.display()
student.update_grade("A")
print("After grade update:")
student.display()

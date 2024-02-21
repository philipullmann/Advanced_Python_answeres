class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def fullname(self):
        fu_name = f"{self.name} {self.surname}"
        return fu_name
    
    

class Student(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject_name = subject
        
    def subject(self):
        return self.subject_name
    
    def printNameSubject(self):
        print(f"{self.name} {self.surname}, {self.subject_name}")
        return f"{self.name} {self.surname}, {self.subject_name}"  
        
class Teacher(Person):
    def __init__(self, name, surname, te_subject):
        super().__init__(name, surname)
        self.te_subject = te_subject

    def printNameSubject(self):
        print(f"{self.name} {self.surname}, {self.te_subject}")
        return f"{self.name} {self.surname}, {self.te_subject}"  
        



"""
per = Person("Hans", "Wu").fullname()
stu = Student("How", "Da", "Physics")


print("Name:", stu.fullname(), "\n"
      "Subject:", stu.subject())
"""
from abc import ABC, abstractmethod

# Class and Class Attributes
# Person
class Person(ABC):

    def __init__(self,name, age,email,phone):
        #Instances Attributes
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone



#Student and Teacher
class Student(Person):

    def __init__(self, Student_id, name, age, email, phone):
        super().__init__(name, age, email, phone)
        self.Student_id = Student_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone




# @classmethod
# def _validate_unique_studentid(cls, studentid):
#     if studentid in cls.existing_studentid:
#         raise ValueError(f"Student with ID {studentid} already exists")
#     cls._existing_studentid.add(studentid)
#     return studentid

class Teacher(Person):

    def __init__(self, Employeeid, Subject, Department, name, age, email, phone):

        super().__init__(name, age, email, phone)
        self.Employeeid = Employeeid
        self.Subject = Subject
        self.Department = Department




#compostion



class School:

 def __init__(self):

    self.teachers = {}     #Name and courses
    self.Students = {}      #Name and courses
    self.courses = {}       #name and Teacher's assignment


class Course:

    def __init__(self, Name,teacher,Students):

        self.Name = Name
        self.teacher = teacher
        self.Students = Students

     #getters

    def get_Name(self):
        return self.Name

    def get_teacher(self):
        return self.teacher

    def get_Students(self):
        return self.Students

    #setters

    def set_Name(self,Name):
        self.Name = Name

    def set_teacher(self,teacher):
        self.teacher = teacher

    def set_Students(self,Students):
        self.Students = Students




class Teacher:

    def __init__(self,Name,Courses):
        self.Name = Name
        self.Courses = Courses

   #getters
    def get_Name(self):
        return self.Name

    def get_Courses(self):
        return self.Courses

    #setters
    def set_Name(self,Name):
        self.Name = Name

    def set_Courses(self,Courses):
        self.Courses = Courses




class Student:

    def __init__(self,Name,Courses,ID):

        self.Name = Name
        self.Courses = Courses
        self.ID = ID


    #GETTERS
    def get_Name(self):
        return self.Name

    def get_Courses(self):
        return self.Courses

    def get_ID(self):
        return self.ID


    #Setters

    def set_Name(self,Name):
        self.Name = Name

    def set_Courses(self,Courses):
        self.Courses = Courses


    def set_ID(self,ID):
        self.ID = ID



    









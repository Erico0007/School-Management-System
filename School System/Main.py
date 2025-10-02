# Main class
from Enrollable import EnrollmentSystem, InMemoryEnrollmentSystem
from Person import Student
from Person import Student
from Person import Teacher
from School import School


class Main:

    print("Starting Program")
    global Student1, Student2, Student3, Student4, Student5, Student6, Student7, Student8, Student9, Student10, Teacher1, Teacher2, Teacher3, Teacher4, Teacher5, Teacher6, Teacher7, Teacher8, enrollment, School

    if __name__ == "__main__":

        # Create Students

        Student1 = Student("11", "Eric Ekra ", 24, "eric@school.ed","416-589-31111")
        Student2 = Student("22", "Sanaa Siaha ",18 ,"Sanaa@school.ed","485-111-2222")
        Student3 = Student("33"  ,"Ahmed Halal",29,"Ahmed#school.ed","123-456-789")
        Student4 = Student("44","Marianne Tchomepi",22,"marianne@school.ed","256-444-9991")
        Student5 = Student("55", "Cam Florence",26,"cam11@school.ed","111-222-5689")
        Student6 = Student("66","Frank Olivier",25,"fo101@school.ed","222-999-4567")
        Student7 = Student("77", "Maya Patel", 19, "m.patel@school.ed", "222-888-1234")
        Student8 = Student("88", "Carlos Garcia", 20, "c.garcia@school.ed", "222-777-9876")
        Student9 = Student("99", "Zoe Tremblay", 22, "z.tremblay@school.ed", "222-555-2468")
        Student10 = Student("100", "Kenji Tanaka", 21, "k.tanaka@school.ed", "222-333-1357")

# Create Teacher

        Teacher1 = Teacher("10","Math","Mahtematics","Alan Baeur",40,"alan@school.ed","458-999-663" )

        Teacher2 =Teacher("22", "Science", "Biology 101", "Dr. Maria Rodriguez", 35, "m.rodriguez@school.ed", "458-777-112")

        Teacher3=  Teacher("15", "History", "World Civilizations", "Robert Chen", 52, "r.chen@school.ed", "458-888-445")

        Teacher4 =Teacher("37", "English", "American Literature", "Sarah-Jane O'Malley", 28, "s.omalley@school.ed", "458-111-998")

        Teacher5 = Teacher("41", "Computer Science", "Intro to Python", "David Miller", 45, "d.miller@school.ed", "458-555-330")

        Teacher6 = Teacher("18", "Art", "Studio Art & Design", "Chloe Williams", 33, "c.williams@school.ed", "458-222-774")

        Teacher7 = Teacher("29", "Physical Education", "Health & Wellness", "James Wilson", 39, "j.wilson@school.ed", "458-666-001")

        Teacher8 = Teacher("54", "Music", "Orchestra and Theory", "Eleanor Vance", 60, "e.vance@school.ed", "458-444-556")


# Create Enrollment System

    enrollment = InMemoryEnrollmentSystem()

# Enroll Students

    enrollment.enroll_student("11", "Math")
    enrollment.enroll_student("22", "Science")
    enrollment.enroll_student("33", "History")
    enrollment.enroll_student("44", "English")
    enrollment.enroll_student("55", "Computer Science")
    enrollment.enroll_student("66", "Art")
    enrollment.enroll_student("77", "Physical Education")
    enrollment.enroll_student("88", "Music")
    enrollment.enroll_student("99", "Math")
    enrollment.enroll_student("100", "Science")
    enrollment.enroll_student("11", "Science")
    enrollment.enroll_student("22", "History")
    enrollment.enroll_student("33", "English")
    enrollment.enroll_student("44", "Computer Science")
    enrollment.enroll_student("55", "Art")
    enrollment.enroll_student("66", "Physical Education")
    enrollment.enroll_student("77", "Music")
    enrollment.enroll_student("88", "Math")

   #Drop Courses

    enrollment.drop_student("22", "Math")
    enrollment.drop_student("33", "Science")
    enrollment.drop_student("44", "History")
    enrollment.drop_student("55", "English")
    enrollment.drop_student("66", "Computer Science")
    enrollment.drop_student("77", "Art")
    enrollment.drop_student("88", "Physical Education")
    enrollment.drop_student("99", "Music")
    enrollment.drop_student("100", "Math")
    enrollment.drop_student("11", "Science")
    enrollment.drop_student("22", "History")

#Create a school and Add Student

    School = School()

    School.Students[11]= Student1
    School.Students[22]= Student2
    School.Students[33]= Student3
    School.Students[44]= Student4
    School.Students[55]= Student5
    School.Students[66]= Student6
    School.Students[77]= Student7
    School.Students[88]= Student8
    School.Students[99]= Student9
    School.Students[100]= Student10

#Add Teachers
    School.teachers[10] = Teacher1
    School.teachers[22] = Teacher2
    School.teachers[15] = Teacher3
    School.teachers[37] = Teacher4
    School.teachers[41] =  Teacher5
    School.teachers[18] = Teacher6
    School.teachers[29] = Teacher7
    School.teachers[54]  = Teacher8


#School Directory


    print(Student1.Student_id, Student1.name, Student1.age, Student1.email, Student1.phone)
    print(Student2.Student_id, Student2.name, Student2.age, Student2.email, Student2.phone)
    print(Student3.Student_id, Student3.name, Student3.age, Student3.email, Student3.phone)
    print(Student4.Student_id, Student4.name, Student4.age, Student4.email, Student4.phone)
    print(Student5.Student_id, Student5.name, Student5.age, Student5.email, Student5.phone)
    print(Student6.Student_id, Student6.name, Student6.age, Student6.email, Student6.phone)
    print(Student7.Student_id, Student7.name, Student7.age, Student7.email, Student7.phone)
    print(Student8.Student_id, Student8.name, Student8.age, Student8.email, Student8.phone)
    print(Student9.Student_id, Student9.name, Student9.age, Student9.email, Student9.phone)

#print The List of  Teacher

    print(Teacher1.Employeeid, Teacher1.Subject, Teacher1.Department, Teacher1.name, Teacher1.age, Teacher1.email, Teacher1.phone)
    print(Teacher2.Employeeid, Teacher2.Subject, Teacher2.Department, Teacher2.name,Teacher2.age,Teacher2.email,Teacher2.phone)
    print(Teacher3.Employeeid, Teacher3.Subject, Teacher3.Department, Teacher3.name,Teacher3.age,Teacher3.email,Teacher3.phone)
    print(Teacher4.Employeeid, Teacher4.Subject, Teacher4.Department, Teacher4.name,Teacher4.age,Teacher4.email,Teacher4.phone)
    print(Teacher5.Employeeid, Teacher5.Subject, Teacher5.Department, Teacher5.name,Teacher5.age,Teacher5.email,Teacher5.phone)
    print(Teacher6.Employeeid, Teacher6.Subject, Teacher6.Department, Teacher6.name,Teacher6.age,Teacher6.email,Teacher6.phone)
    print(Teacher7.Employeeid, Teacher7.Subject, Teacher7.Department, Teacher7.name,Teacher7.age,Teacher7.email,Teacher7.phone)
    print(Teacher8.Employeeid, Teacher8.Subject, Teacher8.Department, Teacher8.name,Teacher8.age,Teacher8.email,Teacher8.phone)

#Print the Students class


    print(f"Enrollments: {enrollment.get_student_courses("11")}")
    print(f"Enrollments: {enrollment.get_student_courses("22")}")
    print(f"Enrollments: {enrollment.get_student_courses("33")}")
    print(f"Enrollments: {enrollment.get_student_courses("44")}")
    print(f"Enrollments: {enrollment.get_student_courses("55")}")
    print(f"Enrollments: {enrollment.get_student_courses("66")}")
    print(f"Enrollments: {enrollment.get_student_courses("77")}")
    print(f"Enrollments: {enrollment.get_student_courses("88")}")

#Print List of the Student enrolled in the different Class

    print(f"Enrollments: {enrollment.get_student_courses("22")}")
    print(f"Enrollments: {enrollment.get_student_courses("33")}")
    print(f"Enrollments: {enrollment.get_student_courses("44")}")
    print(f"Enrollments: {enrollment.get_student_courses("55")}")
    print(f"Enrollments: {enrollment.get_student_courses("66")}")
    print(f"Enrollments: {enrollment.get_student_courses("77")}")
    print(f"Enrollments: {enrollment.get_student_courses("88")}")



#  List of Student who are enrolled in the class

    print(f"Enrollments: {enrollment.is_enrolled("11", "Math")}")
    print(f"Enrollments: {enrollment.is_enrolled("22", "Science")}")
    print(f"Enrollments: {enrollment.is_enrolled("33", "History")}")
    print(f"Enrollments: {enrollment.is_enrolled("44", "English")}")
    print(f"Enrollments: {enrollment.is_enrolled("55", "Computer Science")}")
    print(f"Enrollments: {enrollment.is_enrolled("66", "Art")}")
    print(f"Enrollments: {enrollment.is_enrolled("77", "Physical Education")}")
    print(f"Enrollments: {enrollment.is_enrolled("88", "Music")}")


    #  List of Students who Drop Courses

    print(f"Drop Courses: {enrollment.drop_student("22", "Math")}")
    print(f"Drop Courses: {enrollment.drop_student("33", "Science")}")
    print(f"Drop Courses: {enrollment.drop_student("44", "History")}")
    print(f"Drop Courses: {enrollment.drop_student("55", "English")}")
    print(f"Drop Courses: {enrollment.drop_student("66", "Computer Science")}")
    print(f"Drop Courses: {enrollment.drop_student("77", "Art")}")
    print(f"Drop Courses: {enrollment.drop_student("88", "Physical Education")}")


    # print and the class and teacher

    print(f" list of Students enrolled in the different Class:{enrollment.get_all_enrollments()} ")

    # Print The list of Teacher teaching the different classes

    print(f"List of teachers and the students in a class: {enrollment.get_course_students("Math"),Teacher1.name}")
    print(f"List of teachers and the students in a class: {enrollment.get_course_students("Science"),Teacher2.name}")
    print (f"List of teachers and the students in a class: {enrollment.get_course_students("History"),Teacher3.name}")
    print(f"List of teachers and the students in a class: {enrollment.get_course_students("English"),Teacher4.name}")
    print("Program Ended")










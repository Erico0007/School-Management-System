# InterFace


from abc import ABC, abstractmethod
from typing import List, Dict, Set

class EnrollmentSystem(ABC):
    """Interface for student course enrollment systems"""

    @abstractmethod
    def enroll_student(self, Student_id: str, course_code: str) -> bool:
        """Enroll a student in a course. Returns True if successful."""
        pass

    @abstractmethod
    def drop_student(self, Student_id: str, course_code: str) -> bool:
        """Drop a student from a course. Returns True if successful."""
        pass

    @abstractmethod
    def is_enrolled(self, Student_id: str, course_code: str) -> bool:
        """Check if a student is enrolled in a course."""
        pass

    @abstractmethod
    def get_student_courses(self, Student_id: str) -> List[str]:
        """Get all courses a student is enrolled in."""
        pass

    @abstractmethod
    def get_course_students(self, course_code: str) -> List[str]:
        """Get all students enrolled in a course."""
        pass

    @abstractmethod
    def get_all_enrollments(self) -> Dict[str, Set[str]]:
        """Get all enrollments: {course_code: set_of_student_ids}"""
        pass




    # Implement the class

class InMemoryEnrollmentSystem(EnrollmentSystem):
        def __init__(self):
            self.enrollments = {}


        def enroll_student(self, Student_id: str, course_code: str) -> bool:
            if course_code not in self.enrollments:
                self.enrollments[course_code]=set()
            self.enrollments[course_code].add(Student_id)
            return True

        def drop_student(self, Student_id: str, course_code: str) -> bool:
            if course_code in self.enrollments and Student_id in self.enrollments[course_code]:
                self.enrollments[course_code].remove(Student_id)
                return True
            else:
                return False

        def is_enrolled(self, Student_id: str, course_code: str) -> bool:
            if course_code in self.enrollments and Student_id in self.enrollments[course_code]:
                return True
            else:
                return False



        def get_student_courses(self, Student_id: str) -> List[str]:
            courses = []
            for course_code, students in self.enrollments.items():
                if Student_id in students:
                    courses.append(course_code)
            return courses


        def get_course_students(self, course_code: str) -> List[str]:
            if course_code in self.enrollments:
                return list(self.enrollments[course_code])
            return []


        def get_all_enrollments(self) -> Dict[str, Set[str]]:
            return self.enrollments.copy()



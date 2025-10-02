# School Management System

## Overview
A Python-based school management system that handles...

## Architecture
- **Composition Pattern**: School contains Students, Teachers, and Courses
- **Inheritance Hierarchy**: Person → Student/Teacher
- **Interface Design**: EnrollmentSystem for course management

## Key Features
- Student and teacher management
- Course enrollment system
- [Add your main features...]

## Class Structure
- `School`: Main container class
- `Person`: Base class with common attributes
- `Student`: Manages student information
- `Teacher`: Manages teacher information  
- `Course`: Represents academic courses
- `EnrollmentSystem`: Interface for enrollment operations

## Usage
```python
# Example code snippet
school = School()
student = Student("ID", "Name", age, "email", "phone")
enrollment.enroll_student("11", "Math")

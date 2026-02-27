# Week 9 - School Management System


# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# Child class Student
class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Override parent method
    def introduce(self):
        return (
            f"Hi, I'm {self.name}, a student. "
            f"My ID is {self.student_id} "
            f"and I'm {self.age} years old."
        )


# Child class Teacher
class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return (
            f"Hello, I'm {self.name}, a teacher. "
            f"I teach {self.subject} "
            f"and I'm {self.age} years old."
        )


# Testing
student = Student("Alice", 16, "S001")
teacher = Teacher("Mr. Smith", 35, "Mathematics")

print(student.introduce())
print(teacher.introduce())

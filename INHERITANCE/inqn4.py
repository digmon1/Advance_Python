# Parent Class
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    # String Method
    def __str__(self):
        return (f"Name : {self.__name}\n"
                f"Age  : {self.__age}")


# Child Class 1
class Student(Person):
    def __init__(self, name, age, roll_number, gpa):
        super().__init__(name, age)
        self.__roll_number = roll_number
        self.__gpa = gpa

    # Getters
    def get_roll_number(self):
        return self.__roll_number

    def get_gpa(self):
        return self.__gpa

    # Setters
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def set_gpa(self, gpa):
        self.__gpa = gpa

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nRoll Number : {self.__roll_number}"
                f"\nGPA         : {self.__gpa}")


# Child Class 2
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.__subject = subject
        self.__salary = salary

    # Getters
    def get_subject(self):
        return self.__subject

    def get_salary(self):
        return self.__salary

    # Setters
    def set_subject(self, subject):
        self.__subject = subject

    def set_salary(self, salary):
        self.__salary = salary

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nSubject     : {self.__subject}"
                f"\nSalary      : Rs.{self.__salary}")


# Driver Program

student = Student("Sanjay", 20, "CS101", 3.85)
teacher = Teacher("Ram Sharma", 40, "Python Programming", 65000)

print("Student Details")
print(student)

print("\nTeacher Details")
print(teacher)

# Updating Values
student.set_gpa(3.95)
teacher.set_salary(70000)

print("\nAfter Updating Details")

print("\nStudent")
print(student)

print("\nTeacher")
print(teacher)
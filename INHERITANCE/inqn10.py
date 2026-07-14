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
        return (f"Name         : {self.__name}\n"
                f"Age          : {self.__age}")


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
                f"\nRoll Number  : {self.__roll_number}"
                f"\nGPA          : {self.__gpa}")


# Child Class 2
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    # Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        self.__salary = salary

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nEmployee ID  : {self.__employee_id}"
                f"\nSalary       : Rs.{self.__salary}")


# Grandchild Class
class Teacher(Employee):
    def __init__(self, name, age, employee_id, salary, subject, experience):
        super().__init__(name, age, employee_id, salary)
        self.__subject = subject
        self.__experience = experience

    # Getters
    def get_subject(self):
        return self.__subject

    def get_experience(self):
        return self.__experience

    # Setters
    def set_subject(self, subject):
        self.__subject = subject

    def set_experience(self, experience):
        self.__experience = experience

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nSubject      : {self.__subject}"
                f"\nExperience   : {self.__experience} Years")


# Driver Program

student1 = Student("Sanjay", 20, "CS101", 3.90)

student2 = Student("Ram", 21, "CS102", 3.75)

teacher1 = Teacher(
    "Hari Sharma",
    40,
    "EMP101",
    70000,
    "Python",
    12
)

teacher2 = Teacher(
    "Sita Karki",
    35,
    "EMP102",
    65000,
    "Database",
    8
)

print("========== Student 1 ==========")
print(student1)

print("\n========== Student 2 ==========")
print(student2)

print("\n========== Teacher 1 ==========")
print(teacher1)

print("\n========== Teacher 2 ==========")
print(teacher2)

# Updating Values
student1.set_gpa(4.00)
teacher1.set_salary(75000)
teacher1.set_experience(13)

print("\n========== Updated Details ==========")

print("\nStudent 1")
print(student1)

print("\nTeacher 1")
print(teacher1)
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


# Child Class
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

    # String Method
    def __str__(self):
        return (super().__str__() +
                f"\nEmployee ID : {self.__employee_id}"
                f"\nSalary      : Rs.{self.__salary}")


# Grandchild Class
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.__department = department

    # Getter
    def get_department(self):
        return self.__department

    # Setter
    def set_department(self, department):
        self.__department = department

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nDepartment  : {self.__department}")


# Driver Program
manager = Manager("Sanjay", 21, "EMP101", 70000, "Information Technology")

print("Manager Details")
print(manager)

print("\nAfter Updating Salary and Department")
manager.set_salary(80000)
manager.set_department("Software Development")

print(manager)
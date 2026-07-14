# Parent Class
class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    # Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    # Method to Override
    def work(self):
        return "Employee is working."

    # String Method
    def __str__(self):
        return (f"Employee ID : {self.__employee_id}\n"
                f"Name        : {self.__name}\n"
                f"Salary      : Rs.{self.__salary}")


# Child Class
class Developer(Employee):
    def __init__(self, employee_id, name, salary, programming_language):
        super().__init__(employee_id, name, salary)
        self.__programming_language = programming_language

    # Getter
    def get_programming_language(self):
        return self.__programming_language

    # Setter
    def set_programming_language(self, programming_language):
        self.__programming_language = programming_language

    # Overriding work()
    def work(self):
        return f"Developer writes code using {self.__programming_language}."

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nProgramming Language : {self.__programming_language}")


# Child Class
class Designer(Employee):
    def __init__(self, employee_id, name, salary, design_software):
        super().__init__(employee_id, name, salary)
        self.__design_software = design_software

    # Getter
    def get_design_software(self):
        return self.__design_software

    # Setter
    def set_design_software(self, design_software):
        self.__design_software = design_software

    # Overriding work()
    def work(self):
        return f"Designer creates designs using {self.__design_software}."

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nDesign Software      : {self.__design_software}")


# Driver Program
developer = Developer("EMP101", "Sanjay", 70000, "Python")
designer = Designer("EMP102", "Ram", 65000, "Adobe Photoshop")

print("Developer Details")
print(developer)
print("Work:", developer.work())

print("\nDesigner Details")
print(designer)
print("Work:", designer.work())

print("\nAfter Updating Details")

developer.set_salary(75000)
developer.set_programming_language("Java")

designer.set_salary(68000)
designer.set_design_software("Adobe Illustrator")

print("\nDeveloper")
print(developer)
print("Work:", developer.work())

print("\nDesigner")
print(designer)
print("Work:", designer.work())
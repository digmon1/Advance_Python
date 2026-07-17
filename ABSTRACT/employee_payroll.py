from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def __init__(self, name, basic_salary, bonus):
        super().__init__(name)
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

    def display_details(self):
        print("Employee Type : Manager")
        print("Name          :", self.name)
        print("Basic Salary  :", self.basic_salary)
        print("Bonus         :", self.bonus)
        print("Total Salary  :", self.calculate_salary())


class Developer(Employee):

    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_details(self):
        print("Employee Type :", "Developer")
        print("Name          :", self.name)
        print("Hourly Rate   :", self.hourly_rate)
        print("Hours Worked  :", self.hours_worked)
        print("Total Salary  :", self.calculate_salary())


class Intern(Employee):

    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

    def display_details(self):
        print("Employee Type :", "Intern")
        print("Name          :", self.name)
        print("Monthly Stipend :", self.stipend)
        print("Total Salary    :", self.calculate_salary())


manager = Manager("Rijan", 60000, 10000)
developer = Developer("Ajay", 500, 120)
intern = Intern("Sanjay", 15000)

manager.display_details()
print()

developer.display_details()
print()

intern.display_details()
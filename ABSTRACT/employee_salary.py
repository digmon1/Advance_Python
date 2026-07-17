from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: ABC Pvt Ltd")


class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"{self.name}'s Salary = Rs.{self.monthly_salary}")


class PartTimeEmployee(Employee):

    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        salary = self.hours * self.rate
        print(f"{self.name}'s Salary = Rs.{salary}")


emp1 = FullTimeEmployee("Rijan", 50000)
emp2 = PartTimeEmployee("Sanjay", 40, 500)

print("Full-Time Employee")
emp1.display_company()
emp1.calculate_salary()

print("\nPart-Time Employee")
emp2.display_company()
emp2.calculate_salary()
class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


class Freelancer(Employee):
    def __init__(self, projects, payment):
        self.projects = projects
        self.payment = payment

    def calculate_salary(self):
        return self.projects * self.payment


employees = [
    FullTimeEmployee(50000),
    PartTimeEmployee(80, 400),
    Freelancer(5, 12000)
]

for emp in employees:
    print("Salary =", emp.calculate_salary())
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

emp = Employee(emp_id, name, salary)
emp.display()
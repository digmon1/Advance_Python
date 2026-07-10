class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        per = self.percentage()

        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B+"
        elif per >= 60:
            return "B"
        elif per >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

marks = []
for i in range(5):
    m = float(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(m)

student = Student(name, roll, marks)
student.display()
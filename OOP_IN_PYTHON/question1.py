class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

student = Student()
student.name = input("Enter student name: ")
student.age = int(input("Enter age: "))

print("\nStudent Information")
print("Name:", student.name)
print("Age:", student.age)
class Human:
    def walk(self):
        print("Walking...")
    def sleep(self):
        print("Sleeping...")

class Student(Human):
    def read(self):
        print("Reading...")

s = Student()
s.read()
s.walk()
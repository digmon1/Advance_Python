class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def introduce(self):
        print("I am a student.")


class Teacher(Person):
    def introduce(self):
        print("I am a teacher.")


class TeachingAssistant(Student, Teacher):
    def introduce(self):
        super().introduce()
        print("I am also a Teaching Assistant.")


ta = TeachingAssistant()

ta.introduce()

print("\nMethod Resolution Order (MRO):")
for cls in TeachingAssistant.__mro__:
    print(cls.__name__)
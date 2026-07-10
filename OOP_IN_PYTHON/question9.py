class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def display(self):
        print("\nTeacher:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience)

    def senior(self):
        if self.experience >= 10:
            print("Senior Teacher")
        else:
            print("Junior Teacher")

    def promotion(self):
        self.experience += 1


teachers = [
    Teacher("Ram", "Math", 8),
    Teacher("Hari", "Science", 12),
    Teacher("Sita", "English", 15)
]

for t in teachers:
    t.display()
    t.senior()
    t.promotion()

print("\nAfter Promotion")

for t in teachers:
    t.display()
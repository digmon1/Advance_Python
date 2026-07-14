class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks =marks
    
    def __add__(self, other):
        return self.marks+ other.marks
    
    def __gt__(self, other):
        if self.marks> other.marks:
            return True
        else:
            False
s1=Student('sanjay',55)
s2=Student('Rjan',45)

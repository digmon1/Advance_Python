from abc import *
class Person:
    def speak(self):
        print('speak')

    @abstractmethod
    def sucess(self):
        pass

class student(Person):
        def sucess(self ):
            print("Sucess ny doing smart work....")
        
        def move(self):
            print('Moving')

s1= student()
s1.speak()
s1.suceess()

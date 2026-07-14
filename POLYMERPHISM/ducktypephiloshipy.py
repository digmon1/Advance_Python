#Class level polymerphism
class Dog:
    def speak (self):
        print('Bho....Bho...Bho')

class Cat:
    def speak (self):
        print('Meow...Meow...Meow')

class Duck:
    def speak (self):
        print('Quack...Quack....Quack')

class Goat:
    def speak (self):
        print('Mya....Myaa....Myaa')

def f1(obj):
    obj.speak()

object=[Dog(), Cat(), Duck(),Goat()]
for x in object:
    f1(x)
while x in object:
    f1(x)
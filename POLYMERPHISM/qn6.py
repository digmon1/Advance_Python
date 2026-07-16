class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


class Car:
    def drive(self):
        print("Car is moving")


def make_sound(obj):
    try:
        obj.speak()
    except AttributeError:
        print("This object cannot speak.")


make_sound(Dog())
make_sound(Cat())
make_sound(Car())
class Duck:
    def talk(self):
        print("Duck says: Quack!")


class Human:
    def talk(self):
        print("Human says: Hello!")


class Robot:
    def talk(self):
        print("Robot says: Beep Boop!")


def communicate(obj):
    obj.talk()


communicate(Duck())
communicate(Human())
communicate(Robot())
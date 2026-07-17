from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def __init__(self, name):
        self.name = name
        self.status = False   # False = OFF, True = ON

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def device_status(self):
        pass


class Light(SmartDevice):

    def turn_on(self):
        if self.status:
            print(f"{self.name} is already ON.")
        else:
            self.status = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        if not self.status:
            print(f"{self.name} is already OFF.")
        else:
            self.status = False
            print(f"{self.name} is now OFF.")

    def device_status(self):
        print(f"{self.name} Status :", "ON" if self.status else "OFF")


class Fan(SmartDevice):

    def turn_on(self):
        if self.status:
            print(f"{self.name} is already ON.")
        else:
            self.status = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        if not self.status:
            print(f"{self.name} is already OFF.")
        else:
            self.status = False
            print(f"{self.name} is now OFF.")

    def device_status(self):
        print(f"{self.name} Status :", "ON" if self.status else "OFF")


class AirConditioner(SmartDevice):

    def turn_on(self):
        if self.status:
            print(f"{self.name} is already ON.")
        else:
            self.status = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        if not self.status:
            print(f"{self.name} is already OFF.")
        else:
            self.status = False
            print(f"{self.name} is now OFF.")

    def device_status(self):
        print(f"{self.name} Status :", "ON" if self.status else "OFF")


class Television(SmartDevice):

    def turn_on(self):
        if self.status:
            print(f"{self.name} is already ON.")
        else:
            self.status = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        if not self.status:
            print(f"{self.name} is already OFF.")
        else:
            self.status = False
            print(f"{self.name} is now OFF.")

    def device_status(self):
        print(f"{self.name} Status :", "ON" if self.status else "OFF")


devices = [
    Light("Living Room Light"),
    Fan("Ceiling Fan"),
    AirConditioner("Bedroom AC"),
    Television("Smart TV")
]

for device in devices:
    device.turn_on()
    device.device_status()
    device.turn_on()
    device.turn_off()
    device.device_status()
    device.turn_off()
    print("-" * 35)
# Parent Class 1
class Camera:
    def __init__(self, camera_mp):
        self.__camera_mp = camera_mp

    # Getter
    def get_camera_mp(self):
        return self.__camera_mp

    # Setter
    def set_camera_mp(self, camera_mp):
        self.__camera_mp = camera_mp

    # Method
    def takePhoto(self):
        print(f"Photo taken with {self.__camera_mp} MP camera.")

    # String Method
    def __str__(self):
        return f"Camera MP   : {self.__camera_mp}"


# Parent Class 2
class Phone:
    def __init__(self, phone_number):
        self.__phone_number = phone_number

    # Getter
    def get_phone_number(self):
        return self.__phone_number

    # Setter
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Method
    def call(self):
        print(f"Calling {self.__phone_number}...")

    # String Method
    def __str__(self):
        return f"Phone Number: {self.__phone_number}"


# Child Class
class Smartphone(Camera, Phone):
    def __init__(self, camera_mp, phone_number, brand, storage):
        Camera.__init__(self, camera_mp)
        Phone.__init__(self, phone_number)
        self.__brand = brand
        self.__storage = storage

    # Getters
    def get_brand(self):
        return self.__brand

    def get_storage(self):
        return self.__storage

    # Setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_storage(self, storage):
        self.__storage = storage

    # Overriding __str__()
    def __str__(self):
        return (Camera.__str__(self) + "\n" +
                Phone.__str__(self) + "\n" +
                f"Brand       : {self.__brand}\n"
                f"Storage     : {self.__storage} GB")


# Driver Program
phone = Smartphone(
    64,
    "9812345678",
    "Samsung",
    256
)

print("Smartphone Details")
print(phone)

print("\nTesting Inherited Methods")
phone.takePhoto()
phone.call()

print("\nAfter Updating Details")

phone.set_camera_mp(108)
phone.set_phone_number("9800000000")
phone.set_brand("Apple")
phone.set_storage(512)

print(phone)

print("\nTesting Updated Methods")
phone.takePhoto()
phone.call()
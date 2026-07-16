from abc import * 
class Person(ABC):
    @abstractmethod
    def speak(self):
        print('Sanjay Kumar Shrestha')
p1 =Person()
from abc import ABC, abstractmethod

# 1. Abstract Class (Ye sirf ek Template/Rule Book hai)
class Car(ABC):
    @abstractmethod
    def start(self):
        pass  # Yahan koi code nahi, bas pass likh diya

# 2. Concrete Classes (Jo asal mein kaam karengi)
class Toyota(Car):
    def start(self):
        print("Toyota starts with a Key. 🔑")

class Tesla(Car):
    def start(self):
        print("Tesla starts with a Mobile App or Button. 📱")

class Suzuki(Car):
    def start(self):
        print("Suzuki starts manually. 🗝️")

# Testing
my_car1 = Toyota()
my_car1.start()

my_car2 = Tesla()
my_car2.start()

my_car3 = Suzuki()
my_car3.start()
from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def drink(self):
        pass

    def description(self):
        print("I am a drink")

class Beer(Drink):
    def __init__(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

beer = Beer(10)
print(beer.get_quantity())
beer.description()
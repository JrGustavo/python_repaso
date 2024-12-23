class People:
    classname =  "People"
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def hi(self):
        print("Hola" + self.name)

    def get_age(self):
        return self.__age

    def __some(self):
        print(self)

    @staticmethod
    def hello():
        print("Hello")

    @classmethod
    def new(cls, name: str):
        return cls(name)


class Barman(People):
    pass

    def welcome(self):
        print("bienvenido")

class Student(People):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def hi(self):
        print("Hola" + self.name + " " + self.grade)

def show(people: People):
    people.hi()

gustavo = People( "Gustavo", 20)
gustavo.hi()

show(Barman("Carlos"))
show(gustavo)

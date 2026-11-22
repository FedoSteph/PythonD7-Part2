class Person:
    def call_person(self, name):
        print(f"Helow, I am {name}")

    def expenses(self,type,amount):
        print(f"type: {type} = {amount}")

person = Person()#here there s no self constructor we cn just call. no __init__ here. so we dont want to make onject for person by person like DogC.py
person.call_person("kamal")
person.call_person("Namal")
person.expenses("food",5000)

class Car:

    brand = "Mercedes"

    def __init__(self, type,color):
        self.type = type
        self.color = color

    def start(self):
        print(f"{self.brand} is started!")


car1 = Car("tesla","blue")
print(car1.brand)
car1.start()

car2 = Car("tesla2","black")
print(car2.type)

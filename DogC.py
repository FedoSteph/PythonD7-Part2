class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"Hello {self.name}!")

    def eat(self, food):
        print(f"{self.name} eats {food}")


dog1 = Dog("SHADOW", 4, "German shepard")  # creating object for Dog class
print(dog1.name)
print(dog1.age)
print(dog1.breed)
dog1.bark()
dog1.eat("meat")

dog2 = Dog("Browni", 3, "jungle dog")  # another dog
print(dog2.name)
print(dog2.age)


class GermanShepard(Dog):
    # def home(self, person):
    #     print(f"my owner s name is {person}!")

    def bark(self):
        print(f"Hello German shepard!")

class Shitzu(Dog):
    def bark(self):
        print(f"Hello Shitzu!")

child1 = GermanShepard("Browni", 3, "Jungle dog")
child1.bark()

child2 = Shitzu("Shitzu", 4, "Jungle dog")
child2.bark()


# child1 = GermanShepard("Max", 2, "Shitzu")
# child1.home("Nimal")
# child1.eat("meat")
# child1.bark()
#
# dog1 = Dog("Browni", 3, "Jungle dog")
# print(dog1.name)
# print(dog1.age)
# print(dog1.breed)
# dog1.bark()
# dog1.eat("meat")


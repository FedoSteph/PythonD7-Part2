class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"Hello {self.name}!")

    def eat(self, food):
        print(f"{self.name} eats {food} food!")

dog1 = Dog("SHADOW", 4, "German shepard")#creating object for Dog class
print(dog1.name)
print(dog1.age)
print(dog1.breed)
dog1.bark()
dog1.eat("meat")

dog2=Dog("Browni",3,"jungle dog")#another dog
print(dog2.name)
print(dog2.age)
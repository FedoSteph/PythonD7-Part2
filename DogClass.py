class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"Hello {self.name}!")

dog1 = Dog("SHADOW", 4, "German shepard")#creating object for Dog class
print(dog1.name)
print(dog1.age)
print(dog1.breed)
dog1.bark()
class Tiger:
    def sound(self):
        print("GR.. GR..")

class Cat:
    def sound(self):
        print("MEOW..")

class Bird:
    def sound(self):
        print("CHICK..CHICK...")

animals = [Tiger(),Cat(),Bird()]
for animal in animals:
    animal.sound()


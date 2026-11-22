class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private perperty

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

stu1 = Student("Bob", 20)
print(stu1.name)
print(stu1.get_age())

print(stu1.set_age(30))

#not recommand
print(stu1._Student__age)

#proteted
class Teacher:
    def __init__(self, name: str, salary=None):
        self.name = name #obj.age
        self._salary = salary #this is protected property

teach1 = Teacher("Rathna teacher", 20)
print(teach1.name)
print(teach1._salary)
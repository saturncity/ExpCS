class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = "Black"

    def bark(self):
        print("Woof woof")

    def getName(self):
        print(f"This dog name is {self.name}")

dog1 = Dog("Joey", 14)
print(dog1.name, dog1.age, dog1.color)
dog1.bark()

dog2 = Dog("Jimmy", 3)
dog2.getName()
dog2.bark()
# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.color = "Black"
#
#     def bark(self):
#         print("Woof woof")
#
#     def getName(self):
#         print(f"This dog name is {self.name}")
#
# dog1 = Dog("Joey", 14)
# print(dog1.name, dog1.age, dog1.color)
# dog1.bark()
#
# dog2 = Dog("Jimmy", 3)
# dog2.getName()
# dog2.bark()
#

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f"The restaurant is open!")

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} style food")

restaurant1 = Restaurant("Jolibee", "the best")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.open_restaurant()
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Jimbob", "asian")
restaurant3 = Restaurant("Wendys", "euro peen")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self.first_name, self.last_name, self.age)

    def greet_user(self):
        print(f"Hello, {self.first_name}! welcome to the place")

user1 = User("Jason", "Lenz", 15)
user2 = User("Jim", "Bob", 42)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
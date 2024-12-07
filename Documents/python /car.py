# object = A "bundle" of related attributes (variables) and methods (function)
#           Ex: phone, cup, book
#           You need a "class" to create many objects
# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
#     def __str__(self):
#         return f"{self.model}, {self.year}, {self.color}, {self.for_sale}"
    
#     def drive(self):
#         print(f"You drive the {self.model}.")
        
#     def stop(self):
#         print(f"You stop the {self.model}.") 
        
#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")


# class vaiables = Shared among all instance of a class 
#                   Defined outside the character
#                   Allow you to share data among all objects created from that class

# class Student:
    
#     class_year = 2024
#     num_students = 0
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students +=1
        
# student1 = Student("Dada", 18)
# student2 = Student("Bobo", 30)
# student3 = Student("Haha", 55)

# print(student1.name)
# print(student1.age)
# print(Student.class_year) #can use student1.class_year or student2.class_year is the same
# print(Student.num_students) # count student in the class


# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility
#               class Child(Parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
        
#     def eat(self):
#         print(f"{self.name} is eating")
        
#     def sleep(self):
#         print(f"{self.name} is sleeping")
        
# # class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mikey")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()

# class Dog(Animal):
#     def speak(self):
#         print("Woof")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")
        
# class Mouse(Animal):
#     def speak(self):
#         print("Squeek")
        
# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mikey")

# dog.speak()


# multiple inheritance = inherit from more than one parent class
#                        C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent 
#                           C(B) <- B(A) <- A


# class Animal:
    
#     def __init__(self, name):
#         self.name = name
        
#     def eat(self):
#         print(f"This {self.name} is eating")

#     def sleep(self):
#         print(f"This {self.name} is sleeping")
        
# class Prey(Animal):
#     def flee(self):
#         print(f"This {self.name} is fleeing")
    
# class Predator(Animal):
#     def hunt(self):
#         print(f"This {self.name} is hunting")
    
# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nimo")

# hawk.hunt()



# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                   They can contain abstract methods, which are declared but have no implementation.
#                   Abstract classes benefits:
#                   1. Prevents instantiation of the class itself
#                   2. Require children to use inherited abstract methods

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
    
#     @abstractmethod
#     def go(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
    
# vehicle = Vehicle()



# super() = Function used in  a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)



# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def speak(self):
#         return "Woof"

# class Cat(Animal):
#     def speak(self):
#         return "Meow"

# # Example
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.name, "says:", dog.speak())
# print(cat.name, "says:", cat.speak())





# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds.")

#     def get_balance(self):
#         return self.__balance

# # Example
# account = BankAccount()
# account.deposit(100)
# account.withdraw(50)
# print("Current Balance:", account.get_balance())
# account.withdraw(100)  # Insufficient funds




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)



# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(mysillyobject):
#     print("Hello my name is " + mysillyobject.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)



class Car:
    max_speed = 200  # Class variable, shared across all instances

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating instances
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing the class variable max_speed
print(car1.make)  # Output: 200
print(car2.max_speed)  # Output: 200

# Changing the max_speed for the class affects all instances
# Car.max_speed = 220
print(car1.max_speed)  # Output: 220
print(car2.max_speed)  # Output: 220

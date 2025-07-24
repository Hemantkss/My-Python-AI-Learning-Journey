"""
    OOPS in python
"""

# Classes in OOPS
# class Factory:
#     a = 12 # Attribute
    
#     def hello(self): # Method
#         print("Hello from Factory")
    
#     print("This is a class")
    
# print(Factory().a) 
# print(Factory().hello())


# Objects in OOPS

# class Factory:
#     a = 12 # Attribute
    
#     def hello(self): # Method
#         print("Hello from Factory")
    
#     print("This is a class")
    
# obj = Factory() # Object
# print(obj.a) # Accessing attribute
# obj.hello() # Accessing method

# Constructor
# class Factory: 
#     def __init__(self, material, zips, pockets): # Constructor
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
#     def show(self):
#         print(f"object details: {self.material}, {self.zips}, {self.pockets}")
        

# reebok = Factory("Cotton", 2, 4)
# campus = Factory("Polyester", 3, 5)

# reebok.show()
# campus.show()


# Attributes and Methods

# class Animal:
#     name = "Dog" # Class attribute
    
#     def __init__(self, age):
#         self.age = age # Instance attribute
        
#     def show(self): # Instance method
#         print(f"Animal name: {self.name}, Age: {self.age}")
        
# dog = Animal(2)
# dog.show()


# class Animal:
#     name = "Dog" # Class attribute
    
#     def __init__(self, age):
#         self.age = age # Instance attribute
        
#     def show(self): # Instance method
#         print(f"Animal name: {self.name}, Age: {self.age}")
        
#     @classmethod
#     def hello(cls):
#         print("Hello from class method")
        
#     @staticmethod
#     def hello2():
#         print("Hello from static method")
        
        
# obj = Animal(12) # Object
# obj.show()
# obj.hello() # Class method
# obj.hello2() # Static method


# Inheritance in OOPS
# class Factory:
#     a = "i am a attribute from Factory class"# Attribute
#     def hello(self): # Method
#         print("i am a method from Factory class")
        
# class Factory2(Factory): # Inheriting Factory class
#     pass # Inheriting all the attributes and methods of Factory class

# obj = Factory2() # Object

# print(obj) 
# print(obj.a) # Accessing attribute
# print(obj.hello()) # Accessing method


# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def show(self):
#         print(f"Animal name or Human name: {self.name}")
        
# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         super().show()
#         print(f"Human age: {self.age}")

# animal = Animal("Dog")
# animal.show()

# person = Human("Hemant", 30)
# person.show()


# class Animal:
#     name1 = "Dog" # Class attribute
    
# class Human:
#     name2 = "Hemant" # Class attribute
    
# class Robot(Animal, Human): # Multiple inheritance
#     name3 = "Robot" # Class attribute
    
    
# obj = Robot() # Object
# print(obj.name1) # Accessing attribute from Animal class
# print(obj.name2) # Accessing attribute from Human class
# print(obj.name3) # Accessing attribute from Robot class


# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips
        
# class NashikFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color
        
# class PuneFactory(NashikFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets
        
# obj = PuneFactory("Polimer", 3, "red", 5)
# print(obj)
# print(obj.material) # Accessing attribute from Factory class
# print(obj.zips) # Accessing attribute from Factory class
# print(obj.color) # Accessing attribute from NashikFactory class
# print(obj.pockets) # Accessing attribute from PuneFactory class




# Polymorphism OOPS
# def show():
#     print("how are you")
    
# def show():
#     print("how are you doing")
    
# show() # Last defined function will be executed


# class Animal:
#     def show(self):
#         print("How are you")
        
# class Human(Animal):
#     def show(self):
#         print("what are you doing")
        
# obj = Human()
# obj.show() # Method overriding


# Duck typing
# class Animal:
#     def show(self):
#         print("Animal is showing")
        
# class Human:
#     def show(self):
#         print("Human is showing")
 
# obj1 = Animal()
# obj1.show()   
 
# obj2 = Human()
# obj2.show()

# encapsulation OOPS
# class Factory:
#     _a = "PuneFactory" # Class attribute
    
#     def show(self):
#         print(" I am In PuneFactory")
        
# class Factory2(Factory):
#     def show(self):
#         print(super()._a)
        
# obj = Factory2() # Object
# obj.show() # Accessing method

# class Factory:
#     __a = "PuneFactory" # Class attribute
    
#     def show(self):
#         print(Factory.__a)
        
# obj = Factory() # Object
# obj.show() # Accessing method


# class Info():
#     def __init__(self):
#         self.name = "Hemant"   #Public
#         self._age = 30         #Protected
#         self.__salary = 1000   #Private
        
#     def show(self):
#         print("Inside show method")
#         print("Public: ", self.name)
#         print("Protected: ", self._age)
#         print("Private: ", self.__salary)
        
# obj = Info() # Object
# obj.show() # Accessing method

# class Info():
#     def __init__(self):
        
#         self.__name = "hemant" 
        
# print(Info().__name)




# Abstraction OOPS

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self, side):
#         self.side = side
        
#     def perimeter(self):
#         print("hello")
        
#     def area(self):
#         print("hi")
        
# class Circle(abstract):
#     def __init__(self, radius):
#         self.radius = radius
        
#     def perimeter(self):
#         print("hello")
        
#     def area(self):
#         print("hi")
        
# obj = Circle(7)
# obj2 = Square(12)



# Dunder methods
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age    
        
#     def __str__(self):
#         return f"hello, {self.name}"
    
#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age
            
#         return f"you sume of age {self.age + sum}"
        
# obj = Animal("Dog", 15)
# obj2 = Animal("Cat", 14)
# obj3 = Animal("Mouse", 40)

# print(obj)
# print(obj2)
# print(obj3)
# print(obj + (obj2, obj3))


# Advance stuff

# Decorator
# class Animal:
#     @property
#     def show(self):
#         print("hi")
        
# obj = Animal()
# obj.show



# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print("hi")
#         func(*args, **kwargs)
#         print("nice")
#     return wrapper

# @decorate
# def add(a,b):
#     print(f"Your Total is { a + b}")

# add(12, 12)


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
    
# add(12, 12, 12, 12)


# def Info(**kwargs):
#     print("Your Info Is")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    
# Info(name= "Hemant", age = 24, work="Developer")
    
    
    
# List, Dictionary and set comphrehension

# a = 13
# print("even") if a % 2 == 0 else print("odd")


# l = [i for i in range(1, 21) if i % 2 == 0 ]
# print(l)

# l = {i : i ** 2 for i in range(1, 10)}
# print(l)


# Lambda functions

# def add(a,b):
#     print(a + b)

# add(12, 13)

# add = lambda a, b : a + b
# print(add(12, 13))

# add = lambda a: "even" if a % 2 == 0 else "odd"
# print(add(7))



# Map filter and zip

# a = [1, 2, 3, 4, 5]
# square = map(lambda x : x * 2, a)
# print(list(square))


# a = [1, 2, 3, 4, 5]
# def double(x):
#     return x * 2

# result = map(double, a)
# print(list(result))



# a = [1, 2, 3, 4, 5]
# result = filter(lambda x : x % 2 == 0, a)
# print(list(result))

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
    
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = filter(even, a)
# print(list(result))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: True if x % 2 == 0 else False, a)
print(list(result))



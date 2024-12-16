# OOP Problems in Python

# Problem 1: Create a Class
class Dog:
    def bark(self):
        return "Woof!"

dog = Dog()
print("Problem 1:", dog.bark())

# Problem 2: Constructor
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

person = Person("Alice")
print("Problem 2:", person.greet())

# Problem 3: Class Variables
class Car:
    wheels = 4  # Class variable

    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")
print("Problem 3:", f"{car.brand} has {car.wheels} wheels.")

# Problem 4: Instance Variables
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Bob", 20)
print("Problem 4:", f"Student Name: {student.name}, Age: {student.age}")

# Problem 5: Method Overriding
class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal):
    def sound(self):
        return "Meow"

cat = Cat()
print("Problem 5:", cat.sound())

# Problem 6: Inheritance
class Vehicle:
    def drive(self):
        return "Driving"

class Bike(Vehicle):
    def ride(self):
        return "Riding"

bike = Bike()
print("Problem 6:", bike.drive())
print("Problem 6:", bike.ride())

# Problem 7: Multiple Inheritance
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

c = C()
print("Problem 7:", c.method_a())
print("Problem 7:", c.method_b())

# Problem 8: Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print("Problem 8:", "Balance:", account.get_balance())

# Problem 9: Class Method
class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

print("Problem 9:", "Area of circle:", Circle.area(5))

# Problem 10: Static Method
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print("Problem 10:", "Sum:", Math.add(5, 3))

# Problem 11: Property Decorator
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print("Problem 11:", "Area of rectangle:", rect.area)

# Problem 12: Abstract Class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(4)
print("Problem 12:", "Area of square:", square.area())

# Problem 13: Method Chaining
class Builder:
    def __init__(self):
        self.value = 0

    def add(self, amount):
        self.value += amount
        return self

    def subtract(self, amount):
        self.value -= amount
        return self

builder = Builder()
result = builder.add(10).subtract(5).value
print("Problem 13:", "Result of method chaining:", result)

# Problem 14: Class with Private Method
class Secret:
    def __init__(self):
        self.__secret = "This is a secret"

    def reveal_secret(self):
        return self.__get_secret()

    def __get_secret(self):
        return self.__secret

secret = Secret()
print("Problem 14:", "Revealed:", secret.reveal_secret())

# Problem 15: Class with Class and Instance Variables
class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1
        self.instance_count = Counter.count

counter1 = Counter()
counter2 = Counter()
print("Problem 15:", f"Counter1 instance count: {counter1.instance_count}, Total count: {Counter.count}")
print("Problem 15:", f"Counter2 instance count: {counter2.instance_count}, Total count: {Counter.count}")

# Problem 16: Class with a Method that Returns Another Class
class Factory:
    @staticmethod
    def create_car(brand):
        return Car(brand)

car = Factory.create_car("Honda")
print("Problem 16:", f"Created car brand: {car.brand}")

# Problem 17: Class with a Class Method that Modifies Class Variable
class Employee:
    raise_amount = 1.04  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    def apply_raise(self):
        self.salary *= self.raise_amount

employee = Employee("John", 50000)
employee.apply_raise()
print("Problem 17:", f"Salary after raise: {employee.salary}")

Employee.set_raise_amount(1.05)
employee2 = Employee("Jane", 60000)
employee2.apply_raise()
print("Problem 17:", f"Salary after raise for Jane: {employee2.salary}")

# Problem 18: Class with a Static Method for Validation
class Validator:
    @staticmethod
    def is_positive(number):
        return number > 0

print("Problem 18:", "Is 5 positive?", Validator.is_positive(5))
print("Problem 18:", "Is -3 positive?", Validator.is_positive(-3))

# Problem 19: Class with a Method that Returns a List of Instances
class Book:
    instances = []

    def __init__(self, title):
        self.title = title
        Book.instances.append(self)

    @classmethod
    def get_all_books(cls):
        return [book.title for book in cls.instances]

book1 = Book("1984")
book2 = Book("To Kill a Mockingbird")
print("Problem 19:", "All books:", Book.get_all_books())

# Problem 20: Class with a Method that Uses Inheritance
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

circle = Circle(3)
print("Problem 20:", "Area of circle:", circle.area())

# Problem 21: Class with a Method that Returns the Number of Instances
class InstanceCounter:
    count = 0  # Class variable

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count

instance1 = InstanceCounter()
instance2 = InstanceCounter()
print("Problem 21:", "Number of instances created:", InstanceCounter.get_instance_count())

# Problem 22: Class with a Method that Checks for Equality
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(2, 3)
print("Problem 22:", "Point1 equals Point2?", point1 == point2)
print("Problem 22:", "Point1 equals Point3?", point1 == point3)

# Problem 23: Class with a Method that Returns a String Representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

person = Person("Alice", 30)
print("Problem 23:", "Person:", person)

# Problem 24: Class with a Method that Raises an Exception
class AgeValidator:
    @staticmethod
    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        return True

try:
    AgeValidator.validate_age(-5)
except ValueError as e:
    print("Problem 24:", e)

# Problem 25: Class with a Method that Uses a Decorator
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(25)
print("Problem 25:", f"Temperature in Fahrenheit: {temp.fahrenheit}")

# Problem 26: Class with a Method that Implements a Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print("Problem 26:", "Are both instances the same?", singleton1 is singleton2)

# Problem 27: Class with a Method that Implements a Factory Pattern
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle(1)  # Default radius
        elif shape_type == "square":
            return Square(1)  # Default side
        raise ValueError("Unknown shape type")

shape1 = ShapeFactory.create_shape("circle")
shape2 = ShapeFactory.create_shape("square")
print("Problem 27:", "Created shapes:", type(shape1).__name__, type(shape2).__name__)

# Problem 28: Class with a Method that Implements Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

car = Car()
print("Problem 28:", car.start())

# Problem 29: Class with a Method that Implements Aggregation
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title):
        self.title = title

library = Library()
book1 = Book("1984")
library.add_book(book1)
print("Problem 29:", "Books in library:", [book.title for book in library.books])

# Problem 30: Class with a Method that Implements Polymorphism
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
print("Problem 30:", "Dog sound:")
animal_sound(dog)
print("Problem 30:", "Cat sound:")
animal_sound(cat)

# Problem 31: Class with a Method that Implements a Custom Iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

countdown = Countdown(5)
print("Problem 31:", "Countdown:")
for number in countdown:
    print(number)

# Problem 32: Class with a Method that Implements a Context Manager
class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileHandler('test.txt') as f:
    f.write("Hello, World!")
print("Problem 32:", "Data written to file.")

# Problem 33: Class with a Method that Implements a Property Setter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

temp = Temperature(25)
print("Problem 33:", "Current temperature:", temp.celsius)
temp.celsius = 30
print("Problem 33:", "Updated temperature:", temp.celsius)

# Problem 34: Class with a Method that Implements a Class Invariant
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

account = BankAccount(100)
account.deposit(50)
print("Problem 34:", "Account balance after deposit:", account.balance)

# Problem 35: Class with a Method that Implements a Method Resolution Order (MRO)
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print("Problem 35:", "Method resolution order:", d.method())

# Problem 36: Class with a Method that Implements a Decorator for Logging
def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {method.__name__}")
        return method(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method_call
    def add(self, x, y):
        return x + y

calc = Calculator()
print("Problem 36:", "Addition result:", calc.add(5, 3))

# Problem 37: Class with a Method that Implements a Custom Exception
class NegativeValueError(Exception):
    pass

class ValueChecker:
    @staticmethod
    def check_value(value):
        if value < 0:
            raise NegativeValueError("Value cannot be negative.")

try:
    ValueChecker.check_value(-10)
except NegativeValueError as e:
    print("Problem 37:", e)

# Problem 38: Class with a Method that Implements a Singleton Pattern with Thread Safety
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

singleton1 = ThreadSafeSingleton()
singleton2 = ThreadSafeSingleton()
print("Problem 38:", "Are both instances the same?", singleton1 is singleton2)

# Problem 39: Class with a Method that Implements a Factory Method Pattern
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        raise ValueError("Unknown shape type")

shape = ShapeFactory.get_shape("circle")
print("Problem 39:", shape.draw())

# Problem 40: Class with a Method that Implements a Strategy Pattern
class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

data = [5, 2, 9, 1]
context = Context(ConcreteStrategyA())
print("Problem 40:", "Sorted data (A):", context.execute_strategy(data))

context.set_strategy(ConcreteStrategyB())
print("Problem 40:", "Sorted data (B):", context.execute_strategy(data))

# Problem 41: Class with a Method that Implements a Command Pattern
class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Light is ON"

    def turn_off(self):
        return "Light is OFF"

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()

light = Light()
turn_on_command = TurnOnCommand(light)
turn_off_command = TurnOffCommand(light)

print("Problem 41:", turn_on_command.execute())
print("Problem 41:", turn_off_command.execute())

# Problem 42: Class with a Method that Implements a Template Method Pattern
class DataProcessor:
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    def read_data(self):
        raise NotImplementedError

    def process_data(self):
        raise NotImplementedError

    def save_data(self):
        raise NotImplementedError

class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file.")

    def process_data(self):
        print("Processing CSV data.")

    def save_data(self):
        print("Saving data to CSV file.")

csv_processor = CSVDataProcessor()
print("Problem 42: Processing CSV data:")
csv_processor.process()

# Problem 43: Class with a Method that Implements a Visitor Pattern
class Visitor:
    def visit(self, element):
        pass

class Element:
    def accept(self, visitor: Visitor):
        visitor.visit(self)

class ConcreteElementA(Element):
    def operation_a(self):
        return "Operation A"

class ConcreteElementB(Element):
    def operation_b(self):
        return "Operation B"

class ConcreteVisitor(Visitor):
    def visit(self, element: Element):
        if isinstance(element, ConcreteElementA):
            print(element.operation_a())
        elif isinstance(element, ConcreteElementB):
            print(element.operation_b())

element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor = ConcreteVisitor()

print("Problem 43: Visitor Pattern:")
element_a.accept(visitor)
element_b.accept(visitor)

# Problem 44: Class with a Method that Implements a Mediator Pattern (continued)
class ComponentB(Component):
    def trigger_event(self):
        print("Component B triggers event B.")
        self.mediator.notify(self, "B")

component_a = ComponentA()
component_b = ComponentB()
mediator = ConcreteMediator(component_a, component_b)

print("Problem 44: Mediator Pattern:")
component_a.trigger_event()
component_b.trigger_event()

# Problem 45: Class with a Method that Implements a Chain of Responsibility Pattern
class Handler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handler A handled request A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Handler B handled request B"
        return super().handle(request)

handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.set_next(handler_b)

print("Problem 45: Chain of Responsibility Pattern:")
print(handler_a.handle("A"))
print(handler_a.handle("B"))
print(handler_a.handle("C"))

# Problem 46: Class with a Method that Implements an Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer received message: {message}")

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

print("Problem 46: Observer Pattern:")
subject.notify("Hello Observers!")

# Problem 47: Class with a Method that Implements a State Pattern
class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        return "State A handling"

class ConcreteStateB(State):
    def handle(self):
        return "State B handling"

class Context:
    def __init__(self, state: State):
        self.state = state

    def set_state(self, state: State):
        self.state = state

    def request(self):
        return self.state.handle()

context = Context(ConcreteStateA())
print("Problem 47: State Pattern:")
print(context.request())

context.set_state(ConcreteStateB())
print(context.request())

# Problem 48: Class with a Method that Implements a Prototype Pattern
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

prototype = ConcretePrototype(42)
cloned_prototype = prototype.clone()
print("Problem 48: Prototype Pattern:")
print("Original value:", prototype.value)
print("Cloned value:", cloned_prototype.value)

# Problem 49: Class with a Method that Implements a Builder Pattern
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def get_product(self):
        return self.product

builder = Builder()
builder.build_part_a()
builder.build_part_b()
product = builder.get_product()
print("Problem 49: Builder Pattern:", product.parts)

# Problem 50: Class with a Method that Implements a Composite Pattern
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return "Composite: [" + ", ".join(results) + "]"

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

print("Problem 50: Composite Pattern:")
print(composite.operation())


# # Python keyword showcase

# # Variable assignment
# x = 10

# # Conditional statement
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

# # Looping
# for i in range(5):
#     print(i)

# # Function definition
# def greet(name):
#     print("Hello, " + name + "!")

# # Function call
# greet("Alice")

# # List
# fruits = ["apple", "banana", "cherry"]

# # List iteration
# for fruit in fruits:
#     print(fruit)

# # Dictionary
# person = {"name": "John", "age": 30, "city": "New York"}

# # Dictionary access
# print(person["name"])

# # Exception handling
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")

# # Class definition
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# # Class instantiation
# rect = Rectangle(5, 3)

# # Method call
# print(rect.area())


import threading
import time
import random

class Fork:
    def __init__(self):
        self.lock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"{self.name} is thinking")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        with self.left_fork.lock:
            with self.right_fork.lock:
                print(f"{self.name} is eating")
                time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    forks = [Fork() for _ in range(5)]
    philosophers = [Philosopher(forks[i], forks[(i + 1) % 5]) for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()
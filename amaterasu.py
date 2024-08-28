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


# import threading
# import time
# import random

# class Chopstick:
#     def __init__(self):
#         self.lock = threading.Lock()

# class Genius(threading.Thread):
#     def __init__(self, left_chopstick, right_chopstick):
#         threading.Thread.__init__(self)
#         self.left_chopstick = left_chopstick
#         self.right_chopstick = right_chopstick

#     def run(self):
#         while True:
#             self.think()
#             self.eat()

#     def think(self):
#         print(f"{self.name} is thinking")
#         time.sleep(random.uniform(1, 3))

#     def eat(self):
#         with self.left_chopstick.lock:
#             with self.right_chopstick.lock:
#                 print(f"{self.name} is eating")
#                 time.sleep(random.uniform(1, 3))

# if __name__ == "__main__":
#     chopsticks = [Chopstick() for _ in range(5)]
#     geniuss = [Genius(chopsticks[i], chopsticks[(i + 1) % 5]) for i in range(5)]

#     for genius in geniuss:
#         genius.start()

#     for genius in geniuss:
#         genius.join()

# import threading
# import time
# import random

# class Chopstick:
#     def __init__(self):
#         self.lock = threading.Lock()

# class Arbitrator:
#     def __init__(self):
#         self.lock = threading.Lock()
#         self.available = [True] * 5
    
#     def request(self, left_index, right_index):
#         while True:
#             with self.lock:
#                 print(f"Arbitrator is checking availability of chopsticks {left_index} and {right_index}.")
#                 if self.available[left_index] and self.available[right_index]:
#                     self.available[left_index] = False
#                     self.available[right_index] = False
#                     print(f"Chopsticks {left_index} and {right_index} are granted to genius.")
#                     return
#                 else:
#                     print(f"Chopsticks {left_index} and {right_index} are not available. Genius must wait.")
#             time.sleep(random.uniform(0.1, 0.5))

#     def release(self, left_index, right_index):
#         with self.lock:
#             self.available[left_index] = True
#             self.available[right_index] = True
#             print(f"Chopsticks {left_index} and {right_index} have been released back to the table.")

# class Genius(threading.Thread):
#     def __init__(self, genius_number, left_chopstick, right_chopstick, arbitrator):
#         threading.Thread.__init__(self)
#         self.genius_number = genius_number
#         self.left_chopstick = left_chopstick
#         self.right_chopstick = right_chopstick
#         self.arbitrator = arbitrator

#     def run(self):
#         while True:
#             self.think()
#             self.arbitrator.request(self.genius_number, (self.genius_number + 1) % 5)
#             self.eat()
#             self.arbitrator.release(self.genius_number, (self.genius_number + 1) % 5)

#     def think(self):
#         print(f"Genius {self.genius_number} is thinking.")
#         time.sleep(random.uniform(1, 3))
    
#     def eat(self):
#         print(f"Genius {self.genius_number} is eating.")
#         time.sleep(random.uniform(1, 3))

# if __name__ == "__main__":
#     chopsticks = [Chopstick() for _ in range(5)]
#     arbitrator = Arbitrator()
#     geniuss = [Genius(i, chopsticks[i], chopsticks[(i + 1) % 5], arbitrator) for i in range(5)]

#     for genius in geniuss:
#         genius.start()

#     for genius in geniuss:
#         genius.join()

import threading
import time
import random

class Chopstick:
    def __init__(self):
        self.lock = threading.Lock()

class Arbitrator:
    def __init__(self):
        self.lock = threading.Lock()
        self.available = [True] * 5
    
    def request(self, left_index, right):
        while True:
            with self.lock:
                if self.available[left_index] and self.available[right]:
                    self.available[left_index] = False
                    self.available[right] = False
                    return
            time.sleep(random.uniform(0.1, 0.5))

    def release(self, left_index, right):
        with self.lock:
            self.available[left_index] = True
            self.available[right] = True

class Genius(threading.Thread):
    def __init__(self, genius_number, left_chopstick, right_chopstick, arbitrator):
        threading.Thread.__init__(self)
        self.genius_number = genius_number
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.arbitrator = arbitrator

    def run(self):
        while True:
            self.think()
            self.arbitrator.request(self.genius_number, (self.genius_number + 1) % 5)
            self.eat()
            self.arbitrator.release(self.genius_number, (self.genius_number + 1) % 5)

    def think(self):
        print(f"Genius {self.genius_number} is thinking")
        time.sleep(random.uniform(1, 3))
    
    def eat(self):
        print(f"Genius {self.genius_number} is eating")
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    chopsticks = [Chopstick() for _ in range(5)]
    arbitrator = Arbitrator()
    geniuss = [Genius(i, chopsticks[i], chopsticks[(i + 1) % 5], arbitrator) for i in range(5)]

    for genius in geniuss:
        genius.start()

    for genius in geniuss:
        genius.join()

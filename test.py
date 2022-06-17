# # There are a number of tiles on the floor, each numbered with a different non-negative integer. Treat this set of tiles as an array. You are initially standing on the first tile. Each tile in the set represents your maximum jumping distance at that position. (For example, if you are standing on 3, you can jump up to 3 tiles forward). Find out if you can reach the last tile.

# def can_jump(tiles):
#     if len(tiles) == 1:
#         return True
#     elif len(tiles) == 2:
#         return tiles[0] >= 1
#     else:
#         return can_jump(tiles[1:]) or (tiles[0] >= len(tiles) - 1 - tiles[1])

# Write a function which takes a list of numbers and returns the length of the longest continuous stretch of a single number. For example, on the input [1,7,7,3], the correct return is 2, because there are two 7's in a row.

# def longest_flat(nums):
#     if len(nums) == 1:
#         return 1
#     elif len(nums) == 2:
#         return 1 if nums[0] == nums[1] else 0
#     else:
#         return 1 + longest_flat(nums[1:]) if nums[0] == nums[1] else longest_flat(nums[1:])

# 

# x = "cat"
# def f():
#     x = "bird"
#     def g():
#         x = "dog"
#         y = "fist"
#         print(x)
#     g()
# f()

# given the python  dictionary below, which opetion would print the followint: algebra 99 python

# Choose the list comprehension that transform the 3x3 matrix: [ [1,2,3], [4,5,6], [7,8,9] ] into the following :
# [ [1,4,7], [2,5,8], [3,6,9] ]
# def transpose(matrix):
#     return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# which of the following is not valid python?
# def f(x,y,z):
#     return x+y+z
# print(f(z=3,y=2, 1))

# How to fix error "TypeError: Can't instantiate abstract class Car with abstract method start"

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, id):
#         self.id = id
    
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def honk(self):
#         print("beep beep")

# if __name__=="__main__":
#     car = Car('zippy')
#     car.honk()


# Assume we have a class Animal defined below. Which of the following would create a class Cat that inherits from Animal with a talk method that extend the talk method from Animal?

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print("Hi, I am", self.name)

# class Cat(Animal):
#     def talk(self):
#         speech = ta

# class Square:
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side * self.side

# class Cube(Square):
#     def surface_area(self):
#         return 6 * self.area()

# if __name__=="__main__":
#     print(Cube(6).surface_area())

# print(enumerate("python"))
# print(list(enumerate("python")))

# a = 0
# for i in range(10):
#     if i ==2:
#         pass 
#     else: a = i
# print(a)

# what's the difference between shutil.copy and shutil.copy2


# def mean(*args):
#     sum = 0
#     count = 0
#     for num in args:
#         sum += num 
#         count += 1
#     return sum / count

# if __name__ == "__main__":
#     print(mean(1,2,3,4,5))

# which of the following sets the docstring?
# def f():
#     """
#     This is a docstring

# 

# from urllib.request import rulopen
# EXCITING_NEW-VERSION = 'Python 4.0'


# which of the following is a property of Numpy universal funciton also known as ufuncs

# function returns a random integer between a innclusive a, 
# def choose(array):
#     result = None 
#     i = 0 
#     for item in array:
#         if randonint(0, len(array)) == i:
#             result = item
#         i += 1
#     return result

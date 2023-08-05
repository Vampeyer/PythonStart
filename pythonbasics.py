#This is a comment
print("Hello, World!")

x = 5
y = "Hello, World!" 

# this is how comments are written in python , 

""" and this will 
print the class types of the following variables in python """ 



print(type(x))
print(type(y)) 


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print(type(fruits))

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) 




#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

""" 
The best way to output multiple variables in
 the print() function is to separate
  them with commas, which even support different data types: """


x = 5
y = "John"
print(x, y)

"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

ExampleGet your own Python Server
Create a variable outside of a function, and use it inside the function
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""     

Global Variables
Variables that are created outside
 of a function (as in all of the examples above)
  are known as global variables.

Global variables can be used by everyone, 
both inside of functions and outside.


"""

x = "awesome , and this is a regular global value  "

def myfunc():
  print("Python is " + x)

myfunc()


#########DEMONSTRATION OF CHANGING AND PLACING LOCAL AND GLOBAL VARIABLES . 

x = "awesome second global value  "

def myfunc2():
  x = "fantastic ,  this is a local value"
  print("Python is " + x)

myfunc2()

print("Python is " + x)






''' The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example
If you use the global keyword, the variable belongs to the global scope: '''

def myfunc():
  global x
  x = "fantasticGlobalKeyword1"

myfunc()

print("Python is " + x)
"""
Also, use the global keyword if you want to change a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
xx = "awesome"

def myfunc():
  global xx
  xx = "fantasticGlobalKeyword2"

myfunc()

print("Python is " + xx)



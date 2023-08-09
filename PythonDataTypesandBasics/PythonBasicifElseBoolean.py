
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")     

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
Example
The following will return True:
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])   



########################################
#########BOOLEAN FALSES#################
########################################

'''
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None.
 And of course the value False evaluates to False.
Example
The following will return False:
bool({}) 
'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
'''

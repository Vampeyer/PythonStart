'''Example of Nested Conditionals

The outer conditional if a == b contains two branches:

The first branch contains a simple statement.
The second branch contains another if statement, which has two branches of its own.
Those two branches are both simple statements, although they could have been conditional statements as well.

'''
a = int(input("Enter a? "))
b = int(input("Enter b? "))    

if a == b:
    print('a and b are equal') 
else:
    if a < b:
        print('a is less than b')
    else:
        print('a is greater than b')
'''
	Enter a? 8
	Enter b? 5
	a is greater than b
'''
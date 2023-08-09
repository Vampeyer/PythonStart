


'''
Nested Conditionals

Several conditionals can also be nested one after the other.

Consider a script that is to describe the relationship between
 two integers a and b.

The questions that need to be answered are:

Are these two numbers equal?, 
if not
is a less than b? or
is a greater than b?
Example of Nested Conditionals

The outer conditional if a == b contains two branches:

The first branch contains a simple statement.
The second branch contains another if statement, which has
 two branches of its own.
Those two branches are both simple statements, although
 they could have been conditional statements as well.
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


print('Instructional book on achieving power level' +
'over 9000 ')		
x = int(input('Enter x '))

y = int(input('Enter that Y value ')) 


z = int(input('enter That Z value too ')) 


if x <= 2000: 
	print(' go train more and increase x ') 
else: 
	print('move onto next variable')
	if y <= 2000: 
		print(' go train more and increase y ') 
	else: 
		print('move onto next variable') 

		if z <= 2000: 
			print(' go train more and increase z') 
		else: 
			print('You now have a power level of over 9000 total , meditate on your accomplishments , and maintain health !  ')















x = 21
if x > 0: 
  print('x is positive')
  
# x is positive



'''
Integer Comparison Example

Write a script that will find the largest of three numbers by comparing
 them to each other.  

In the script you should: 

Ask the user for 3 integers: a, b, c
Compare each integer to the other two
Print which number is the largest
Example of multiple if statements to determine the largest:
'''

a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")








'''
  Enter a? 6
  Enter b? 9
  Enter c? 3
  b is largest
'''












'''
The expression  

n%2 == 0 or n%3 == 0 

is true if either n is divisible by 2 or if n is divisible by 3
'''



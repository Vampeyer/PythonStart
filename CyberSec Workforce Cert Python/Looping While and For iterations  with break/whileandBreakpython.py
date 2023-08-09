
'''
More on while statement

We can use other programming structures in the body of a while loop. 
 In the next example we would like to use a while loop to print the even
  integers between 1 and 16 and would like to skip the odd ones:

The plan of actions is to start at n = 1 and while n <= 16

Test: if n is even then print and change n to n + 1  else do not print 
but must change n to n + 1

We will start with an integer i:
Set i = 1
While our integer i <= 16
if  i is even
print i
change i to i+1
else
just change i to i+1
EXAMPLE:  Use a while loop to print the even integers between 1 and 16
'''

i = 1
while i <= 16:
    if i % 2 == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
print("We are done")


''' 
The break statement discussion

Notice that we start looping at i = 1.
Once we hit 7 we jump out of the loop to the last print statement.
Note the formatted print statement: print("i = %d" % i) 
It should be read as “print i using the format “i = a digit”
Use a while loop to start printing integers between one 
and 10 but if you hit 7 abort printing
'''

i = 1
while i <= 10:
    print("i = %d" % i)
    i = i + 1
    if i == 7:
        break
print("The while loop exhausted")  # This is optional

i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
 


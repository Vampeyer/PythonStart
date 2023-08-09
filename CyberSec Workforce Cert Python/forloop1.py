'''
looping with the for statement

The for statement is powerful looping structure that takes a much simpler form in python. In python, the for statement is restricted to iterations over elements of a sequence or a range of values.

The for loop over a range 

In python, the range() function in its simplest form returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

  range(5) is the set of integers {0, 1, 2, 3, 4}

The general form of the range function is 

range(start, end, step), stop at the last integer 
range(2, 7, 2) means we start at 2, jump by 2, we stop before we get to 7
range(2, 7, 2) is the set of integers {2, 4, 6}
We can iterate over this range by using a for as follow:

for i in range(2,7,2)

  do this …

Iterating over a range with for

To see the set of values in the range(2, 7, 2) we can use the for loop as seen to the right. In this case we are printing the value i for as long as i is in the range:

Starting at 2, incrementing by 2 and stopping just before we reach 7

Iterating over a range with for
'''


print(range(100))

for i in range(2,7,2):
    print(i)
'''
2
4
6
Another for over a range example

In this example we construct a table of integers and their square values. The number we chose is 9. Notice that the range started at 1 and the end was num+1 which is 9+1, i.e., 10. Have we used just num in the range we would have stopped at 8 

Create a table that shows a set of integers and their square values starting with 1 and until we reach a number, we  choose
'''
i=1
num = int(input(" this shows the highest exponentiated number  . in the range of your input , input here   Enter a number:"))
for i in range(1,num+1):
    print("%d : %2d" % (i, i*i))
	

'''
Enter a number:9
1 :  1
2 :  4
3 :  9
4 : 16
5 : 25
6 : 36
7 : 49
8 : 64
9 : 81
More on using for

In python for is well suited for use with sequences as in letters in a word or elements in a list. 
We will cover lists and strings more later but for now, we will introduce them in our examples.
Any String can be thought of as a sequence of letters
Cereal = “Fruit Loops”, Cereal[0] = ‘F’ … Cereal[10] = ‘s’

A list can be thought of as a sequence of values 
Week_Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

Examples of for over sequences and lists



1.  for over a sequence
'''
Cereal = "Fruit Loops"
for letter in Cereal:
    if letter != ' ' :
      print(letter)
    else:
      print('-')

'''
F
r
u
i
t
-
L
o
o
p
s
2.  for over a list

'''
Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in Weekdays :
  if day != "Saturday" and day != "Sunday":
    print("It must be workday")
  else:
    print("It must be the week-end")


'''	
It must be the week-end
It must be workday
It must be workday
It must be workday
It must be workday
It must be workday
It must be the week-end
'''
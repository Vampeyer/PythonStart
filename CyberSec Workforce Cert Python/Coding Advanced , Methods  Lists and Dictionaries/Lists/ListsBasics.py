'''
What is a List

Like a string, a list is a sequence of values

In a string, the values are characters but in a list they can be any type
The values in a list are called elements or sometimes items
A simple way to create a list is to enclose the sequence of elements in square brackets [ and ] , as shown below 

Example list
Description
[10, 20, 30, 40]	List of integer elements
['orange', 'apple', 'banana']	List of string elements
['thermometer', 25, 9.99]
Heterogeneous list of elements
[]
Empty list
Lists are mutable

Unlike strings, lists in Python are mutable so elements in a list can be changed by using an index to access and alter a specific value.  The first element in a list is found at index [0]

EXAMPLE:  in the following code fragment, the 2nd list element is replaced by a new value using index [1] to access it:
'''
numbers = [10, 20, 30, 40]
print(numbers)
#[10, 20, 30, 40]
numbers[1] = 25
print(numbers)
#[10, 25, 30, 40]



admissions = [124, 115, 102, 107, 99, 96, 88]   # ​
 # this will print the last digit in the list array 
print(admissions[6])
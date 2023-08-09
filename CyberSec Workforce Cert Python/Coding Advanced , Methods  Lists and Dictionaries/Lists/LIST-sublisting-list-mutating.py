'''
List Slices

As with strings, the slice operator can be used to extract a sublist of the existing elements in a list

EXAMPLE:
'''
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
#['b', 'c']
print(t[:4]) # Starts from beginning
#['a', 'b', 'c', 'd']
print(t[3:]) # Stops at end
#['d', 'e', 'f']
print(t[:]) # Creates a copy of the list
#['a', 'b', 'c', 'd', 'e', 'f']
#Be careful, though, since lists are mutable unlike strings

#A slice operator on the left side of an assignment can update multiple elements: 

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
#['a', 'x', 'y', 'd', 'e', 'f']
#This can also be true even when accessed from a different variable if the elements are mutable, such as when a list is nested inside another list as an element

#Here, s1 may represent a student's name and associated list of test scores:

s1 = ['Carlos', [97, 92, 95]]
print(s1) 







####################################3



List Slices

As with strings, the slice operator can be used to extract a sublist of the existing elements in a list

EXAMPLE:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
#['b', 'c']
t[:4] # Starts from beginning
#['a', 'b', 'c', 'd']
t[3:] # Stops at end
#['d', 'e', 'f']
t[:] # Creates a copy of the list
#['a', 'b', 'c', 'd', 'e', 'f']
'''
Be careful, though, since lists are mutable unlike strings

A slice operator on the left side of an assignment can update multiple elements: 
'''


t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
#['a', 'x', 'y', 'd', 'e', 'f']
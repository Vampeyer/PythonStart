'''
Deleting Elements

There are several ways to delete elements from a list using methods pop and
 remove or the del operation

Method pop removes the element specified by index and returns its
 value•If you don't specify an index, it removes and returns the 
 last element by default
The remove method instead removes the first element that matches
 the specified value•If the specified value is not in the list, a
  ValueError will be raised
The del operation can remove a single element or a range of values
 using slice notation
See: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
 and https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

For del operation, see:
 https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
 '''

numbers = list(range(1, 11))
print(numbers)
print(' range method starts and stops  ')
          #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = numbers.pop() # Removes last item

print('.pop() Removes last item')

print(num, numbers)
           #[1, 2, 3, 4, 5, 6, 7, 8, 9]
num = numbers.pop(0) # Removes first item
print('.pop(0) Removes first item')
print(num, numbers)
           #[2, 3, 4, 5, 6, 7, 8, 9]
numbers.remove(5) # Removes value 5
print('.remove() Removes value 5')
print(numbers)
           #[2, 3, 4, 6, 7, 8, 9]
del numbers[3] # Removes element at index [3]
print ( 'Removes element at index [3]')



print(numbers)
[2, 3, 4, 7, 8, 9]
del numbers[::2] 

           # Removes every other item
print(numbers)
[3, 7, 9]


#REMOVES ALL ITEMS  
del numbers[::] 
del * []






## REMOVES THE FIRST TWO ITEMS 
case_counts = [150, 97, 111, 88, 129]
 
del case_counts[:2]

#prints  [111, 88, 129]
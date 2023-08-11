'''
Dictionary Operations

An empty dictionary is represented by a pair of curly braces { }

A key-value pair may be added to an existing dictionary by using an assignment statement
 with [key] syntax similar 
 to a list's [index] syntax
 '''
number_words = {'one' : 1, 'two' : 2, 'three' : 3}
print(number_words)
number_words['four'] = 4
print(number_words)
#{'one': 1, 'two': 2, 'three': 3, 'four': 4}
#If the key already exists in the dictionary, the assignment statement will replace the associated value with 
#the newly assigned value instead



#Values may be retrieved using the [key] syntax, as well:

print(number_words['two'])
#2
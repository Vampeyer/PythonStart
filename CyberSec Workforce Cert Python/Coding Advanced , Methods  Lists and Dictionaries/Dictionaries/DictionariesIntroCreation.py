'''

A dictionary is a collection that creates associations between pairs of 
objects

In a list, you use an integer index to retrieve a value but, in a dictionary, 
you aren't limited to sequential integer indices. For example, a dictionary could map a string, such as a patient's name or patient ID, onto an associated value, such as their room number or current vital signs. The object used to look up the associated value is known as the dictionary's key and the combination is known as a key-value pair. Each key in a Python dictionary must be unique for the lookup of its associated value to work and the key's type must be immutable. So, you can use a string or an integer as a key but you can't use a list as a dictionary's key

Dictionary Creation

There are many ways to create a dictionary in Python but the most common is to use a comma-separated list of key : value pairs enclosed within curly braces { }
'''
number_words = {'one' : 1, 'two' : 2, 'three' : 3}
print(number_words)
#{'one': 1, 'two': 2, 'three': 3} 
'''
Be aware that dictionaries don't maintain a sequence as lists do, so when you print a dictionary, the key-value pairs may appear in any order. The
 pairs are maintained in the collection to make lookups by key efficient
 '''
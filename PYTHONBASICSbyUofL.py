'''Arithmetic Operators  

The expression 2 + 3 + 7 uses the arithmetic operator +

Other operators we may use in Python expressions are:

  -     the minus operator

  *    the multiplication operator

  /     the division operator

  //   another division operator (what’s the difference?

  %   the mod operator (remaindering operator)

  **  the exponentiation operator


---------------------------------------------------------------

Scripts Involving Arithmetic Expressions

Consider the screenshot shown below

Each expression typed leads to the result shown on the line below it
Note that 8 / 3 yields a result with the decimal part and 8 // 3 yields an integer result
Also, 8 / 2 yields 4.0 as opposed to 4 because of / as opposed to //
13 % 5 yields the remainder when 13 is divided by 5
2**3 calculates 23 (Exponentiation) [Python uses ^ for something else]



'''
'''--------------------------------------------------------------------------------------------
'''
print("Data Types and Values, \n \n A value is a letter, number, or a string \n \n 2 2.466,  Hello Python! are examples of values \n Each value is of a specific data type. \n 2 is an integer (int) \n 2.466 is a floating-point number  \"Hello Python!\" is a string string \n  The term  \"class\" /n is used by Python to identify the category of data being defined by the value.") 




'''

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it
 could mean an increase in efficiency or security.


'''
# List of integers
my_list = [1, 2, 3, 4, 5]

# List of strings
my_string_list = ["one", "two", "three", "four", "five"]

# List of mixed data types
my_mixed_list = [1, "two", 3.0, True, [1, 2, 3]]
 
'''   CANNOT BE PRINTED BECAUSE LISTS AINT HASHABLE !    
print("my list" + my_list);
print("my string list " +  my_string_list);
print("my mixed list " + my_mixed_list);  

 SO TO FIX THIS , PRINT THEM AS A STRING TYPE , AS FOLLOWS

'''

print("my list" + str(my_list));
print("my string list " +  str(my_string_list));
print("my mixed list " + str(my_mixed_list));  


'''
Tuples are also ordered collections of data, but they are unchangeable.
 This means that you cannot add or remove elements from a tuple once it has been created. Tuples are created using parentheses (()), and elements are separated by commas.

Python
'''
# Tuple of integers
my_tuple = (1, 2, 3, 4, 5)

# Tuple of strings
my_string_tuple = ("one", "two", "three", "four", "five")

# Tuple of mixed data types
my_mixed_tuple = (1, "two", 3.0, True, [1, 2, 3])
'''
Use code with caution. Learn more
Sets are unordered and unchangeable collections of unique elements.
 This means that the order of the elements in a set does not matter, and you cannot have duplicate elements in a set. Sets are created using curly braces ({}), and elements are separated by commas.
'''

print("my tuple " + str(my_tuple));
print("my string tuple " + str(my_string_tuple));
print("my mixed tuple " + str(my_mixed_tuple));


#Python
# Set of integers
my_set = {1, 2, 3, 4, 5}

# Set of strings
my_string_set = {"one", "two", "three", "four", "five"}

# Set of mixed data types
my_mixed_set = {7, "two", 3.0, True, (1, 2, 3)} 



print("my set " + str(my_set));
print("my string set " + str(my_string_set));
print("my mixed set " + str(my_mixed_set));

'''
Dictionaries are unordered and changeable collections of key-value pairs.
 The keys of a dictionary must be unique, but the values can be anything. Dictionaries are created using curly braces ({}), 
and key-value pairs are separated by colons (:).

#Python

# Dictionary of integers and strings'''
my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

# Dictionary of strings and floats
my_string_dict = {"one": 1.0, "two": 2.0, "three": 3.0, "four": 4.0, "five": 5.0}

# Dictionary of mixed data types
my_mixed_dict = {1: "one", "two": 2.0, 3.0: True, "four": [1, 2, 3]}


print("my dict " + str(my_dict));
print("my string dict " + str(my_string_dict));
print("my mixed dict " + str(my_mixed_dict));

'''
These are just a few basic examples of how to use Python data types. 
For more information, please see the Python documentation: https://www.w3schools.com/python/python_datatypes.asp.
'''


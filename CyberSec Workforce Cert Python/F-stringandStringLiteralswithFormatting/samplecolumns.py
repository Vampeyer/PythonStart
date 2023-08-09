



'''
Example -  Consider the following example, solved with and without an 
f-string:

>>> name = 'Mary'
>>> age = 37
>>> print(name + ' is ' + str(age) + ' years old.')
Mary is 37 years old.

>>> print(f'{name} is {age} years old.')
Mary is 37 years old.
Note how the f-string avoids the need to concatenate the string and use the string 
constructor to convert the numeric variable to a string when printing

See: https://docs.python.org/3/reference/lexical_analysis.html#f-strings and
 https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals

You can control the formatting of the replacement field expressions by using a
 format specifier that dictates how the expression will be formatted

The format specifier can dictate a minimum width for the field so as you might
 want when creating columns in multi-line output

This width is specified immediately after the : that follows the expression

EXAMPLE: if you wanted a report with a column for first names and a column for 
last names, each 10 characters wide, you might write:

print(f'{f_name:10} {l_name:10}')
'''

firstname = ['Mary', 'John' , 'Jingle', 'Heimmerschmidt' ]
lastname = ['Louie' , ' George' , 'Henry' , 'Alfred' ]
age = 37

(f'{name} is {age} years old.')

print(f'{f_firstname:4} {l_lastname:4}')


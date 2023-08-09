'''
Helpful String Methods

Python strings provide built-in methods that perform a variety of useful operations

A method is similar to a function in that it takes arguments and returns a value, but the syntax is different
A function typically accepts an object as an argument and acts on the object, as in:
fn_acts_on(obj)

A method, however, starts with the object being acted on and uses dot notation to specify the method that will be called to act on it, as in:
 obj.method_that_acts_on()

Python string methods are documentation


STRING METHODS TO CHANGE CASE

STRING METHODS THAT SEARCH FO...
String methods to change case



Python provides several methods to change the case of characters in a string as needed, the simplest being upper and lower

As their names suggest, these methods change all alphabetic characters in a string to uppercase or lowercase
Recall, since strings are immutable, these methods will not alter the original string at all, instead returning a copy of the string with the specified changes
There are also methods that test the case of letters in strings including isupper and islower
If you only need to capitalize the first letter in a string (as you might for each sentence in a paragraph), method capitalize will do the work



If you need to capitalize each word in a string (as might in a title), method title will do the work



Python string methods are documentation



There are many string methods that test the characters contained in a string. See the is methods, starting with isalnum and ending with isupper here



EXAMPLE

'''
acronym = 'nsa'
agency = 'national security agency'
print(agency.title())
#'National Security Agency'
print(acronym.upper())

#'NSA'
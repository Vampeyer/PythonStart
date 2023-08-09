'''
String Slices
A segment of a string, or substring, can be created through a slice operation
While the simple index operation returns a single character using a single index, the slice operation can extract more than one character in the resulting string by specifying starting and ending indices much like the range function
EXAMPLE:
'''
s = 'Hello World'
print(s[0:5])
#'Hello'

print(s[6:11]) 
#'World'

'''
If you omit the first index (before the colon), the slice starts
 at the beginning of the string, at index [0]
EXAMPLE:
'''

s = 'Hello World'
print(s[:5])
#'Hello'

print(s[6:]) 

#'World'
'''
If the first index is greater than or equal to the second,
 the result is an empty string

If you omit both indices, you get a copy of the entire string
 being sliced
 '''
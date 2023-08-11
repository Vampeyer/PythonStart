#If you need to remove a key-value pair from a dictionary, a del statement may be used:

number_words = {'one' : 1, 'two' : 2, 'three' : 3}
del number_words['one']
print(number_words)
#{'two': 2, 'three': 3}     


# deleting the key 
del number_words['three'] 
print(number_words) 


#adding the key back 
number_words[3] = 'three' 
print(number_words) 


# adding the value back 
number_words['three'] = 3 
print(number_words)
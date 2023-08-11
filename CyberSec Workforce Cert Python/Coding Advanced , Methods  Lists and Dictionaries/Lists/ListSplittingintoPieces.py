'''
The list function breaks a string into individual letters but if you want to break a string into words, you can use the split method. 

By default, words in a string get split into the list wherever spaces occur but you can specify a delimiter string to use as word boundaries

See: https://docs.python.org/3/library/stdtypes.html#str.split
'''
s = 'National Security Agency'
words = s.split()
print(words)
#['National', 'Security', 'Agency']
 url_str = 'www.mywebsite.com'
url_list = url_str.split('.')
print(url_list)
#['www', 'mywebsite', 'com']
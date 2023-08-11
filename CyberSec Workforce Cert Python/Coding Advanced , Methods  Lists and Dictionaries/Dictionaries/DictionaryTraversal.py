'''
Dictionary Traversal

A for loop may be used to traverse the keys stored in a dictionary but no specific sequence for the keys is guaranteed unless you sort them first
'''
icu_beds = { 'Mercy North' : 10, 'Mercy South' : 12, 'Mercy Midtown' : 8 }
for name in icu_beds:
        print(name, 'has', icu_beds[name], 'ICU beds.')
'''
Mercy North has 10 ICU beds.
Mercy South has 12 ICU beds.
Mercy Midtown has 8 ICU beds.
'''
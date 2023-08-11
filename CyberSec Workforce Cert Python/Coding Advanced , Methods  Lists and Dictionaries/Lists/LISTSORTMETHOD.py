'''
List method sort rearranges the elements of the list from low to high•You may add the optional keyword argument reverse=True to go from high to low instead

See: https://docs.python.org/3/library/stdtypes.html#list.sort

If you want to see sorted result without modifying the list, you can use method sorted. It returns a new sorted list. 
'''
case_counts = [150, 97, 111, 88, 129]
case_counts.sort()
print(case_counts)
#[88, 97, 111, 129, 150]
case_counts.sort(reverse=True)
print(case_counts)
#[150, 129, 111, 97, 88]
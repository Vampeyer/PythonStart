'''
List Comparisons

The relational operators work for lists on an element-by-element basis.

Consider:  
'''
list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = [10, 20, 30, 40]

print(list1 == list2) # Same length, same elements in seq.
#True
print(list1 == list3) # Different length
#False
list1 < list3 # Elements 0-2 match but fewer elements
#True
list3 >= list1 # Elements 0-2 match but more elements
#True


''' 
Given the following list:
what value is returned by [101, 102] <= room_numbers ?


'''
room_numbers = [101, 102, 103, 104]
 
print([101, 102] <= room_numbers) 
###3THIS PRINTS TRUE ### 
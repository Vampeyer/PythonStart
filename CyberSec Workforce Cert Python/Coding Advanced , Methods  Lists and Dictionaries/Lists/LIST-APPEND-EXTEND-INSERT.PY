
'''
List Methods

Python provides many list methods to help use lists efficiently

Methods append, extend, and insert add values to an existing list


bullet
append adds a single item onto the end of a list


bullet
extend adds a sequence of items onto the end of a list


bullet
insert adds a new item into a list at a specified index, shifting existing elements to accommodate the new item
'''
admissions = [12, 15, 9]
admissions.append(14)
print(admissions)
#[12, 15, 9, 14]
admissions.insert(0, 13)
print(admissions)
#[13, 12, 15, 9, 14]
weekend_admissions = [16, 10]
admissions.extend(weekend_admissions)
print(admissions)
[13, 12, 15, 9, 14, 16, 10]
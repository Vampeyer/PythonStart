'''
Nested Lists

More commonly, nested lists are used to represent tabular information, arranged into rows and columns similar to a spreadsheet

Consider the following nested list representing a table of student test scores – each row represents a student and each column represents a test's scores:
'''
tests = [[97, 92, 95], [90, 94, 89], [91, 93, 97]]



'''
Nested Lists Example - Code

To traverse a 2-dimensional list, use nested loops as shown below:
'''
tests = [[97, 92, 95], [90, 94, 89], [91, 93, 97]]
for row in tests:
        for score in row:
            print(score, end=' ')
        print()
        '''

##THIS PRINTS A THREE DIMENSIONAL ARRAY.   

97 92 95 
90 94 89 
91 93 97 '''
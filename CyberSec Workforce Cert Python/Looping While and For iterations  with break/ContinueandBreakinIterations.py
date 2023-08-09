'''
The continue statement

The continue statement returns the execution to the beginning of the loop for each of the while loop or the for loop. It does so by skipping all the remaining statements in the current iteration and moving to the next iteration.

The following two examples contrast the continue with the break.  Notice the continue skips the 7 only while break skips all the cases after 7.

The Continue Example
'''

i = 0
while i < 10:
    i = i + 1
    if i == 7:
     continue
    print("i = %d" % i)
print("The while loop exhausted")  # This is optional
'''
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 8
i = 9
i = 10
The while loop exhausted
The Break Example
'''
i = 0
while i < 10:
    i = i + 1
    if i == 7:
     break
    print("i = %d" % i)
print("The while loop exhausted")  # This is optional
'''
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
The while loop exhausted
'''










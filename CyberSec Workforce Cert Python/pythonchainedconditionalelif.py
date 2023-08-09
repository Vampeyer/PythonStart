'''
Chained Conditionals

Sometimes there are more than two possibilities, and we need more than two branches.

One way to express a computation like that is a chained conditional:

This is typically called if … elif  or if … else if statement
The example to the right illustrates the syntax
Notice: 
Exactly one branch will run. 
There is no limit on the number of elif statements. 
If there is an else clause, it has to be at the end, but there
Example of chained if elif ... statements illustrating "Chained execution"
'''
score = int(input("Enter the score? "))
if 90 <= score <= 100:
    print("Congrats! you scored an A ...")
elif 80 <= score < 90:
    print("You scored a B ...")
elif 70 <= score < 80:
    print("You scored a C ...")
elif 60 <= score < 70:
    print("You scored a D ...")
else:
    print("Sorry you did not make it")


'''
	Enter the score? 77
	You scored a C ...
'''
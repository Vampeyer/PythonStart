
'''
The else statement with while and for

Both the while statement and the for support and else statement at the end.

In the while structure the else statement is executed when the condition fails
In the for structure the else executes after the loop complete fully
The else statement with while
'''
i = 1
while i <= 18:
    if i % 2 == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
else:
  print("We are done")
  '''
2  
4  
6  
8  
10  
12  
14
16
18
We are done
The else statement with for
'''
Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in Weekdays :
  if day != "Saturday" and day != "Sunday":
    print("It must be workday")
  else:
    print("It must be the week-end")
else:
    print("There are no more days in the week")
'''    
It must be the week-end
It must be workday
It must be workday
It must be workday
It must be workday
It must be workday
It must be the week-end
There are no more days in the week
'''
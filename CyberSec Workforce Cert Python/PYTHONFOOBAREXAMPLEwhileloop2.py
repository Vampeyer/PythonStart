n = 5
while n > 0 :
  print(n)
  n = n - 1
  print('the next in line ')

   

print ("We are done")




# nested if inside while statement 

i = 1
while i <= 16:
    if i % 2 == 0:
        print(i)
        print('printed up the even number ')
        i = i + 1   # THIS IS AN INCREMENTAL EXPRESSION # I gets 1 indivicual I added to its count
    else:
        i = i + 1
print("We are done")


foo = 'foo' 
bar = 'bar'  


i = 100  

while i >= 0 : 
    i = i -1
    if i % 2 == 0:    # this says , if i , when divisible by two, has a remainder of zero , then ... or otherwise , 
        print(foo)
    else:
        print(bar)                                      #When it is even , do this  -  
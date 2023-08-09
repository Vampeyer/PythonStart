Slicing with Steps

As with the range function, slices can also use a step argument to determine which indices are used when making its copy.

EXAMPLE: the following code copies every other letter by using a step size of 2:

fruit = 'banana'
 print(fruit[0:5:2])
#'bnn'
#Similarly, a step size of -1 will create a copy in reverse order:
#               STEP SIZING STARTS AT THE -FIRST VALUE like -1 
fruit = 'banana'
print(fruit[::-1])
#'ananab'
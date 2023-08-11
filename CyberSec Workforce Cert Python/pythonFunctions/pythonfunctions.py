'''
Example:  Creating Our Own Functions

A function definition contains a header and a body.  The keyword def, as part of the           header, begins the definition.  The body of a function contains statements.
'''

def my_function(x):
  """This function takes an integer as input and returns its square."""

  # Enter value
  square = x * x

  # Exit value
  return square

print(my_function(5))




def print_greetings( ):
        print("Welcome to Python functions!")

def repeat_greetings( ):
        print_greetings( )
        print_greetings( )
        print_greetings( )

repeat_greetings( )

'''
Welcome to Python functions!
Welcome to Python functions!
Welcome to Python functions!
'''




def calculate_BMI(weight, height):
         return weight / height ** 2

 calculate_BMI(69,1.6)

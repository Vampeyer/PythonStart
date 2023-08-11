
# i === patientID number 


# BMI Calculator Base - 
def bmi_calc(w,h):
		bmi = w / (h * h) * 703
		return bmi


# Chained conditional for inputs,  and outputs to 
#decide Weight Category based on BMI 


#Example of chained if elif ... statements illustrating "Chained execution"

name = '' 
i = 0                                 # Code that executes when entering a positive ID number
#i = int(input('Input a number : '))
while i >= 0:

	i = int(input('Input yout PatientID number : '))
	name = str(input('Enter patients name here : '))
	
	w = float(input('Enter patients weight here'))

	if w <= 0:   # continue if the weight is a  positive integer
		print(" Please type a valid weight")
		break  # break if its not a positive integer 
	h = float(input('Enter patients height here'))
	if h <= 0:
		print('Please enter a valid height')
		break

	PatientsBMI = bmi_calc(w,h)
	print(f'The patient {name} has a patientID of {str(i)}  , they have a weight of {w} and a height of {h} ,  - This patients BMI is {PatientsBMI} ')  # displays ID Number in menu. 
	print(f'Your bmi is {PatientsBMI}')

	if PatientsBMI >= 30 :
		print("Patient is in the Obese category")
	elif PatientsBMI >= 25:
		print("Patient is in the Overweight category")
	elif PatientsBMI > 18.5:
 	  	print("Patient is in the Healthy weight category")
	elif PatientsBMI < 18.5:
  		print("Patient is in the Underweight")
	else:
   		print("Sorry you did not make it")





'''
i = int((input(' Input a number:  ' )))
print(bool(i))
'''
'''
i = 0
#i = int(input('Input a number : '))
while i >= 0:
	i = int(input('Input a number : '))
	print(f'The number is {i}')
    
'''
'''
i2 = 1
while i2 <= i:
  print(i)
  i2 += 1


     
x = int(input("Enter a number to see its square root displayed: "))   
def my_function(x):
  """This function takes an integer as input and returns its square."""
  # Enter value
  square = x * x
  # Exit value
  return square

print(my_function(x))
'''
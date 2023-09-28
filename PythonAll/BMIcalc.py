
# i === patientID number 


# BMI Calculator Base - 
def bmi_calc(w,h):
		bmi = w / (h * h) * 703
		return bmi


# Chained conditional for inputs,  and outputs to 
#decide Weight Category based on BMI 


####making an additional patient list addition and display. 
'''
def PatientDataEntry():
	TotalPatients = {name:'name' ,
				   patientID:000, 
				   Height: 1 , 
				   Weight: 1,
				   age: 1, 
				   }
	print(TotalPatients)

	TotalPatients.name = 'New Name' 
	print(TotalPatients)
	return TotalPatients
PatientDataEntry()
'''
# THIS IS HOW TO ADD CONTENT TO A DICT 
'''
x = dict(name="John", age=36)	# 	dict	

weight = 0
x[weight] = 200
print(x)
height = 0

x[height] = 6
print(x)
print(f'The new weight is {x[weight]}, and height is {x[height]} ')
print(x)

###**************************************************************
###However ,  this is throwing errors for not replacing the dict properly. 
###***************************************
'''

# THIS IS - The Proper Way - of  HOW TO ADD CONTENT TO A DICT 

number_words = {'one' : 1, 'two' : 2, 'three' : 3}
print(number_words)
number_words['four'] = 4
print(number_words) 
five = 5
number_words[five] = 5 
print(number_words)
height = 20
number_words[height] = 20
print(number_words)


print(f'The new weight is {number_words[five]}, and height is {number_words[height]} ')

'''
i = 0 
name = 'r' 
w = 1 
h = 1 

def placingPatientInfo(i, name, w, h):
	patientInformation = { }
	 
	patientInformation['PatientID'] = i
	patientInformation['name'] = name
	patientInformation['Weight'] = w
	patientInformation['height'] = h 
	return print(patientInformation)


##################################################
#Example of chained if elif ... statements illustrating "Chained execution"
'''

patient_data = {}
i = 0
while i >= 0:




    i = int(input('Input your PatientID number : '))
    name = str(input('Enter patients name here : '))

    w = float(input('Enter patients weight here'))
    if w <= 0:
        print(" Please type a valid weight")
        break

    h = float(input('Enter patients height here'))
    if h <= 0:
        print('Please enter a valid height')
        break

    PatientsBMI = bmi_calc(w, h)
    print(f'The patient {name} has a patientID of {str(i)} , they have a weight of {w} and a height of {h} ,  - This patients BMI is {PatientsBMI} ')
    print(f'Your bmi is {PatientsBMI}')

    if PatientsBMI >= 30:
        print("Patient is in the Obese category")
    elif PatientsBMI >= 25:
        print("Patient is in the Overweight category")
    elif PatientsBMI > 18.5:
        print("Patient is in the Healthy weight category")
    elif PatientsBMI < 18.5:
        print("Patient is in the Underweight")
    else:
        print("Sorry you did not make it")
   
    display = input(' Would you like to see the patient data ? y / n ? ')
    
    Y = 'y' 
    
    print(display)
    patient_data['PatientId'] = i
    patient_data['name'] = name 
    patient_data['Height'] = h
    patient_data['Weight'] = w

    if display == Y:
        print(patient_data) 
    


    #print(patient_data)


'''
	if display == 'Y':
 	   placingPatientInfo(i, name, w, h)

'''
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






# Right method to add content into a dict -  

''' 

# THIS IS - The Proper Way - of  HOW TO ADD CONTENT TO A DICT 
number_words = {'one' : 1, 'two' : 2, 'three' : 3}
print(number_words)
number_words['four'] = 4
print(number_words) 
five = 5
number_words[five] = 5 
print(number_words)
height = 20
number_words[height] = 20
print(number_words)


print(f'The new weight is {number_words[five]}, and height is {number_words[height]} ')

##################################################

'''
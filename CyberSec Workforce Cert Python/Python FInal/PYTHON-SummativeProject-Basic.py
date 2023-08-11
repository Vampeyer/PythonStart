
# BMI Calculator Base - 
def bmi_calc(w,h):
        bmi = w / (h * h) * 703
        return bmi




print(" Program Start")
### Program Start 
##################################################
#Example of chained if elif ... statements illustrating "Chained execution"


patient_data = {}
i = 0

while i >= 0:
    i = int(input('Input your PatientID number  :'))
    name = str(input('Enter patients name here  :'))

    w = float(input('Enter patients weight here  :'))
    if w <= 0:
        print(" Please type a valid weight")
        break

    h = float(input('Enter patients height here  :'))
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
   

# Below is extra content to display the patient data optionally , 
  # within the while loop.

    display = input(' Would you like to see the patient data ? y / n ? ')
    
    Y = 'y' 
    
    print(display)
    patient_data['PatientId'] = i
    patient_data['name'] = name 
    patient_data['Height'] = h
    patient_data['Weight'] = w

    if display == Y:
        print(patient_data) 
    


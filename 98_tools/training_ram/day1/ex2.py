#find body mass index (BMI) of a person given his/her weight and height
#<=25 fit, >25 fat
#BMI=weight_kg/height_meter^square

def getBMI(weight_kg, height_meter):
    return round(weight_kg/height_meter**2)

w=eval(input('Enter your weight: '))
h=eval(input('Enter your height: '))

bmi=getBMI(w,h)
print(bmi)

if bmi <= 25:
    print('You are fit')

if bmi > 25:
    print('You are fat')
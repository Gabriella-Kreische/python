from Exercises import colour

print('{}{}{}'.format(colour.green, '-' * 50, colour.clear))
print('Body Mass Index (BMI) Calculator')
print('{}{}{}'.format(colour.green, '-' * 50, colour.clear))

w = float(input('Please type your weight in kg: '))
h = float(input('Please type your height in cm: '))

bmi = float(w / ((h/100)**2))
print('BMI: {:.1f} kg/m\u00b2'.format(bmi))
underweight = 18.5
healthy = 24.9
overweight = 29.9
obese = 40

if bmi < underweight:
    print('Weight status: Underweight!')
elif bmi >= underweight and bmi <= healthy:
    print('Weight Status: Normal weight!')
elif bmi > healthy and bmi <= overweight:
    print('Weight Status: Overweight!')
elif bmi > overweight and bmi <= obese:
    print('Weight Status: Obese!')
else:
    print('Weight Status: Morbid Obesity!')

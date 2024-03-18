w = float(input('What is your weight? (Kg) '))
h = float(input('What is your height? (m) '))
bmi = w / (h ** 2)
print('Your BMI is {:.1f}'.format(bmi))

if bmi < 18.5:
    index = 'UNDERWEIGHT'
elif 18.5 <= bmi < 25:
    index = 'NORMAL'
elif 25 <= bmi < 30:
    index = 'OVERWEIGHT'
elif 30 <= bmi < 40:
    index = 'OBESE'
elif bmi >= 40:
    index = 'MORBID OBESE'
print('It correspond to an index of {}!'.format(index))

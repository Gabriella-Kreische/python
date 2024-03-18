gender = ''
while gender != 'F' and gender != 'M':
    gender = input('What is your gender? (F/M) ')
    if gender != 'F' and gender != 'M':
        print('Value not accepted. Please try again!')
print('END!')

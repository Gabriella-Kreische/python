'''
time = float(input('How old is your car? '))
if time <= 3:
    print('New car')
else:
    print('Old car')
print('--END--')

name = input('What is your name? ')
if name == 'Gabriella':
    print('You have a beautiful name!')
print('Good morning, {}!'.format(name))

n1 = float(input('Type the first exam result: '))
n2 = float(input('Type the second exam result: '))
n = (n1 + n2)/2
print('Your score is {:.1f}'.format(n))
if n >= 6.0:
    print('Your score is great! Congratulations!')
else:
    print('Your score is bad, study more!')
'''

n1 = float(input('Type the first exam result: '))
n2 = float(input('Type the second exam result: '))
n = (n1 + n2)/2
print('Your score is {:.1f}'.format(n))
print('CONGRATULATIONS!' if n >= 6.0 else 'STUDY MORE!')


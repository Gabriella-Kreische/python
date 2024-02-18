import random

s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')
s4 = input('Forth student: ')
result = [s1, s2, s3, s4]
random.shuffle(result)
print('The presentation order will be: {}'.format(result))

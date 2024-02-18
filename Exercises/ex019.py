import random

s1 = input('1\u00b0 student: ')
s2 = input('2\u00b0 student: ')
s3 = input('3\u00b0 student: ')
s4 = input('4\u00b0 student: ')
l = [s1, s2, s3, s4]
print('The chosen student is: {}'.format(random.choice(l)))

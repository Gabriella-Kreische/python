'''
n2 = int(input('Second number: '))
n3 = int(input('Third number: '))
n4 = int(input('Fourth number: '))
n5 = int(input('Fifth number: '))
n6 = int(input('Sixth number: '))

'''

n = []
s = 0
for c in range(0, 6):
    n1 = int(input('Type a number: '))
    n += [n1]
    if n1 % 2 == 0:
        s += n1
print(n)
print('The sum of all even values entered is equal to {}!'.format(s))

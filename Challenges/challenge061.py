print('{:-^40}'.format(' Arithmetic Progression (AP)  '))
n1 = int(input('Type first value: '))
constant = int(input('Type constant value: '))

arrow = '\u2192 '
max = (constant*10)+n1
c = 1
while n1 < max:
    print('{} '.format(n1), end=arrow)
    n1 += constant
print('FINISHED!!')

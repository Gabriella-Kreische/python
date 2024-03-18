print('{:-^40}'.format(' Arithmetic Progression (AP)  '))
n1 = int(input('Type first value: '))
constant = int(input('Type constant value: '))

arrow = '\u2192 '
maximum = 10
cont = 1
while cont <= maximum:
    print('{} '.format(n1), end=arrow)
    n1 += constant
    cont += 1
print('FINISHED!!')

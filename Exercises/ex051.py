print('{:-^40}'.format(' Arithmetic Progression (AP)  '))
n1 = int(input('Type first value: '))
constant = int(input('Type constant value: '))

arrow = '\u2192 '
#pa = [s]
#pa += [s] Add items to a list
for c in range(n1, (constant*10)+n1, constant):
    print('{} '.format(c), end=arrow)
print('FINISHED!!')

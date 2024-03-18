print('{:-^40}'.format(' Arithmetic Progression (AP)  '))

n1 = int(input('Type first value: '))
constant = int(input('Type constant value: '))
arrow = '\u2192 '
plus = 10
total = 0
cont = 1
while plus != 0:
    total = total + plus
    while cont <= total:
        print('{} '.format(n1), end=arrow)
        n1 += constant
        cont += 1
    print('FINISHED!!')
    plus = int(input('How many more terms would you like to see? '))
print('It was shown in total {} terms!'.format(total))

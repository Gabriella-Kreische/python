print('{:-^40}'.format(' Arithmetic Progression (AP)  '))

n1 = int(input('Type first value: '))
constant = int(input('Type constant value: '))
items = 10
arrow = '\u2192 '

#c = 1

while items != 0:
    max = (constant * items) + n1
    while n1 < max:
        print('{} '.format(n1), end=arrow)
        n1 += constant
    print('FINISHED!!')
    items = int(input('How many more terms would you like to see? '))


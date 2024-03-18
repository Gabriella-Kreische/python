
decision = 0

while decision != 5:
    n1 = []
    total = 0
    i = 0
    for c in range(1, 3):
        n1 += [int(input('Please type {}\u00B0 number: '.format(c)))]
    decision = int(input('''Menu Page. Please press:
[ 1 ] Sum 
[ 2 ] Multiply 
[ 3 ] Find higher number 
[ 4 ] Enter new number 
[ 5 ] Leave 
Your choice: '''))
    if decision == 1:
        while i < len(n1):
            total += n1[i]
            i += 1
        print('The sum of {} is equal to {}.'.format(n1, total))
    elif decision == 2:
        mul = 1
        for x in n1:
            mul = mul * x
        print('The multiplication of {} is equal to {}.'.format(n1, mul))
    elif decision == 3:
        print('The higher number between {} is {}!'.format(n1, max(n1)))
    elif decision > 5:
        print('Number invalid. Please try again.')

print('END!')

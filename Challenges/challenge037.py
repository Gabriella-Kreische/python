num = int(input('Type a number: '))
choise = int(input('Press 1 if you want to convert this number to binary, 2 if you want to convert this number to octagonal or 3 if you want to convert this number to hexadecimal '))
if choise == 1:
    num_converted = bin(num)
    choise = 'binary'
    print(choise)
elif choise == 2:
    num_converted = oct(num)
    choise = 'octagonal'
    print(choise)
elif choise == 3:
    num_converted = hex(num)
    choise = 'hexadecimal'
    print(choise)
else:
    print('Number invalid. Please try again!')

print('The number {} converted to {} is equal to {}'.format(num, choise, num_converted))

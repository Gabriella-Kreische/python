
c = 1
while c < 10:
    print(c, end=' ')
    c += 1

a = 1
while a != 'n':
    n = int(input('Type a number: '))
    a = input('Would you like to continue? (y/n) ')
print('END!')

even = odd = 0
while n != 0:
    n = int(input('Type a number: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print('You typed {} odd numbers and {} even numbers!'.format(odd, even))

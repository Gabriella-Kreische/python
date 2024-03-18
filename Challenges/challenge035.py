n1 = int(input('Type the length of the first line: '))
n2 = int(input('Type the length of the second line: '))
n3 = int(input('Type the length of the third line: '))

if n1 > n2 and n1 > n3:
    print('{} is the higher number'.format(n1))
    h = n1
elif n2 > n1 and n2 > n3:
    print('{} is the higher number'.format(n2))
    h = n2
else:
    print('{} is the higher number'.format(n3))
    h = n3

if h == n1 and (n2 + n3) > n1:
    print('You can make a triangle!')
elif h == n2 and (n1 + n3) > n2:
    print('You can make a triangle!')
elif h == n3 and (n1 + n2) > n3:
    print('You can make a triangle!')
else:
    print('You can not make a triangle!')




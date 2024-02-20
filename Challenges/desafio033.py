n1 = float(input('Type first number: '))
n2 = float(input('Type second number: '))
n3 = float(input('Type third number: '))

if n1 > n2 and n1 > n3:
    print('{} is the higher number'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} is the higher number'.format(n2))
else:
    print('{} is the higher number'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} is the smaller number'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} is the smaller number'.format(n2))
else:
    print('{} is the smaller number'.format(n3))

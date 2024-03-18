n1 = float(input('First line: '))
n2 = float(input('Second line: '))
n3 = float(input('Third line: '))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    if n1 == n2 == n3:
        triangle = 'EQUILATERAL'
    elif n1 == n2 and n1 != n3 or n2 == n3 and n2 != n1:
        triangle = 'ISOSCELES'
    else:
        triangle = 'SCALENE'
    print('You CAN form a triangle {}'.format(triangle))
else:
    print('You CAN NOT form a triangle')

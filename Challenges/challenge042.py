n1 = float(input('Type the length of the 1o line: '))
n2 = float(input('Type the length of the 2o line: '))
n3 = float(input('Type the length of the 3o line: '))

if n2 + n3 > n1 and n1 + n2 > n3 and n1 + n3 > n2:
    if n1 == n2 == n3:
        print('You can have a triangle EQUILATERAL!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('You can have a triangle ISOSCELES!')
    else:
        print('You can have a triangle SCALENE!')
else:
    print('You can not have a triangle!')

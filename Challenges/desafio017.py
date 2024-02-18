import math
s1 = float(input('Type the length of the first side of the hypotenuse: '))
s2 = float(input('Type the length of the second side of the hypotenuse: '))
h = math.hypot(s1, s2)
print('The hypotenuse of a right angled triangle is {:.2f}.'.format(h))

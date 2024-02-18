'''
import math

num1 = float(input('Length of first side of the right-angle triangle: '))
num2 = float(input('Length of the second side of the right-angle triangle: '))
h = math.hypot(num1, num2)
print('The hypotenuse is {:.2f}!'.format(h))
'''

from math import hypot
num1 = float(input('Length of first side of the right-angle triangle: '))
num2 = float(input('Length of the second side of the right-angle triangle: '))
h = hypot(num1, num2)
print('The hypotenuse is {:.2f}!'.format(h))

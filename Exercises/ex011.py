l = float(input('Total wall length: '))
h = float(input('Total wall height: '))
a = l * h
p = a / 2
print('Your wall has dimension of {}x{} meters and your area is {:.2f}m\u00b2'.format(l, h, a))
print('To paint this wall, you are going to need {:.2f} liters of paint.'.format(p))

l = int(input('Enter the total length in meters of the are you need to paint: '))
h = int(input('Enter the total height in meters of the are you need to paint: '))
a = l * h
p = a / 2
print('You will need to buy {:.1f} liters of paint.'.format(p))

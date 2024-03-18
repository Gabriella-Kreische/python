# degree symbol: \u00B0
n = []
s = 0
for c in range(1, 7):
    n1 = int(input('Type the {}\u00B0 value: '.format(c)))
    n += [n1]
    if n1 % 2 == 0:
        s += n1
print('The numbers entered are: {}'.format(n))
print('The sum of all even values entered is equal to {}!'.format(s))

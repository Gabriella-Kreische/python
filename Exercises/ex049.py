import colour

n1 = int(input('Type a number to see its multiplication table: '))
print('{}{:=^40}{}'.format(colour.red, ' MULTIPLICATION TABLE ', colour.clear))

i = 0
f = 10
r = 0
for c in range(i, f+1):
    r = n1 * c
    print('{} x {:2} = {}'.format(n1, c, r))
print('End')

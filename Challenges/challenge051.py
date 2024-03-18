print('{:-^40}'.format(' Arithmetic Progression (AP)  '))
n1 = int(input('Type first value: '))
n2 = int(input('Type constant value: '))

s = n1
pa = [s]
for c in range(1, 10):
    s += n2
    pa += [s]
print(pa)

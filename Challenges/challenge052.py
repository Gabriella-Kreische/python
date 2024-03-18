print('{:-^40}'.format(' PRIME NUMBER tester'))
n1 = int(input('Type a number: '))
s = []

if n1 > 1:
    for c in range(2, n1+1):
        if n1 % c == 0:
            s += [n1]
if len(s) != 1:
    print('{} is NOT a PRIME number'.format(n1))
else:
    print('{} is a PRIME number'.format(n1))

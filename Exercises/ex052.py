import colour

print('{:-^40}'.format(' PRIME NUMBER TESTER'))
n1 = int(input('Type a number: '))
s = []

if n1 > 1:
    for c in range(2, n1+1):
        if n1 % c == 0:
            s += [c]
print('The numbers greater than 1 until {} that can divide {} are: {}{}{}'.format(n1, n1, colour.yellow, s, colour.clear))
if len(s) != 1:
    print('{} is NOT a PRIME number'.format(n1))
else:
    print('{} is a PRIME number'.format(n1))

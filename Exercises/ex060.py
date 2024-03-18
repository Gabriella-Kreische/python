print('{:=^40}'.format(' FACTORIAL CALCULATOR '))
n1 = int(input('Type a number: '))
c = 1
factorial = 1
x = n1
print('Calculating {}! = '.format(n1), end='')
#while c <= n1:


while x > 0:
    factorial *= c
    c += 1
    print('{} '.format(x), end='')
    print('x ' if x > 1 else '= ', end='')
    x -= 1
print('{}'.format(factorial))

factorial = 1
c = n1
print('Calculating {}! = '.format(n1), end='')
for x in range(n1, 0, -1):
    factorial = factorial * x
    x += 1
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    c -= 1
print('{}'.format(factorial))

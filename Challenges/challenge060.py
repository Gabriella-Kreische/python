print('{:=^40}'.format(' FACTORIAL CALCULATOR '))
n1 = int(input('Type a number: '))
c = 1
factorial = 1
while c <= n1:
    factorial = factorial * c
    c += 1
print('The factorial of {} is {}!'.format(n1, factorial))

factorial = 1
for x in range(n1, 0, -1):
    factorial = factorial * x
    x += 1
print('The factorial of {} is {}!'.format(n1, factorial))

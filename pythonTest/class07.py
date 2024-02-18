'''
print(5 + 2)
print(5 - 3)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)
print(10 % 2)
5**3
'''
n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
sum = n1 + n2
div = n1 / n2
divi = n1 // n2
mul = n1 * n2
exp = n1 ** n2
print('The sum is equal to {} \nand the division is equal to {:.3f}! '.format(sum, div), end='>>>>')
print('The module is {} and the multiplication is equal to {}!'.format(divi, mul))

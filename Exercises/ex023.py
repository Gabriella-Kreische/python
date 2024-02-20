number = int(input('Type a number: '))
u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
th = number // 1000 % 10
print('Analyzing the number {}'.format(number))
print('Unit: {}'.format(u))
print('Ten: {}'.format(t))
print('Hundred: {}'.format(h))
print('Thousand: {}'.format(th))

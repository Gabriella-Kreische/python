import math

num = float(input('Type a number: '))
#result = math.floor(num)
#result = int(num)
result = math.trunc(num)
print('The value entered was {} and its integer part is {}!'.format(num, result))

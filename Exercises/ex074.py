import random
draw = []

for n in range(0, 5):
    number = [random.randint(0, 10)]
    draw += number
draw = tuple(draw)
print(f'The numbers generated are {draw}')
'''
smaller = ''
bigger = ''
for pos in range(0, len(draw)):
    if smaller == '':
        smaller = draw[pos]
        bigger = draw[pos]
    elif draw[pos] <= smaller:
        smaller = draw[pos]
    elif draw[pos] >= bigger:
        bigger = draw[pos]
print(f'The smaller value is {smaller}')
print(f'The biggest value is {bigger}')
'''

print(f'The highest number draw was {max(draw)}')
print(f'The smallest number draw was {min(draw)}')

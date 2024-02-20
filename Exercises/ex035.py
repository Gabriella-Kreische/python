import colour

print('{}{}{}'.format(colour.blue, '-=-'*15, colour.clear))
print('Analysing a triangle')
print('{}{}{}'.format(colour.yellow, '-=-'*15, colour.clear))
l1 = float(input('First line: '))
l2 = float(input('Second line: '))
l3 = float(input('Third line: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('You can make a triangle!')
else:
    print('You can NOT make a triangle!')

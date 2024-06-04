num = (int(input('Type a number: ')),
    int(input('Type another number: ')),
    int(input('Type another number: ')),
    int(input('Type another number: ')))

print(f'You have entered the numbers: {num}')
print(f'The value 9 appeared {num.count(9)} times.')
if 3 in num:
    print(f'Number 3 was the {num.index(3)+1}\u00b0 value entered.')
else:
    print(f'Number 3 was not entered.')
print('The even number(s) entered are: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



'''
cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('Finished!')

n = cont = 0
while cont < 3:
    n = int(input('Type a number: '))
    cont += 1
'''


n = 0
s = 0
while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    s += n
#print('The sum is {}'.format(s))
print(f'The sum is {s}') #Python 3.6+

name = 'John'
age = 33
print(f'{name} has {age} years old')
wage = 987.35
print(f'{name:-^10} has {age} years old and earns ${wage:.2f} per week')

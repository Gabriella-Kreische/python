print('{:-^50}'.format('MULTIPLICATION TABLE'))
while True:
    print('-'*50)
    n = int(input('Type a number to see its Multiplication Table: '))
    print('-'*50)
    if n < 0:
        break
    '''
    while y < 10:
        y += 1
        print(f'{n} x {y} = {n*y}')   
    if y >= 10:
        n = y = 0         
    '''
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')


print('Multiplication Table process ended. Come back always!')

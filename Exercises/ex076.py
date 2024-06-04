print('='*40)
#print('{:^60}'.format('PRICE LIST'))
print(f'{"PRICE LIST":^40}')
print('='*40)
prod_price = ('Pen', 1.75,
              'Eraser', 2.0,
              'Notebook', 15.90,
              'Case', 25.00,
              'Bevel', 4.20,
              'Compass', 9.99,
              'Backpack', 120.32,
              'Pen', 22.30,
              'Book', 34.90)
for pos in range(0, len(prod_price)):
    if pos % 2 == 0:
        print(f'{prod_price[pos]:.<30}', end='')
    else:
        print(f'${prod_price[pos]:>7.2f}')
print('-'*40)

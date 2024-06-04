from tabulate import tabulate

print('='*60)
print('{:^60}'.format('PRICE LIST'))
print('='*60)

prod_price = (('PRICE LIST'),('Pen', 1.75), ('Eraser', 2.0), ('Notebook', 15.90), ('case', 25.00), ('bevel', 4.20), ('compass', 9.99), ('backpack', 120.32), ('pen', 22.30), ('book', 34.90))
#data_header = "LIST OF PRICES"
#print(data_header)
headers = 'PRICE LIST'
print(tabulate(prod_price, headers, floatfmt=".2f", numalign="left",))

print('-'*60)

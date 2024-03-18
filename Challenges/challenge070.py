print('{:-^50}'.format(' ALL FOR $1.99 STORE '))
prod_name = []
prod_price = []
expensive_prod = []
while True:
    name = input('Product name: ')
    prod_name += [name]
    price = float(input('Product price: $ '))
    while price < 0:
        price = float(input('Product price: $ '))
    prod_price += [price]
    if price > 1000:
        expensive_prod += [price]
    again = input('Would you like to continue? [Y/N] ')
    while again not in 'YyNn':
        again = input('Would you like to continue? [Y/N] ')
    if again in 'Nn':
        break
print(prod_name)
print(prod_price)
prod_sum = sum(prod_price)
print('{:-^50}'.format(' CHECK OUT '))
print(f'The total price is {prod_sum}')
print(f'{len(expensive_prod)} products cost more than $1,000.00 dollars.')
cheapest_prod_price = 0
cheapest_prod_name = ''
for a in range(0, len(prod_price)):
    if cheapest_prod_name == '':
        cheapest_prod_name = prod_name[a]
        cheapest_prod_price = prod_price[a]
    elif prod_price[a] < cheapest_prod_price:
        cheapest_prod_price = prod_price[a]
        cheapest_prod_name = prod_name[a]
print(f'The name of the cheapest product is {cheapest_prod_name} and it has cost ${cheapest_prod_price:.2f} dollars.')

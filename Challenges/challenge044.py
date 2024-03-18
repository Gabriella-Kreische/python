from Exercises import colour

n1 = float(input('what is the price of the product? $ '))
n2 = int(input('Press 1 to pay in cash; 2 to pay by debit card; 3 to pay by credit card (2 months); 4 to pay by credit card (3 months): '))
price = ''

if n2 == 1:
    price = n1 - (n1 * 0.1)
elif n2 == 2:
    price = n1 - (n1 * 0.05)
elif n2 == 3:
    price = n1
elif n2 == 4:
    price = n1 + (n1 * 0.2)
else:
    print('Number invalid! Please try again!')

if price != '':
    print('Total price {}${:.2f}{}'.format(colour.yellow, price, colour.clear))

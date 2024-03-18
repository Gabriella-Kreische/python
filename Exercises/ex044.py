from Exercises import colour
print('{:=^40}'.format(' GUANABARA STORE '))
n1 = float(input('Price of the products: $ '))
n2 = int(input('''PAYMENT OPTIONS:
[ 1 ] Cash 
[ 2 ] Debit card
[ 3 ] 2x credit card 
[ 4 ] 3x or more by credit card
Your Option: '''))
price = ''

if n2 == 1:
    price = n1 - (n1 * 0.1)
elif n2 == 2:
    price = n1 - (n1 * 0.05)
elif n2 == 3:
    price = n1
    split = price / 2
    print('Your bill will be split in 2 instalments of {}${:.2f}{}'.format(colour.yellow, split, colour.clear))
elif n2 == 4:
    price = n1 + (n1 * 0.2)
    total_split = int(input('Number of instalments: '))
    split = price / total_split
    print('Your bill will be split in {} instalments of {}${:.2f}{}'.format(total_split, colour.yellow, split, colour.clear))
else:
    print('{}Number invalid! Please try again!{}'.format(colour.yellow, colour.clear))

if price != '':
    print('Your shopping of ${:.2f} is going to cost a Total price of {}${:.2f}{}'.format(n1, colour.yellow, price, colour.clear))

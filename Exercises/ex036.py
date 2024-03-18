import colour
house_price = float(input('What is the price of the house you would like to buy? $ '))
salary = float(input('What is your annual salary? $ '))
year = int(input('In how many years would you like to pay the house? '))
interest = (house_price * 0.1)/12
monthly_bill = (house_price/(year * 12)) + interest

print('Future Monthly bill: {}${:.2f}{}'.format(colour.red, monthly_bill, colour.clear))
maximum = (salary/12) * 0.3
print('Your maximum affordable monthly bill can be until ${:.2f}.'.format(maximum))
if monthly_bill <= maximum:
    print('Your loan can be approved!')
else:
    print('Your monthly bill will exceed 30% of you income so your loan is denied!')


d = int(input('How many days the car was used? '))
km = float(input('How many miles the car travelled? '))
price = (d * 60) + (km * 0.15)
print('The total rental price is NZ${:.2f}!'.format(price))

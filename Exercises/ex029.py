speed = float(input('What is the current car speed (km/h)? '))
if speed > 80:
    print('You were fined! The limite is 80km/h!')
    print('You need to pay ${} dollars.'.format((speed - 80) * 7))
print('Have a good day! Drive safe!')

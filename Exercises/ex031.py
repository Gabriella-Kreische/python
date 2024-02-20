import colour

distance = float(input('What is the distance of your travel? '))
print('You are about to start your travel of {}{} km.{}'.format(colour.green, distance,colour.clear))
if distance <= 200:
    ticket = distance * 0.5
else:
    ticket = distance * 0.45
print('The price is {}${:.2f}{}'.format(colour.red, ticket, colour.clear))

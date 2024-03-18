travel = float(input('What is your travel distance? '))
if travel <= 200:
    ticket = travel * 0.5
else:
    ticket = travel * 0.45

print('The ticket will cost: ${:.2f} dollars'.format(ticket))
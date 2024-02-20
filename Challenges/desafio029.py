v = float(input('What is the speed of the car? (km/h) '))
if v > 80:
    print('You were fined! It will cost you ${:.1f} dollars'.format((v-80)*7))

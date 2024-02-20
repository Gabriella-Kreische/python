year = int(input('Type a year: '))

if year % 4 == 0:
    if year % 100 != 0:
        print('{} is a leap year! Congratulations you have 1 day more!'.format(year))
    elif year % 400 == 0:
        print('{} is a leap year! Congratulations you have 1 day more!'.format(year))
    else:
        print('{} is not a leap year!'.format(year))
else:
    print('{} is not a leap year!'.format(year))
    
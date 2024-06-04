while True:
    written_number = ('zero', 'one', 'two',
                      'three', 'four', 'five',
                      'six', 'seven', 'eight',
                      'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen',
                      'fifteen', 'sixteen', 'seventeen',
                      'eighteen', 'nineteen', 'twenty')
    while True:
        number = int(input('Type a number between 0 and 20: '))
        if 0 <= number <= 20:
            break
        print('Please try again.', end=' ')
    print(f'You have typed {written_number[number]}')

    proceed = input('Do you wish to continue? Y/N ')
    if proceed in 'Nn':
        break

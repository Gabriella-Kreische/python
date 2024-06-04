written_number = (
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
number = int(input('Type a number between 0 and 20: '))
if number > 20 or number < 0:
    number = int(input('Please try again. Type a number between 0 and 20: '))
print(f'You have typed {written_number[number]}!!')

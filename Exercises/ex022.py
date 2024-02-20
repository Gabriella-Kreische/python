import colour

name = input('What is your name? ').strip()
name_upper = name.upper()
name_lower = name.lower()
print('Your name in uppercase is {}{}{}'.format(colour.blue, name_upper, colour.clear))
print('Your name in lowercase is {}'.format(name_lower))
print('Your name has {}{}{} letters'.format(colour.red,len(name) - name.count(' '), colour.clear))
name_split = name.split()
print('Your first name is {} and has {} letters'.format(name_split[0],len(name_split[0])))

name = input('What is your name? ').strip()
name = name.split()
first_name = name[0]
last_name = name[len(name) - 1]
print('Your first name is: {}'.format(first_name))
print('Your last name is: {}'.format(last_name))

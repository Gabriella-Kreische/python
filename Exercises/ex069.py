print('{:-^40}'.format(' USER REGISTER '))
t18 = tman = tf20 = 0
while True:
    age = int(input('Age: '))
    while age < 0:
        age = int(input('Age: '))
    sex = input('Sex [F/M]: ').strip()
    while sex not in 'MmFf':
        sex = input('Sex [F/M]: ')
    if age >= 18:
        t18 += 1
    if sex in 'Mm':
        tman += 1
    if sex in 'Ff' and age >= 20:
        tf20 += 1
    again = input('Would ou like to continue [Y/N]? ')
    while again not in 'YyNn':
        again = input('Would ou like to continue [Y/N]? ')
    if again in 'Nn':
        print('{:-^40}'.format(' End of the register!! '))
        break
print(f'{t18} user(s) registered have more than 18 years old.')
print(f'{tman} user(s) of the male sex were successfully registered.')
print(f'{tf20} young women with less than 20 years old were successfully registered.')

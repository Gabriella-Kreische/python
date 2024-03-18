print('{:-^40}'.format(' USER REGISTER '))
age_list = []
sex_list = []
cont = man = young_woman = 0
while True:
    age = int(input('Age: '))
    while age < 0:
        age = int(input('Age: '))
    age_list += [age]
    sex = input('Sex [F/M]: ')
    while sex not in 'MmFf':
        sex = input('Sex [F/M]: ')
    sex_list += [sex]
    again = input('Would ou like to continue [Y/N]? ')
    while again not in 'YyNn':
        again = input('Would ou like to continue [Y/N]? ')
    if again in 'Nn':
        print('{:-^40}'.format(' End of the register!! '))
        break

for a in range(0, len(age_list)):
    if age_list[a] > 18:
        cont += 1
print(f'{cont} user(s) registered have more than 18 years old.')
for a in range(0, len(sex_list)):
    if sex_list[a] in 'Mm':
        man += 1
print(f'{man} user(s) of the male sex were successfully registered.')
for a in range(0, len(sex_list)):
    if sex_list[a] in 'Ff' and age_list[a] < 20:
        young_woman += 1
print(f'{young_woman} young women with less than 20 years old were successfully registered.')

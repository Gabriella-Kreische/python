name = []
age = []
sex = []
older_age = 0
older_name = 0
young_woman = 0
for c in range(1, 5):
    print('----- {}\u00B0 PERSON -----'.format(c))
    name += [input('What is your name: ')]
    age += [int(input('How old are you? '))]
    sex += [int(input('How do you identify yourself? Press: \n[ 1 ] for Male\n[ 2 ] for Female \n[ 3 ] for Non-binary)\nYour choise: '))]
#print(name)
#print(age)
#print(sex)
age_avg = sum(age)/len(age)
print('The average age entered is {:1f} years old'.format(age_avg))

for c in range(0, 4):
    if sex[c] == 1:
        if older_age == 0:
            older_age = age[c]
            older_name = name[c]
        elif age[c] > older_age:
            older_age = age[c]
            older_name = name[c]
print('The older male have {} years old and is called {}.'.format(older_age, older_name))

for c in range(0, 4):
    if sex[c] == 2:
        if age[c] < 20:
            young_woman += 1
print('There are {} females with less than 20 years old.'.format(young_woman))


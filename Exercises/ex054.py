from datetime import date

this_year = date.today().year
print('{:+^40}'.format(' MAJORITY CALCULATOR '))
m = []
i = []
majority = 21
for person in range(1, 8):
    born_year = int(input('What year {}\u00B0 person was born? '.format(person)))
    if (this_year - born_year) > majority:
        m += [born_year]
    else:
        i += [born_year]

print('{} person(s) who were born in {} have reach majority!'.format(len(m), m))

print('{} person(s) who were born in {} have NOT reach majority yet!'.format(len(i), i))

import datetime
import colour

print('{}{}{}'.format(colour.yellow, '-'*50, colour.clear))
print('NATIONAL CONFEDERATION OF SWIMMING')
print('{}{}{}'.format(colour.yellow, '-'*50, colour.clear))

date_entry = input('Please type your date of bith in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date_birth = datetime.date(year, month, day)
print(date_birth)

today = datetime.date.today()
print(today)

if date_birth.month > today.month or (date_birth.month == today.month and date_birth.day > today.day):
    age = today.year - date_birth.year - 1
else:
    age = today.year - date_birth.year
print(age)

if age <= 9:
    print('MIRIM')
elif age <= 14:
    print('INFANTIL')
elif age <= 19:
    print('JUNIOR')
elif age <= 20:
    print('SENIOR')
else:
    print('MASTER')


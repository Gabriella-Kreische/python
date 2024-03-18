import datetime

date_entry = input('Type your date of birth in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date_birth = datetime.date(year, month, day)
print(date_birth)
today = datetime.date.today()
print(today)
if date_birth.month <= today.month and date_birth.day < today.day:
    age = today.year - date_birth.year
else:
    age = today.year - date_birth.year - 1

print('You have {} years old.'.format(age))
if age > 18:
    print('It has past {} years since your army enlistment year!'.format(age-18))
elif age == 18:
    print('You can do your army enlistment this year!')
else:
    print('You still have {} years until you can do your army enlistment.'.format(18 - age))

salary = float(input('Type your annual salary: '))
if salary >= 48000:
    new_salary = salary + (salary * 0.10)
    print('Your new salary is ${:.2f}'.format(new_salary))
else:
    new_salary = salary + (salary * 0.15)
    print('Your new salary is ${:.2f}'.format(new_salary))

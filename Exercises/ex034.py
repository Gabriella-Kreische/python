salary = float(input('What is the wage of the employee? $'))
if salary <= 48000:
    new_salary = salary + (salary * 0.15)
else:
    new_salary = salary + (salary * 0.10)
print('Who used to earn {:.2f}, will pass to earn {:.2f}'.format(salary, new_salary))

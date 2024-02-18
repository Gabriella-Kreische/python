salary = float(input('What is the salary of the employee? NZ$ '))
promotion = salary + (salary * 0.15)
print('An employee that has a salary of NZ${:,.2f}, with 15% of raise will receive NZ${:,.2f}!'.format(salary, promotion))

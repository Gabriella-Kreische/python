print('{:+^40}'.format(' NUMBERS CALCULATOR '))
print('Type a number or write 999 to leave. ')
total = 0
stop = 999
list_n = []
n = 0
i = 1
while n != stop:
    n = int(input('{}\u00B0 number: '.format(i)))
    i += 1
    if n != 999:
        list_n += [n]
        total += 1
print(list_n)
print(type(list_n))
print('{} numbers were entered.'.format(total))
sum_n = sum(list_n)
print('The sum of the numbers entered is equal to {}!'.format(sum_n))

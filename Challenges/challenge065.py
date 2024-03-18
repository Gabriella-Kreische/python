print('{:=^40}'.format(' NUMBERS CALCULATOR '))

higher = ''
smaller = ''
cont = 'Y'
list_n = []
while cont == 'Y':
    n = int(input('Type a number: '))
    list_n += [n]
    cont = input('Would you like to continue? Y/N ')
#print(list_n)
#print(sum(list_n))
avg = sum(list_n)/len(list_n)
print('The average between the numbers entered is equal to {:.2f}!'.format(avg))
for i in range(0, len(list_n)):
    if higher == '' or smaller == '':
        higher = list_n[i]
        smaller = list_n[i]
    elif list_n[i] > higher:
        higher = list_n[i]
    elif list_n[i] < smaller:
        smaller = list_n[i]
print('The higher number entered is {}!'.format(higher))
print('The smaller number entered is {}!'.format(smaller))

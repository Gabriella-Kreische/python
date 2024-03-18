import colour

print('{}{}{}'.format(colour.red,'-=-'*15, colour.clear))
print('GRADE CALCULATOR')
print('{}{}{}'.format(colour.red,'-=-'*15, colour.clear))

n1 = float(input('First exam result: '))
n2 = float(input('Second exam result: '))
average = (n1 + n2)/2
if average < 5:
    print('FAILED')
elif 6.9 >= average >= 5:
    print('STUDENT CAN REDO ONE EXAM')
else:
    print('APPROVED')

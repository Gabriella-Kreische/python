import colour

print('{}{}{}'.format(colour.red,'-=-'*15, colour.clear))
print('GRADE CALCULATOR')
print('{}{}{}'.format(colour.red,'-=-'*15, colour.clear))

n1 = float(input('First exam result: '))
n2 = float(input('Second exam result: '))
average = (n1 + n2)/2
if average < 5:
    print('FAILED')
elif average >=5 and average <= 6.9:
    print('STUDENT CAN REDO AN EXAM')
else:
    print('APPROVED')

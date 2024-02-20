import colour

n1 = float(input('First value: '))
n2 = float(input('Second value: '))
n3 = float(input('Third value: '))
'''
#Analysing who is the highest
if n1 > n2 and n1 > n3:
    print('{} is the highest value!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} is the highest value!'.format(n2))
else:
    print('{} is the highest value!'.format(n3))

#Analysing who is the smaller
if n1 < n2 and n1 < n3:
    print('{} is the smaller value'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} is the smaller value'.format(n2))
else:
    print('{} is the smaller value'.format(n3))
'''
#Analysing who is the highest
higher = n1
if n2 > n1 and n2 > n3:
    higher = n2
else:
    higher = n3
print('{}{}{} is the highest value!'.format(colour.yellow, higher, colour.clear))

#Analysing who is the smallest
smaller = n1
if n2 < n1 and n2 < n3:
    smaller = n2
else:
    smaller = n3
print('{}{}{} is the smaller value'.format(colour.red ,smaller, colour.clear))

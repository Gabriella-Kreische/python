print('{:=^60}'.format(' TUPLES '))
print('variable = ()  or variable = x, x, x')
print('{:=^60}'.format(' YOU CAN NOT CHANGE '))
lunch = ('hamburger', 'beer', 'pizza', 'pudding')
for food in lunch:
    print(f'I will eat {food}')
print(lunch[1:])
print(lunch[-1])
print(lunch[2:3])
print(lunch[2])
print(lunch)
for count in range(0, len(lunch)):
    print(f'I will eat {lunch[count]} in position {count}')

for pos, food in enumerate(lunch):
    print(f'I will eat {food} in position {pos}')
print('I have eaten a lot!!')

print(sorted(lunch))


a = (2, 5, 4)
b = (8, 1, 6, 4)
c = b + a
print(c)
print(len(c))
print(c.count(4))
print(c.index(8)) #position of number 8 in tuple
print(c.index(4, 4))
person = ('John', 99.98, 'M')
print(person)
del person
print(person)

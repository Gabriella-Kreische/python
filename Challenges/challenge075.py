
value_list = []
even_list = []
for n in range(0, 4):
    value = [int(input('Type a number: '))]
    value_list += value

for e in range(0, 4):
    if value_list[e] % 2 == 0:
        even_list += [value_list[e]]

value_tuple = tuple(value_list)
even_tuple = tuple(even_list)
print(value_list)
print(value_tuple)
print(even_list)
print(even_tuple)
print(f'You entered the numbers: {value_tuple}')
print(f'The number 9 appears {value_tuple.count(9)} time(s).')
if value_tuple.count(3) != 0:
    print(f'Number 3 was the {value_tuple.index(3)+1}\u00b0 value entered.')
else:
    print(f'Number 3 was not entered.')
print(f'The even number(s) entered are {even_tuple}')

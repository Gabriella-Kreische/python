number = int(input('Type a number: '))
split_str = list(str(number))
print(split_str)
split_int = list(map(int, str(number)))
print(split_int)
length = len(split_int)
print(length)
if length == 1:
    unit = split_int[0]
    print('Unit:', unit)
elif length == 2:
    unit = split_int[1]
    print('Unit:', unit)
    ten = split_int[0]
    print('Ten:', ten)
elif length == 3:
    unit = split_int[2]
    print('Unit:', unit)
    ten = split_int[1]
    print('Ten:', ten)
    hundred = split_int[0]
    print('Hundred:', hundred)
else:
    unit = split_int[3]
    print('Unit:', unit)
    ten = split_int[2]
    print('Ten:', ten)
    hundred = split_int[1]
    print('Hundred:', hundred)
    thousand = split_int[0]
    print('Thousand:', thousand)



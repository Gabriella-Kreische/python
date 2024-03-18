import colour
s = 0
for c in range(1, 500+1, 2):
    #print(c)
    if (c % 3) == 0:
        s += c #s = s + c
        #print(s)
print('The sum of all odd numbers multiples of three between 1 and 500 is {}{}{}!'.format(colour.yellow, s, colour.clear))

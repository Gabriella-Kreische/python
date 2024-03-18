n = s = cont = 0
while True:
    n = int(input('Type a number (or type 999 to exit): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'You have entered {cont} values and their sum is {s}!')

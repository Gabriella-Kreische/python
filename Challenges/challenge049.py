n1 = int(input('Type a number to see its multiplication table: '))
print('{:=^40}'.format(' MULTIPLICATION TABLE '))
i = 0
f = 10
r = 0
m = 0
for c in range(i, f+1):
    r = n1 * m
    print('{} x {} = {}'.format(n1, m, r))
    m += 1
print('End')

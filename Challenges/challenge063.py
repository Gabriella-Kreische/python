print('{:=^40}'.format(' FIBONACCI SEQUENCE '))
n = int(input('Type e number: '))
f1 = 0
print(f1, end=' ')
f2 = 1
print(f2, end=' ')
f3 = 0
i = 0
while i < n:
    f3 = f2 + f1
    print(f3, end=' ')
    f1 = f2
    f2 = f3
    i += 1


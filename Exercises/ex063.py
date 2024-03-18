print('{:=^42}'.format(' FIBONACCI SEQUENCE '))
n = int(input('How many numbers would you like to see: '))
print('='*42)
f1 = 0
f2 = 1
print('{} - {}'.format(f1, f2), end=' - ')

f3 = 0
i = 0
while i < n:
    f3 = f2 + f1
    print(f3, end=' - ')
    f1 = f2
    f2 = f3
    i += 1
print('END!')

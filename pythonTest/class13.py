print('{:=^55}'.format(' Loops '))

c = 0
for c in range(0, 10):
    #c = c+1
    print(c, end=' ')
print('End')

i = int(input('Start number: '))
f = int(input('Final number: '))
j = int(input('Jump number: '))
for c in range(i, f+1, j):
    print(c, end=' ')
print('End')

for c in range(0, 10):
    c = c+1
    print(c, end=' ')
print('End')

for c in range(10, 0, -1):
    #c = c+1
    print(c, end=' ')
print('End')

for c in range(0, 10, 2):
    print(c, end=' ' )
print('End')
print('-'*5)



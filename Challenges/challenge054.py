
m = []
i = []
majority = 2003
for c in range(0, 7):
    n1 = int(input('What year were you born? '))
    if n1 < majority:
        m += [n1]
    else:
        i += [n1]
print(n1)

print('Who were born in {} have reach majority!'.format(m))

print('Who were born in {} have NOT reach majority yet!'.format(i))

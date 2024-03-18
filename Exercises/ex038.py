n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
if n2 == n1:
    print('{} and {} are the same number!'.format(n1, n2))
elif n1 > n2:
    print('{} is the biggest number!\n{} is the smaller value!'.format(n1, n2))
else:
    print('{} is bigger!\n{} is the smaller value!'.format(n2, n1))

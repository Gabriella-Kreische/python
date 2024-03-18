heavier = float(0)
lighter = float(0)
for c in range(0, 5):
    w = float(input('What is your weight in Kg? '))
    if heavier == 0 and lighter == 0:
        heavier = w
        lighter = w
    elif w > heavier:
        heavier = w
    elif w < lighter:
        lighter = w
print('The heavier weight is {}!'.format(heavier))
print('The lighter weight is {}!'.format(lighter))

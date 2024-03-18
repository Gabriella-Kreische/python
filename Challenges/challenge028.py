import random
pc_num = [0, 1, 2, 3, 4, 5]
pc_num = random.choice(pc_num)
num = int(input('Try to guess what number the computer thought between 0 and 5: '))
if pc_num == num:
    print('You got it! The number is {}'.format(pc_num))
else:
    print('No, the number was {}!'.format(pc_num))

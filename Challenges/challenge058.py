import random
pc_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc_num = random.choice(pc_num)
num = ''
attempt = 0
while pc_num != num:
    num = int(input('Try to guess what number the computer thought between 0 and 10: '))
    attempt += 1
    if pc_num == num:
        print('You got it! The number is {}! You have try {} times until the correct answer'.format(pc_num, attempt))
    else:
        print('No, it is not {}, please try again!'.format(num))

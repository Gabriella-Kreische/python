import random
pc_num = random.randint(0, 10)
num = ''
attempt = 0
while pc_num != num:
    num = int(input('Try to guess what number the computer thought between 0 and 10: '))
    attempt += 1
    if pc_num == num:
        print('You got it! The number is {}! You have try {} times until the correct answer'.format(pc_num, attempt))
    elif pc_num > num:
        print('More ... please try again!'.format(num))
    else: #pc_num < num:
        print('Less ... please try again!'.format(num))

from random import randint
from time import sleep

pc_num = randint(0, 5) #make the pc think in a number
#pc_num = random.choice(pc_num) another option
print('--'*15)
num = int(input('What number am I thinking (0-5)? '))
print('--'*15)
print('Processing...')
sleep(3)
if pc_num == num:
    print('The number is {}, you got it!'.format(pc_num))
else:
    print('Sorry, the correct number is {}'.format(pc_num))

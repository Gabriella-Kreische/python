import random
from Exercises import colour

print('{}{}{}'.format(colour.red, '-=+=-'*15, colour.clear))
print('JOKENPON GAME')
print('{}{}{}'.format(colour.green, '-----'*15, colour.clear))
player1 = int(input('Press 1 for STONE, 2 for PAPER or 3 for SCISSOR: '))
list = ['Stone', 'Paper', 'Scissor']
player2 = random.choice(list)
print('Computer chose: {}!'.format(player2))

if player1 == 1:
    if player2 == 'Stone':
        print('Broke Even. Please try again!')
    elif player2 == 'Scissor':
        print('Stone and {}. You won!!'.format(player2))
    elif player2 == 'Paper':
        print('Stone and {}. The computer won!!'.format(player2))
elif player1 == 2:
    if player2 == 'Paper':
        print('Broke Even. Please try again!')
    elif player2 == 'Stone':
        print('Paper and {}. You won!!'.format(player2))
    elif player2 == 'Scissor':
        print('Paper and {}. The computer won!!'.format(player2))
elif player1 == 3:
    if player2 == 'Scissor':
        print('Broke Even. Please try again!')
    elif player2 == 'Paper':
        print('Scissor and {}. You won!!'.format(player2))
    elif player2 == 'Stone':
        print('Scissor and {}. The computer won!!'.format(player2))
else:
    print('Number invalid, please try again!')

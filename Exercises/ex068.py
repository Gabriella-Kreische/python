import random

print('-=-'*10)
print('EVEN OR ODD GAME')

victory = 0
result = ''
while True:
    print('-=-' * 10)
    n = int(input('Type a number: '))
    choice = ' '
    while choice not in 'EO':
        choice = input('Even or Odd? [E/O] ').strip().upper()[0]
    pc = random.randint(0, 10)
    s = n + pc
    print('-' * 30)
    if s % 2 == 0:
        result = 'EVEN'
    else:
        result = 'ODD'
    print(f'You have played {n} and the computer {pc}. The total was {s} and it is a {result} number')
    print('-' * 30)
    if result == 'EVEN' and choice in 'Oo' or result == 'ODD' and choice in 'Ee':
        print('GAME OVER!')
        print(f'You have won {victory} times.')
        break
    else:
        print('Congratulations you WON!')
        print('Lets play again...')
        victory += 1

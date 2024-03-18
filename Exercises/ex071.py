print('=' * 50)
print('{:^50}'.format('NZ BANK'))
print('=' * 50)
money = int(input('How much would like to withdraw? $ '))
money_left = money
fifty_note = 50
twenty_note = 20
ten_note = 10
one_note = 1

while True:
    if money_left == 0:
        break
    elif money_left // fifty_note != 0:
        fifty_note_printed = money // fifty_note
        print(f'The machine will print {fifty_note_printed} bank note of $50')
        money_left = money_left - (fifty_note_printed * fifty_note)
        #print(fifty_note_printed)
        #print(f'Money left: {money_left}')
    elif money_left // twenty_note != 0:
        twenty_note_printed = money_left // twenty_note
        print(f'The machine will print {twenty_note_printed} bank note of $20')
        money_left = money_left - (twenty_note_printed * twenty_note)
        #print(twenty_note_printed)
        #print(f'Money left: {money_left}')
    elif money_left // ten_note != 0:
        ten_note_printed = money_left // ten_note
        print(f'The machine will print {ten_note_printed} bank note of $10')
        money_left = money_left - (ten_note_printed * ten_note)
        #print(ten_note_printed)
        #print(f'Money left: {money_left}')
    elif money_left // one_note != 0:
        one_note_printed = money_left // one_note
        #print(one_note_printed)
        print(f'The machine will print {one_note_printed} bank note of $1')
        break



from Exercises import colour

print('{}{:=^50}{}'.format(colour.green,' PALINDROME TESTER ', colour.clear))
phrase = input('Type something: ')
print('You have entered: {}{}{}'.format(colour.yellow,phrase, colour.clear))
phrase = phrase.replace(' ', '')

letter_list = []
reverse_list = []
for c in phrase:
    letter_list.append(c)

for c in range(len(letter_list)-1, -1, -1):
    reverse_list += letter_list[c]

if letter_list == reverse_list:
    print('You have a {}palindrome{} phrase/word!!'.format(colour.red, colour.clear))
else:
    print('It is {}NOT{} a palindrome'.format(colour.red, colour.clear))

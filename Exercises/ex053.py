import colour

print('{}{:=^50}{}'.format(colour.green,' PALINDROME TESTER ', colour.clear))
phrase = input('Type something: ').strip().upper()
print('You have entered: {}{}{}'.format(colour.yellow,phrase, colour.clear))
#To join a string
phrase = phrase.replace(' ', '')
words = phrase.split()
together = ''.join(words)
reverse = together[::-1]
'''
reverse = ''

for letter in range(len(together)-1, -1, -1):
    reverse += together[letter]
'''

if reverse == together:
    print('You have a {}Palindrome{} phrase/word!!'.format(colour.red, colour.clear))
else:
    print('It is {}NOT{} a Palindrome!'.format(colour.red, colour.clear))

phrase = input('Type a phrase: ')
print('The letter A appear in this phrase {} times'.format(phrase.count('a')))
print('The first time this letter appear is in position {}'.format(phrase.find('a')))
print('The last time this letter appear in the phrase is in position {}'.format(phrase.rfind('a')))
phrase = input('Type a phrase: ').strip()
phrase = phrase.lower()
phrase_a = phrase.count('a')
print('The letter A appears {} times in this phrase.'.format(phrase_a))
print('The first letter A is in position {}'.format(phrase.find('a')+1))
print('The last letter A is in postion {}'.format(phrase.rfind('a')+1))

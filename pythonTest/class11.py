#colour = \0033[0;33;44m] #[style;text;background m
#style:
#0 None
#1 Bold
#4 Underline
#7 Negative

#text:
# 30 white
# 31 red
# 32 green
# 33 yellow
# 34 blue
# 35 purple
# 36 light blue
# 37 gray

#background same but 40 - 47

word = 'Test'
print('\033[0;30;41m{}Test')

print('\033[4;33;46m{}'.format(word))
print('\033[1;35;43m{}'.format(word))
print('\033[0;30;42m{}'.format(word))
print('\033[m{}'.format(word))
print('\033[7;30m{}'.format(word))

word2 = 'Hello World'

print('\033[7;31m{}\033[m'.format(word2))

a = 3
b = 5
print('The values are \033[1;33m{}\033[m and \033[1;34m{}\033[m!!'.format(a, b))

name = 'Guanabara'
colour = { 'clear' : '\033[m',
           'blue' : '\033[0;34m',
           'yellow' : '\033[0;33m',
           'blackandwhite' : '\033[7;30m'}
print('Nice to meet you {}{}{}!!!'.format(colour['yellow'], name, colour['clear']))


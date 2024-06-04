print('{:=^60}'.format(' FIFA WORLD CUP RESULTS '))
print('-'*60)
result = ('Argentina', 'France', 'Croatia', 'Morocco')
print(f'List of winners of the 2022 FIFA World Cup are {result}')
print('-'*60)
print(f'The first and second champions are {result[:2]}')
print('-'*60)
print(f'The third and fourth champions are {result[2:]}')
print('-'*60)
print(f'The winners in alphabetic order are {sorted(result)}')
print('-'*60)
print(f'France is in {result.count("France")+1}\u00b0 position')

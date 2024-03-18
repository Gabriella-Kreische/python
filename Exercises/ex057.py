gender = input('What is your gender? (F/M) ')
while gender not in 'MmFf':
    gender = input('Value not accepted. Please try again! What is your gender? (F/M) ')
print('Gender {} register with success!'.format(gender.upper()))

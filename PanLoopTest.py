times_to_clean = 4

while True:
    answer = input('Is pan clean?\n')
    if answer == 'yes':
        print('Great! Put it away')
        break
    else:
        print('Give it another go!')
        times_to_clean -=1
        
    if times_to_clean == 0:
        print('Throw it away! Time for a new one.')
        break
    
    

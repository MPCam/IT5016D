#ChessBoard.py
#M.Campbell
#25/08/2024

black_square = 'black'
white_square = 'white'

letter = input('Please enter a letter \n')
number = int(input('Please enter a number \n'))

if letter == ('a, c, e, g')  and number %2==0:
    print(black_square)
elif letter == ('b, d, f, h') and number %2==1:
    print(black_square)
else:
    print(white_square)

import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def checkRows(symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            board[i][j] == symbol
            count = count+1
        if count==3:
            print(symbol,'won')
            return True
            

def won(symbol):
    return checkRows(symbol) or checkColumn(symbol) or checkDiagnols(symbol)

def place(symbol):
    print(numpy.matrix[board])
    while(1):
        row = int(input('Enter the row 1 or 2 or 3: '))
        column = int(input('Enter the column 1 or 2 or 3: '))
        if row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-':
            break
        else:
            print('Invalid entry')
    symbol = board[row-1][column-1]
    return symbol
    

def play():
    for turn in range(0,9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won():
                break
        
        else:
            print('O turn')
            place(p2s)
            if won():
                break
            
    if not win():
        print('Its a draw')
        
play()

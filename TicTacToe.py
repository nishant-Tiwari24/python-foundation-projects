import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def place(symbol):
    print(numpy.matrix[board])
    

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

import random as random
movies=['drishyam','nayakan','avengers','pink','golmaal','vikram vedha','black friday','dangal','manichithratazu','taare zameen par']

def createQues(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range (n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('-')
    separator = ''
    qn = separator.join(temp) #converts back to string
    return qn

def isPresent(letter,movie):
    return letter in movie
     
def unlock(question, movie, letter):
    question = list(question)
    for i in range(len(movie)):
        if movie[i] == letter:
            question[i] = letter
    return ''.join(question)

def play():
    p1name = input('Player 1 enter your name: ')
    p2name = input('Player 2 enter your name: ')
    pointsP1=0
    pointsP2=0
    turn=0
    willing=True
    
    while(willing is True):
        if turn%2==0:
            print(p1name," Your Turn")
            pickedMovie = random.choice(movies)
            question = createQues(pickedMovie)
            print(question)
            
            notSaid = True
            while(notSaid):
                letter = str(input("Your letter: "))
                if(isPresent(letter,pickedMovie)):
                    modifiedQues = unlock(modifiedQues,pickedMovie,letter)
                    print(modifiedQues)
                    d = int(input('Press 1 to guess the movie name or 2 to nlock another letter'))
                    if d==1:
                        ans = input('Your answer: ')
                        if ans == pickedMovie:
                            pointsP1 = pointsP1+1
                            print('Correct')
                            notSaid = False
                            print(p1name,'Your score : ', pointsP1)
                        else:
                            print('Try again')
                    
                else:
                    print(letter," is not found")

            c = int(input("Press 1 to continue or 0 to exit"))
            if c==0:
                print(p1name,'Your score is ',pointsP1)
                print(p2name,'Your score is ',pointsP2)
                print('Thanks for playing')
                willing = False
                
        else:
            print(p2name," Your Turn")
            pickedMovie = random.choice(movies)
            question = createQues(pickedMovie)
            print(question)
            
            notSaid = True
            while(notSaid):
                letter = input("Your letter")
                if(isPresent(letter,pickedMovie)):
                    modifiedQues = unlock(modifiedQues,pickedMovie,letter)
                    print(modifiedQues)
                    d = input('Press 1 to guess the movie name or 2 to nlock another letter')
                    if d==1:
                        ans = input('Your answer: ')
                        if ans==pickedMovie:
                            pointsP2=pointsP2+1
                            print('Correct')
                            notSaid=False
                            print(p2name,'Your score : ',pointsP2)
                        else:
                            print('Try again')
                    
                else:
                    print(letter," is not found")

            c = input("Press 1 to continue or 0 to exit")
            if c==0:
                print(p1name,'Your score is ',pointsP1)
                print(p2name,'Your score is ',pointsP2)
                print('Thanks for playing')
                willing = False
        
        turn=turn+1

play()

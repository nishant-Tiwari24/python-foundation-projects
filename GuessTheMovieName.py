import random
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
    separator = ', '   # You can change this to the desired separator
    qn = separator.join(str(x) for x in temp) #converts back to string
    return qn

def isPresent(letter,movie):
    c = movie.count(letter)  #counts the number of times the letter is present in the movie
    if c==0:
        return True
    else:
        return False
     
def unlock(qn,movie,letter):
    n = len(movie)
    ref = list(movie)
    refQn = list(qn)
    temp = []
    for i in range (n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if ref[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    
    separator = ','
    qnNew = separator.join(str(x) for x in temp)
    return qnNew
    

def play():
    p1name = input('Enter your name: ')
    p2name = input('Enter your name: ')
    pointsP1=0
    pointsP2=0
    turn=0
    willing=True
    
    while(willing==True):
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

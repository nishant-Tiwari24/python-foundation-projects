import random
movies=['Drishyam','Nayakan','Avengers','Pink','Golmaal','Vikram Vedha','Black Friday','Dangal','Manichithratazu','Taare Zameen Par']

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
            question = createBlanks(pickedMovie)
            print(question)
            
            notSaid = True
            while(notSaid):
                letter = input("Your letter")
                if(isPresent(letter,pickedMovie)):
                    modifiedQues = unlock(modifiedQues,pickedMovie,ch)
                    print(modifiedQues)
                    d = input('Press 1 to guess the movie name or 2 to nlock another letter')
                    if d==1:
                        ans = input('Your answer: ')
                        if ans==pickedMovie:
                            pp1=pp1+1
                            print('Correct')
                            notSaid=False
                            print(p1name,'Your score : ',pp1)
                    
                else:
                    print(letter," is not found")
        
        else:
        
        turn=turn+1

play()

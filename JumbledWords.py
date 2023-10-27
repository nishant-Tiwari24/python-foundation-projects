import random

def choose():
    words = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "mango", "orange", "pear"]
    pick = random.choice(words)
    return pick



def jumble(word):
   jumbled = "".join(random.sample(word,len(word)))
   return jumbled

def thank(player1,player2,pp1,pp2):
    print(player1," score is ",pp1)
    print(player2," score is ",pp2)
    print('Thanks for playing')

def play():
    player1 = input('Enter the name of first player: ')
    player2 = input('Enter the name of second player: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    
    pickedWord = choose()
    qn = jumble(pickedWord)
    print(qn)
    
    while(1):
        if turn%2 == 0:
            print(player1," your chance")
            ans = input('What is in your mind?\n')
            if ans == pickedWord:
                pp1 = pp1 + 1
                print('Your score is ',pp1)
            else:
                print('Better luck next time')
            c = int(input('Choose 1 to continue and 0 to quit '))
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
        
        else:
            print(player1," your chance")
            ans = input('What is in your mind?')
            if(ans == pickedWord):
                pp1 = pp1 + 1
                print('Your score is ',pp1)
            else:
                print('Better luck next time',pickedWord)
            c = int(input('Choose 1 to continue and 0 to quit'))
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
        turn=turn+1

play()
    
import random

doors = [0]*3
goatDoor = [0]*2
swapWins = 0 
noSwapWins = 0

price = random.randint(0,2)
doors[price] = 'price'

for i in range(0,2):
    if(i==price):
        continue
    else:
        doors[i] = 'Goat'
        goatDoor.append(i)
c = int(input("Enter your choice"))
doorOpen = random.choice(goatDoor)
while(doorOpen==c):
    doorOpen = random.choice(goatDoor)
ch = input("Do you want to swap? y/n")
if(ch=='y'):
    if(doors[c]=='Goat'):
        print('Player wins')
        swapWins =  swapWins + 1
    else:
        print('Player lost')
else:
    if(doors[c]=='Goat'):
        print('Player lost')
    else:
        print('player wins')
        noSwapWins = noSwapWins + 1
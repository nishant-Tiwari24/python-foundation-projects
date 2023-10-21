import random
yourChoice = int(input("Enter your number: type 0 for Rock, type 1 for Paper and type 2 for scissors: "))
if(yourChoice >= 3 or yourChoice <0):
    print("Invalid number seclected")
computerChoice = random.randint(0,2)
print("Computer's choice is",computerChoice)

if(yourChoice == computerChoice):
    print("Its a draw")
elif(yourChoice == 0 and computerChoice == 2):
    print('You lose')
elif(yourChoice == 2 and computerChoice == 1):
    print('You Win')
elif(yourChoice > computerChoice):
    print('You Win')
elif(yourChoice < computerChoice):
    print('You lose')


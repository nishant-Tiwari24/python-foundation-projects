import random    
name = input("What is your name? ")    
print("Good Luck ! ", name) 
print ("Guess the word")

   
words = ['accept', 'acting', 'advice', 'beauty', 'python', 'before', 'player', 'beyond', 'artist', 'branch', 'boards', 'branch'] 
astrick = words.replace(words,"*" * len(words)) 
   
 
word = random.choice(words) 
   
   
print("Guess the characters") 
   
guesses = '' 
   
 
turns = 9000
      
while turns > 0: 
       
    
    failed = 0
       
     
    for char in word:  
           
        
        if char in guesses:  
            print(char) 
               
        else:  
            print("_") 
               
           
            failed += 1
               
   
    if failed == 0: 
         
        print("You Win")  
           
        print("The word is: ", word)  
        break
     
    guess = input("guess a character:") 
       
     
    guesses += guess  
      
    if guess not in word: 
           
        turns -= 1
           
        
        print("Wrong") 
           
        
        print("You have", + turns, 'more guesses') 
           
           
        if turns == 0: 
            print("You Loose")
 
input ("press enter to continue")
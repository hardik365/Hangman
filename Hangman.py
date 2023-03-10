#Author - Hardik Shahu
#Name - Hangman

from asyncio.windows_events import NULL

from words import wordList
import random

CONST_LIVES = 10 #insert # of lives you want



#This function will pick a random word from our list and return that
def getWord(): 
   word = random.choice(wordList)
   return word.upper()


#This function will be where the user actually plays the game
def round(word):
    
    livesLeft = CONST_LIVES
    completedWord = "_" * len(word)
    guessedSoFar = []

    while( True == True):

        print("\n\nSo far, the deciphered word looks like: " + completedWord)
        print("\nSo far, the letters you have guessed are: ")
        print(guessedSoFar)
        print("\nYou have " + str(livesLeft) + " lives left!")

        guessedLetter = input("Please enter a letter: ").upper()

        if guessedLetter.isalpha() == False:
            print("Error, only input letters, try again!")
        
        elif guessedLetter in guessedSoFar:
            print("Error, only input letters you have not already inputed, try again!")
        
        else:

            guessedSoFar.append(guessedLetter)

            if guessedLetter in word: #If they guess right letter
                print("Nice, " + guessedLetter + " is in the secret word!" )
                
                #This will replace "_" at the right spot in the word to display
                tempWordList = list(completedWord)
                indices = [i for i, letter in enumerate(word) if letter == guessedLetter]
                for i in indices:
                    tempWordList[i] = guessedLetter
                    completedWord = "".join(tempWordList)
               
                
                if(completedWord == word): #if they fully guessed the word
                    print("Comgrats! You won this round!\nYou were able to successfully guess the word: " + completedWord )
                    return NULL

            else: #if they dont guess right letter
                print("Sorry, " + guessedLetter + " is not correct letter!" )
                livesLeft = livesLeft - 1


                if livesLeft == 0:
                    print("Sorry! You lost this round, the correct word was: " + word )
                    return NULL
    return NULL




#"Main" starts from here
start = input("Welcome to Hangman!\nPress any key to begin! ")

endGame = False

while endGame != True:

   round(getWord())
   cont = input("\n\nContinue playing? Enter Y for yes and N for no: ").upper()

   if(cont == "N"):
       endGame = True
   
   elif(cont != "Y"):
       print("Error, you typed unexpected input, game will close now.")
       endGame = True


print("Thank You for playing!")
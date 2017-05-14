import random 

# generate a random number between 1 and 10 
  
def main():
  round = 1
  guesses = 5
  secret_num = random.randint(1, 10) 
  print("Round {} start!".format(round))
  
  while True and guesses > 0: 
    # get a number guess from the player 
    guess = int(input("Guess a number between 1 and 10: ")) 
    # compare guess to secret number 
    
    if guess == secret_num: 
      # print hit / miss 
      print("Congratulations! you guessed right! \n Would you like to play again?")  
      answer = str(input("> ")) 
      # lets the user start a new round with a newly generated number
      if answer.upper() == 'YES':
        round += 1
        secret_num = random.randint(1, 10)
        print("Round {} start!".format(round))
        continue 
      # ends the program
      else: 
        print("Thanks for playing!") 
        break
    
    else: 
      guesses -= 1
      print("You guessed wrong \n {} guesses remaining".format(guesses)) 
      if guesses == 0: 
        print("You have ran out of guesses, play again?") 
        answer = str(input("> ")) 
        
        if answer.upper() == 'YES':
          round += 1
          guesses = 5
          secret_num = random.randint(1, 10)
          print("Round {} start!".format(round))
          continue 
        
        # ends the program
        else: 
          print("Thanks for playing!") 
          break
        
      
print("Welcome to the Number Game!") 
main()

#RPS.py
#Name:Alexa Falkner
#Date:9/14/0205
#Assignment:RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  again = "Y"
  while again == "Y":
      
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    computer = random.choice( ["R","P","S"] )
    player = input("Choose Rock, Paper, or Scissors (R,P,S) !! ")
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    if computer == "R":
      print("Opponent chose Rock!")
    elif computer == "P":
      print("Oppponent chose Paper!")
    else:
      print("Opponent chose Scissors!")


    if player == "R":
      print("You chose ROCK!!!")
    elif computer == "P":
      print("You chose PAPER!!!")
    else:
      print("You chose SCISSORS!!!")



    if player == "R" and computer == "R":
      print("It's a TIE!!")
      ties = ties + 1 
      print("ties:" , ties)
    if player == "R" and computer == "S":
      print("You WIN!!")
      wins = wins + 1
      print("wins:" , wins)
    if player == "R" and computer == "P":
      print("You LOSE!!")
      losses = losses + 1
      print("lossses:" ,losses)

    if player == "S" and computer == "S":
      print("It's a TIE!!")
      ties = ties + 1 
      print("ties:" , ties)
    if player == "S" and computer == "P":
      print("You WIN!!")
      wins = wins + 1
      print("wins:" , wins)
    if player == "S" and computer == "R":
      print("You LOSE!!")
      losses = losses + 1
      print("lossses:" ,losses)

    if player == "P" and computer == "P":
      print("It's a TIE!!")
      ties = ties + 1 
      print("ties:" , ties)
    if player == "P" and computer == "R":
      print("You WIN!!")
      wins = wins + 1
      print("wins:" , wins)
    if player == "P" and computer == "S":
      print("You LOSE!!")
      losses = losses + 1
      print("lossses:" ,losses)
    #Ask the user if they would like to play again.
    again = input("Go again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()

import random 

def game() :
    player_choice = input("choose any one option( rock or paper or scissor):")
    options=["paper","rock","scissor"]
    computer_choice= random.choice(options)
    choices={"player" : player_choice, "computer" : computer_choice } 
    return choices
choice =game()
print(choice)

def checkwin(player,computer):
   
    if player == computer : 
       return (" its a tie")
    elif player == "rock":
     if computer=="scissor":
           return "rock smashes scissors you won"
     else:
        return "paper covers rock computer won hahahahaha loserr"
    elif player == "paper":
        if computer=="rock":
           return "paper covers rock you won"
        else:
          return " scissor cuts paper computer won"
    elif player == "scissor":
      if computer=="paper":
           return "scissor cuts paper you won"
      else:
         return "rock smashes scissor you lose loser hahahahaha"


result=checkwin(choice ["player"] , choice ["computer"])
print(result)

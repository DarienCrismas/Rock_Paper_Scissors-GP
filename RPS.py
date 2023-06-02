import random 

def rock_paper_scissors():
    player_score = 0
    comp_score = 0
    
    while True:
        move = input("Rock, paper, or scissors? Or quit to quit. ")
        comp_move = computer_move()

        if move.lower().strip() == "rock":
            if comp_move == "Paper":
                comp_score += 1
                print("Point to computer!")
            elif comp_move == "Rock":
                print("It's a tie.")
            elif comp_move == "Scissors":
                player_score += 1
                print("Point to player!")

        elif move.lower().strip() == "paper":
            if comp_move == "Paper":
                print("It's a tie.")
            elif comp_move == "Rock":
                player_score += 1
                print("Point to player!")
            elif comp_move == "Scissors":
                comp_score += 1
                print("Point to computer!")
            
        elif move.lower().strip() == "scissors":
            if comp_move == "Paper":
                player_score += 1
                print("Point to player!")
            elif comp_move == "Rock":
                comp_score += 1
                print("Point to computer!")
            elif comp_move == "Scissors":
                print("It's a tie.")
        elif move.lower().strip() == "quit":
            print("See you later.")
            break
          
def computer_move():
   options = ["Rock", "Paper", "Scissors"]
   move = random.choice(options)
   return move


rock_paper_scissors()
    
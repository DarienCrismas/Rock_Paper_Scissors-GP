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
                print("Computer chose Paper! Point to computer!")
            elif comp_move == "Rock":
                print("Computer chose Rock! Nobody gets a point.")
            elif comp_move == "Scissors":
                player_score += 1
                print("Computer chose Scissors! Point to player!")

        elif move.lower().strip() == "paper":
            if comp_move == "Paper":
                print("Computer chose Paper! Nobody gets a point.")
            elif comp_move == "Rock":
                player_score += 1
                print("Computer chose Rock! Point to player!")
            elif comp_move == "Scissors":
                comp_score += 1
                print("Computer chose Scissors! Point to computer!")
            
        elif move.lower().strip() == "scissors":
            if comp_move == "Paper":
                player_score += 1
                print("Computer chose Paper! Point to player!")
            elif comp_move == "Rock":
                comp_score += 1
                print("Computer chose Rock! Point to computer!")
            elif comp_move == "Scissors":
                print("Computer chose Scissors! Nobody gets a point.")
        elif move.lower().strip() == "quit":
            score_calc()

            break
          
def computer_move():
   options = ["Rock", "Paper", "Scissors"]
   move = random.choice(options)
   return move

def score_calc(player, computer):
    print(f"See you later. Here's the final score!")
    print(f"Your score: {player} - Computer score: {computer}")
    if player > computer:
        print("You won! Congrats!")
    elif player < computer:
        print("You lost, get gud.")
    else:
        print("Nobody won, you're psychic in the worst way.")

rock_paper_scissors()
    
import random 

"""This is a rock paper scissors game with random messages when the player wins or loses against the computer."""

def rock_paper_scissors():
    player_score = 0
    comp_score = 0

    print("Welcome to rock-paper-scissors! Choose rock, paper, or scissors and hope you get lucky. Try a few times, see if you get any secrets.")
    print()
    
    while True:
        move = input("Rock, paper, or scissors? Or quit to quit. ")
        comp_move = computer_move()

        if move.lower().strip() == "rock":
            if comp_move == "Paper":
                comp_score += 1
                print("Computer chose Paper! Point to computer!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Rock":
                print("Computer chose Rock! Nobody gets a point.")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Scissors":
                player_score += 1
                print("Computer chose Scissors! Point to player!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()

        elif move.lower().strip() == "paper":
            if comp_move == "Paper":
                print("Computer chose Paper! Nobody gets a point.")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Rock":
                player_score += 1
                print("Computer chose Rock! Point to player!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Scissors":
                comp_score += 1
                print("Computer chose Scissors! Point to computer!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            
        elif move.lower().strip() == "scissors":
            if comp_move == "Paper":
                player_score += 1
                print("Computer chose Paper! Point to player!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Rock":
                comp_score += 1
                print("Computer chose Rock! Point to computer!")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
            elif comp_move == "Scissors":
                print("Computer chose Scissors! Nobody gets a point.")
                print(f"Current Totals. Player Score: {player_score} Computer Score: {comp_score}")
                point_gap(player_score, comp_score)
                print()
        elif move.lower().strip() == "quit":
            score_calc(player_score, comp_score)

            break
          
def computer_move():
   options = ["Rock", "Paper", "Scissors"]
   move = random.choice(options)
   return move

def score_calc(player, computer):
    print(f"See you later. Here's the final score!")
    print(f"Your score: {player} - Computer score: {computer}")
    if player > computer:
        print(f"You won! {victory_messages()}")
    elif player < computer:
        print(f"You lost. {defeat_messages()}")
    elif player == 0 and computer == 0:
        print("Leaving so soon?")
    else:
        print("Nobody won, you're psychic in the worst way.")

def victory_messages():
   options = ["You are the best!", "If winning is not important, why keep score?", "Where there is perseverance, there is victory!", 
              "The harder the conflict, the more glorious the triumph.", "Without victory, there is no survival!"]
   move = random.choice(options)
   return move

def defeat_messages():
   options = ["Get gud.", "Death before dishonor!", "Towards thee I roll, thou all-destroying but unconquering whale; to the last I grapple with thee; from hell's heart I stab at thee; for hate's sake I spit my last breath at thee.", 
              "Never confuse a single defeat with a final defeat.", "You didn't lose the game, you just ran out of time.", "That's it! Game over, man! Game over!", 
              "Defeat is not the worst of failures. Not to have tried is the true failure."]
   move = random.choice(options)
   return move

def point_gap(player, computer):
    if computer > (player + 1):
        print("Watch out, they're beating you!")
    

rock_paper_scissors()
    
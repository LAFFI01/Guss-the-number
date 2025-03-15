import random
def update_highest_score(name , guess):
    try:
        with open('highscore.txt','r')as f:
            lines = f.readlines()
            if lines:
                best_player, best_guesses = lines[0].strip().split(" - ")
                best_guesses = int(best_guesses)
            else:
                best_player,best_guesses = "",float('inf')
                
    except FileNotFoundError:
        best_player,best_guesses="", float('inf')
        
    if (guess < best_guesses):
        print(f"Congratulation, {name}! with {guess}") 
        with open('highscore.txt','w')as f:
            f.write(f"{name} - {guess}\n")
    else:
        print(f"The current high score is held by {best_player} with {best_guesses}")
        
        
target = random.randint(1,50)

name = input("Enter the name: ").capitalize()

print(f"Welcome to game {name}.\n please enter the number between 1 to 50.")
guess = 0
guess_life = 5

while (guess<guess_life):
    guess += 1
    player = int(input("Enter the number: "))
    try:
        if(player>target):
            print(f"Go down than {player} ")
        elif(player<target):
            print(f"Go up than {player}")
        else:
            print(f"You win! {name}")
            print(f"Your score is {guess}")
            update_highest_score(name , guess)
            break
    except ValueError:
        print("Please enter a valid number")
        
if(player!=target and guess==guess_life):
    print(f"You loss! {name}")


with open('game.txt','a')as f:
    if player == target:
        f.write(f"{name} win the game in {guess}\n")
    else:
        f.write(f"{name} loss the game in {guess}\n")
        

import random
target = random.randint(1,50)
name = input("Enter the name: ").capitalize()
print(f"Welcome to game {name}.\n please enter the number between 1 to 50.")
guess = 0
guess_life = 5
while guess<guess_life:
    guess += 1
    player = int(input("Enter the number: "))
    try:
        if(player>target):
            print(f"Go down than {player} ")
        elif(player<target):
            print(f"Go up than {player}")
        else:
            print(f"You win! {name}")
            break
    except ValueError:
        print("Plese enter the number")
if(player!=target and guess==guess_life):
    print(f"You loss! {name}")

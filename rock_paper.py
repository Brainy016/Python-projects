import random

choice=["rock", "paper", "scissors"]
running=True

while running:
    user_choice = input("Enter a choice: (rock,paper,scissors):").lower()
    computer_choice = random.choice(choice)

    if user_choice not in choice:
        print("invalid choice")
    user_choice = input("Enter a choice: (rock,paper,scissors)").lower()
    computer_choice = random.choice(choice)
    print(f"Your choice: {user_choice}")
    print(f"computer: {computer_choice}")
else:
    if user_choice==computer_choice:
        print("Draw")
    elif user_choice=="rock"  and computer_choice=="scissors":
        print("You win")
    elif user_choice=="scissors" and computer_choice=="paper":
        print("You win")
    elif user_choice=="paper" and computer_choice =="rock":
        print("You win")
    else:
        print("You lose")
    if not input("Play agian? (y/n)")=="y":
        running=False
print("Thanks for playing")
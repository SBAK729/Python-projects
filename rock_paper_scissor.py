import random 

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choices_dict = {
    ROCK:"Rock 🪨",
    PAPER:"Paper 📄",
    SCISSORS:"Scissor ✂️",
}

choices = tuple(choices_dict.keys())

def rock_paper_scissor():
    user_choice = input("Rock, Paper Or Scissor? (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid Choice!! (r/p/s): ")
        rock_paper_scissor()

    computer_choice =random.choice(choices)

    if user_choice == computer_choice :
        print("Tie")

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You Win!")

    else:
        print("You Lose!!")

    print(f"Your choice: {choices_dict[user_choice]}")
    print(f"Computer choice: {choices_dict[computer_choice]}")

    if input("Do you want to play again? (y/n): ").lower() == "y":
        rock_paper_scissor()
    
rock_paper_scissor()
import random 


choices = ("r", "p", "s")

choices_dict = {
    "r":"Rock 🪨",
    "p":"Paper 📄",
    "s":"Scissor ✂️",
}


def rock_paper_scissor():
    user_choice = input("Rock, Paper Or Scissor? (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid Choice!!")

    computer_choice =random.choice(choices)

    if user_choice == "r" and computer_choice == "p":
        print(f"Your choice: {choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Loss!")

    elif user_choice == "r" and computer_choice == "s":
        print(f"Your choice: {choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Win!")

    elif user_choice == "s" and computer_choice == "p":
        print(f"Your choice:{choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Win!")

    elif user_choice == "s" and computer_choice == "r":
        print(f"Your choice:{choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Loss!")

    elif user_choice == "p" and computer_choice == "r":
        print(f"Your choice: {choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Win!")

    elif user_choice == "p" and computer_choice == "s":
        print(f"Your choice: {choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("You Loss!")

    else:
        print(f"Your choice: {choices_dict[user_choice]}")
        print(f"Computer choice: {choices_dict[computer_choice]}")
        print("Tie")


    if input("Do you want to play again? (y/n): ").lower() == "y":
        rock_paper_scissor()
    
rock_paper_scissor()
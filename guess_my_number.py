import random
def guess_my_number():

    number_to_guess = random.randint(1,100)

    guessed = int(input("Guess number between 1 and 100: "))

    if guessed >= 1 and guessed <=100:

        if number_to_guess == guessed:
            print("\nCongratulations!, You guessed the Number!")
        elif number_to_guess < guessed:
            print("Too High!!")
            guess_my_number()
        else:
            print("Too Low!!")
            guess_my_number()
    else:
        print("Invalid Input. Only number between 1 and 100")
        guess_my_number()


guess_my_number()

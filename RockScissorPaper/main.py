from random import choice

done = False
all_choices = ["rock", "paper", "scissors"]
CPU_score = 0
user_score = 0

"""game loop"""
while not done:
    choice_made = None

    """generate random choice for bot"""
    CPU_choice = choice(all_choices)

    """ask user for user's choice"""
    user_input = input(
        "\nEnter 1 for Rock, 2 for Paper or 3 for Scissors. Enter x to quit: ")

    """validate user's input"""
    if user_input == "1":
        user_choice = "rock"
        choice_made = "valid"
    elif user_input == "2":
        user_choice = "paper"
        choice_made = "valid"
    elif user_input == "3":
        user_choice = "scissors"
        choice_made = "valid"
    elif user_input == "x":
        choice_made = "close"
    else:
        print("Invalid input. Please try again")

    """if user input is valid, compare"""
    if choice_made == "valid":
        print(
            f"Computer select \'{CPU_choice}\': User select \'{user_choice}\'")

        if user_choice == CPU_choice:
            print("It is a tie")
        else:
            if user_choice == "rock":
                if CPU_choice == "paper":
                    print("Computer wins")
                    CPU_score += 1
                else:
                    print("User wins")
                    user_score += 1
            if user_choice == "paper":
                if CPU_choice == "scissors":
                    print("Computer wins")
                    CPU_score += 1
                else:
                    print("User wins")
                    user_score += 1
            if user_choice == "scissors":
                if CPU_choice == "rock":
                    print("Computer wins")
                    CPU_score += 1
                else:
                    print("User win")
                    user_score += 1
        print(f"Current score: Computer = {CPU_score}, User = {user_score}")

    """if user input is to quit, end program"""
    if choice_made == "close":
        print("Thanks for playing")
        print(f"Final score: Computer = {CPU_score}, User = {user_score}")
        done = True

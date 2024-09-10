
def rock_paper_scissors():
    import random

    while True:
        try:
            player = int(input("Rock - paper - scissors. What is your choice?\nAnswer with '1', '2' or '3':\n"))
        except ValueError:
            print("This is not one of the numbers from 1 to 3.")
            continue

        computer = random.randint(1,3)

        if player == computer:
            print("Equal draw. Play again!")
        elif player == 1 and computer == 2:
            print("Computer chose paper. Paper beats rock: you lose.")
        elif player == 2 and computer == 1:
            print("Computer chose rock. Paper beats rock: you win.")
        elif player == 2 and computer == 3:
            print("Computer chose scissors. Scissors beat paper: you lose.")
        elif player == 3 and computer == 2:
            print("Computer chose paper. Scissors beat paper: you win.")
        elif player == 1 and computer == 3:
            print("Computer chose scissors. Rock beats scissors: you win.")
        else:
            print("Computer chose rock. Rock beats scissors: you lose.")

        replay = input("Press 'y' if you want to play again!\n").lower()
        if replay != "y":
            break

rock_paper_scissors()

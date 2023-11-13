#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# write down a minigame of rock , paper ,scissors that can be played with the computer when the user inputs his choice of rock , paper or scissors and the computer randomly chooses one of the three options and the winner is decided based on the rules of the game and the score is displayed at the end of the game and the user is asked if he wants to play again or not and the game continues until the user chooses to quit the game , if the user inputs an invalid option he should be alerted and asked to input again and the game continues until the user chooses to quit the game , when someone wins it should appear on console the following message : Pedra vence tesoura (quebrando) in case rock wins from scissors , Tesoura vence papel(cortando) in case scissors wins from paper , Papel vence pedra (embrulhando) in case paper wins from rock , if both the user and the computer choose the same option it should appear on console Empate: both chose the same option and the game continues until the user chooses to quit the game.

import random

def rock_paper_scissors():
    # Score tracking
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("Choose Rock, Paper or Scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid option, please choose again.")
            continue

        # Computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("Empate: both chose the same option.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            user_score += 1
            if user_choice == "rock":
                print("Pedra vence tesoura (quebrando)")
            elif user_choice == "scissors":
                print("Tesoura vence papel (cortando)")
            elif user_choice == "paper":
                print("Papel vence pedra (embrulhando)")
        else:
            computer_score += 1
            if computer_choice == "rock":
                print("Pedra vence tesoura (quebrando)")
            elif computer_choice == "scissors":
                print("Tesoura vence papel (cortando)")
            elif computer_choice == "paper":
                print("Papel vence pedra (embrulhando)")

        # Display scores
        print(f"Score: You {user_score} - Computer {computer_score}")

        # Check if user wants to continue
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over!")

# Uncomment the line below to play the game
rock_paper_scissors()

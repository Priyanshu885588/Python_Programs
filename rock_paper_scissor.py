import random

def get_choices():
    player_choice=input("Enter your choice "+"\n")
    computer_choice=["paper","rock","scissors"]
    choices={"player":player_choice,"computer":random.choice(computer_choice)}
    return choices


def check_win(player,computer):
    print(f"players_choice:{player} computer_choice:{computer}")
    if player == computer:
        return "it's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "rock smashes scissors! You win!"
        else:
            return "paper covers rock! You lose."
    elif player=="paper":
        if computer=="rock":
            return "paper covers rock! You win."
        else:
            return "scissors cuts paper! you lose."
    elif player=="scissors":
        if computer=="paper":
            return "scissors cuts paper! you win."
        else:
            return "rock smashes scissors! You loose."

choices=get_choices()

result=check_win(choices["player"],choices["computer"])
print(result)

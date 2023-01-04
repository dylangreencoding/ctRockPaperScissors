import random


def rps():
    keep_playing = True
    while keep_playing:
        player = input(
            "Rock, paper or scissors? Or 'q' to quit: ").lower().strip()
        computer = random.choice(("rock", "paper", "scissors"))
        if player == computer:
            print(
                f"{player.title()} makes sweet love to {computer} and they run away together to start a family! Everybody wins!")
        elif player == "rock":
            if computer == "scissors":
                print("Rock smashes scissors to tiny pieces! You win!")
            else:
                print("Rock smothered in the night by paper! You lose.")
        elif player == "paper":
            if computer == "rock":
                print(
                    "Paper wraps itself around rock and squeezes until rock is no more! You win!")
            else:
                print(
                    "Paper dismembered and then decapitated in one decisive blow by scissors! You lose.")
        elif player == "scissors":
            if computer == "paper":
                print(
                    "Scissors gives paper severe lacerations and paper bleeds out in the hospital! You win!")
            else:
                print(
                    "Every bone in scissors's body broken by rock! Rock feels nothing! You lose.")
        elif player == "q":
            keep_playing = False


rps()

import random 

choices = ["rock", "paper", "scissors"]

print("🎮 Rock Paper Scissors")

while True:
    user = input("choose (rock/papaer/scissors): ").lower()

    if user not in choices:
        print("invalid choice!!")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("Its' Draw!!")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("🎉 You win!!")
    else:
         print("🙃 Computer wins !!")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y" :
        break

print("Thanks for playing!!")     
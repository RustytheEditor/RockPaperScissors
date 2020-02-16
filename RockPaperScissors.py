import sys
import random


x = 0
output = float

# 1 = Rock
# 2 = Paper
# 3 = Scissors



while x == 0:
    output = 0
    for x in range(1):
        cpu = random.randint(1, 3)
    print("Rock, Paper, or Scissors?")
    choice = input()
    if choice.lower() == "rock":
        if(cpu == 1):
            print("You Tied, Computer chose rock")
            continue
        if(cpu == 2):
            print("You Lose, Computer chose paper")
            continue
        if(cpu == 3):
            print("You Win, Computer chose scissors")
            continue
    if choice.capitalize() == "Rock":
        if(cpu == 1):
            print("You Tied, Computer chose rock")
            continue
        if(cpu == 2):
            print("You Lose, Computer chose paper")
            continue
        if(cpu == 3):
            print("You Win, Computer chose scissors")
            continue



    elif choice.lower() == "paper":
        if(cpu == 2):
            print("You Tied, Computer chose paper")
            continue
        if(cpu == 3):
            print("You Lose, Computer chose scissors")
            continue
        if(cpu == 1):
            print("You Win, Computer chose rock")
            continue
    elif choice.capitalize() == "Paper":
        if(cpu == 2):
            print("You Tied, Computer chose paper")
            continue
        if(cpu == 3):
            print("You Lose, Computer chose scissors")
            continue
        if(cpu == 1):
            print("You Win, Computer chose rock")
            continue


    elif choice.lower() == "scissors":
        if(cpu == 3):
            print("You Tied, Computer chose scissors")
            continue
        if(cpu == 1):
            print("You Lose, Computer chose rock")
            continue
        if(cpu == 2):
            print("You Win, Computer chose paper")
            continue
    elif choice.capitalize() == "Scissors":
        if(cpu == 3):
            print("You Tied, Computer chose scissors")
            continue
        if(cpu == 1):
            print("You Lose, Computer chose rock")
            continue
        if(cpu == 2):
            print("You Win, Computer chose paper")
            continue


    else:
        print("Improper Input")






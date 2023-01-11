import random

def play():
    number = int(input("Number (1 - 3) : "))
    number_2 = random.randint(1, 3)

    if number == number_2:
        print("You won!\n")
    else:
        print("L\n")
    
    play()

play()
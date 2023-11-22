import random

def dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

def main():

    while True:
        rounds = input("Enter how many rounds (1-10): ")
        
        if rounds.isdigit():
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                break
        else:
            print("Invalid, please enetr a number between 1 and 4.")
    roll = dice()
    print(f"Player 1 your roll is {roll}, do you want to roll again?")

if __name__ == "__main__":
    main()
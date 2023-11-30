import random

def dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

def rounds():
    max_health = 100
    player_health = 100
    current_damage = 0

    keep_roll = input("Would you like to keep rolling? yes/no")
    if keep_roll == "yes":
        score = dice()
    
    if keep_roll == "no":
        print("Your turn is over")

def main():

    while True:
        rounds = input("Enter how many rounds (1-10): ")
        
        if rounds.isdigit():
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                break
        else:
            print("Invalid, please enetr a number between 1 and 10.")
    
    rounds()
    # roll = dice()
    # print(f"Player 1 your roll is {roll}, do you want to roll again?")
    # roll = roll + dice()
    # print(f"Player 1 your roll is {roll}, do you want to roll again?")

if __name__ == "__main__":
    main()
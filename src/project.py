import random

def dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

def rounds(result):
    max_health = 100
    player_health = 100
    current_damage = 0

    while current_damage <= player_health:
        keep_roll = input("Would you like to keep rolling? yes/no")
        if keep_roll == "yes":
            score = dice()
            current_damage += score
            print("Your damage is :" , current_damage)
    
        if keep_roll == "no":
            print("Your turn is over")

    return "player 2 wins"
def main():

    while True:
        rounds = input("Enter how many rounds (1-10): ")
        
        if rounds.isdigit():
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                break
        else:
            print("Invalid, please enetr a number between 1 and 10.")
    
    max_health = 100
    player_health = 100
    current_damage = 0

    while current_damage <= player_health:
        keep_roll = input("Do you want to roll? yes/no:")
        if keep_roll == "yes":
            score = dice()
            current_damage += score
            print("Your damage is :" , current_damage)
    
        if keep_roll == "no":
            print("Your turn is over")
            print(f"You have done {current_damage} points of damage!")
            break
    # roll = dice()
    # print(f"Player 1 your roll is {roll}, do you want to roll again?")
    # roll = roll + dice()
    # print(f"Player 1 your roll is {roll}, do you want to roll again?")

if __name__ == "__main__":
    main()
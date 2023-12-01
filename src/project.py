import random

def dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

def rounds():
   

def main():

    while True:
        rounds = input("Enter how many rounds (1-10): ")
        
        if rounds.isdigit():
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                break
        else:
            print("Invalid, please enetr a number between 1 and 10.")
    


#
    player_health = 100
    # player1_points = 0
    # player2_points = 0
    # player1_damage = 0
    # player2_damage = 0
    current_damage = 0
    player_score = ["player1" , "player2"]

    for round_num in range(rounds):
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
            
            if score == 1:
                print("You rolled a 1! Your turn is over!")
                break
        
        round_num = 0
        round_num += 1



#

if __name__ == "__main__":
    main()
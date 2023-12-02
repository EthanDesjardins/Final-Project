import random

def dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

def round(damage):
    current_damage = damage
    keep_roll = input("Do you want to roll? yes/no:")
    score = dice()
    
    if keep_roll == "yes" and score != 1:
        current_damage += score
        print("Your damage is :" , current_damage)
        return current_damage
    
    if keep_roll == "no":
        print("Your turn is over")
        print(f"You have done {current_damage} points of damage!")
        return current_damage
        
                    
    if keep_roll == "yes" and score == 1:
        print("You rolled a 1! Your turn is over!")
        current_damage = 0
        print(f"You have done {current_damage} points of damage!")
        return current_damage
        

def main():

    while True:
        rounds = input("Enter how many rounds (1-10): ")
        
        if rounds.isdigit():
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                break
        else:
            print("Invalid, please enetr a number between 1 and 10.")

    player_health = 20
    player1_health = player_health
    player2_health = player_health
    players = 2
    current_damage = 0
    player_points = {"player1 damage": 0,
                     "player2 damage": 0,
                     "turn_counter" : 0}

 
    for turn_player in range(rounds):
        current_damage = 0
        while current_damage <= player_health:

            print("Player 1's turn!")
            player1_roll = round(current_damage)
            print("Player 2's turn!/n")
            Player2_roll = round(current_damage)
                
            round_num = 0
            round_num += 1
            player_points["player1 damage"] += player1_roll
            player_points["player2 damage"] += Player2_roll

            print("Player1 total score is :", player_points["player1 damage"])
            print("Player2 total score is :", player_points["player2 damage"])
            
            player_points["turn_counter"] += 1
            player1_health = player_health - player_points["player1 damage"]
            player2_health = player_health - player_points["player2 damage"]

            if player1_health <= 0:
                print("Winner is Player2!!")
            if player2_health <= 0:
                print("Winner is Player1!!")
            if player_points["turn_counter"] >= rounds:
                break

            

    print(f"Player1 has {player1_health} health left, and Player2 has {player2_health} health left.")

    if player1_health > player2_health:
        print("Winner is Player1!!")
    if player2_health > player1_health:
        print("Winner is Player2!!")
    if player1_health == player2_health:
        print("It was a Tie!!")

if __name__ == "__main__":
    main()
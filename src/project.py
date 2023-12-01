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
            print("Invalid, please enetr a number between 1 and 10.")
    


#
    player_health = 20
    player1_health = player_health
    player2_health = player_health
    players = 2
    current_damage = 0
    player_points = [0 for _ in range(players)]

    while player1_health > 0 or player2_health > 0 :   
        for turn_player in range(rounds):
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
                    
                if score == 1:
                    print("You rolled a 1! Your turn is over!")
                    current_damage = 0
                    print(f"You have done {current_damage} points of damage!")
                    break
                
            round_num = 0
            round_num += 1
            player_points[turn_player] += current_damage

            print("your total score is :", player_points[turn_player])

        player1_health = player_health - player_points[turn_player]
        player2_health = player_health - player_points[turn_player]

        if player1_health <= 0:
            print("Winner is Player2!!")
        if player2_health <= 0:
            print("Winner is Player1!!")
        print(player1_health)
        print(player2_health)

#

if __name__ == "__main__":
    main()
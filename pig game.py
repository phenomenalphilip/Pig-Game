### Create a dice game that allows for a maximum number of 4 players. 
### Let the players decide what the winning score would be. 
### Each player can roll as many times as they wish during a turn. 
# Every time they roll a number greater than 1, it adds to their total score. 
# If they get a one, their total becomes 0. ###


import random

def roll():
    max_number = 6
    min_number = 1
    roll = random.randint(min_number, max_number)

    return roll

while True: #define the number of players in this game
    player_number = input("How many players (2-4)?: ")
    if player_number.isdigit():
        player_number = int(player_number)
        if 2 <= player_number <= 4:
            break
        else:
            print("Must be between 2 and 4")   
    else:
        print("Invalid. Try again.")

while True: #define maximum score
    max_score = input("What's the winning score for this game? (40 - 100):  ")
    if max_score.isdigit():
        max_score = int(max_score)
        if 40 <= max_score <= 100:
            break
        else:
            print("Has to be between 40 and 100")
    else:
        print("Must be a number")



player_scores = [0 for _ in range(player_number)]

while max(player_scores) < max_score:

    for player_idx in range(player_number):
        print("\nPlayer number", player_idx + 1, " turn has just started!\n")
        print("Your total score is \n", player_scores[player_idx])
        
        current_score = 0

        while True:
            wanna_roll = input("Do you want to roll? (y): ")
            if wanna_roll.lower() != "y":
                break
            else:
                value = roll()
                print(value)
                if value == 1:
                    current_score = 0
                    player_scores[player_idx] =  0
                    print("You rolled a 1!End of turn!!")
                    break
                else:
                    current_score += value
                    print("You rolled a", value)
                
                print("Your current score is", current_score)
                    
        player_scores[player_idx] += current_score
        print("Your totoal score is:", player_scores[player_idx])


winning_num = max(player_scores)
winner_idx = player_scores.index(winning_num)
print("Player number", winner_idx + 1, "is the winner with a score of", winning_num)

print("Player number %d is the winner with a score of %d", winner_idx+1, winning_num)


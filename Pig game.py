### I am creating a game which can have a max no of 4 players. 
# When it is a player's turn, he gets to roll a dice and the number on the dice is added to his score. 
# He can then decide to keep rolling or to pass to the next player. 
# However, if he gets a 1, his score becomes 0 and his turn is over.
# The first player to get a score of 50 wins. 
# Once a player gets to 50, the game ends.


import random

def roll():
    # Since it is a dice roll, our minimum number will have to be 1 and maximum number will have to be 6
    min_number = 1
    max_number = 6

    roll = random.randint(min_number, max_number)
    return roll

while True:
    Player = input("Enter number of player (2 - 4): ")
    if Player.isdigit():
        Player = int(Player)
        if Player >= 2 and Player <= 4:
            print("Welcome.", Player, "players are battling it out in this game.")
            
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid. Must be a number")



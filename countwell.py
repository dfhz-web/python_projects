import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4):  ")


    #isdigit means if it is a valid number
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
           break
        else:
            print("Must be between 2-4 players.")
    else:
         print("Invalid, try again")
# print(players)

max_score = 8
#put a 0 for each player that we have 
player_score = [0 for _ in range(players)]

print(player_score)

#max gives the maximun value for this array or list


# for player_index in range(players):
   
#      print(player_score[player_index])


#while to control when someone wins
while max(player_score) < max_score:
    
    #for to control turns 
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "Turn has just started!\n")
        print("Your total score is: ", player_score[player_index], "\n")
        current_score = 0
        #while to control player's moves and score
        while True:
            should_roll = input("Would u like to roll (y)?  ")

            # if player does not want to continue
            if should_roll.lower() != "y":
                print("Good bye")
                break
            #playing
            value = roll()

            # if got 1
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            # continue playing
            else:
                current_score += value
                print("U rolled a: ", value)
            
            # know about the current score
            print("Your current score is: ",  current_score)

        player_score[player_index] += current_score
        print("Your total score is: ", player_score[player_index])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print("the winner is player number : ", winning_index + 1, "with  an  score of", max_score)
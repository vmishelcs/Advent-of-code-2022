# Part 1:
# A - Rock       X - Rock
# B - Paper      Y - Paper
# C - Scissors   Z - Scissors

score_dict_pt1 = {
    'X' : 0,
    'Y' : 1,
    'Z' : 2,
    'A' : 0,
    'B' : 1,
    'C' : 2
}

def part_one():
    total_points = 0
    with open("Day2/input", "r") as input_file:
        for line in input_file:
            round_points = 0
            # Get opponent and my move
            round_turn = line.rstrip("\n").split(" ")
            opponent_shape = round_turn[0]
            my_shape = round_turn[1]

            # Add score for shape used
            round_points += (score_dict_pt1[my_shape] + 1)
            # Decide who won
            if score_dict_pt1[opponent_shape] == score_dict_pt1[my_shape]:
                # Tie
                round_points += 3
            elif (score_dict_pt1[opponent_shape] + 1) % 3 == score_dict_pt1[my_shape]:
                # I won
                round_points += 6
            # Otherwise I lost, so +0 points
            total_points += round_points
    print("1. Total points: " + str(total_points))


# Part 2:
# A - Rock       X - Lose
# B - Paper      Y - Draw
# C - Scissors   Z - Win

score_dict_pt2 = {
    'X' : 0, # 0 points for losing
    'Y' : 3, # 3 points for draw
    'Z' : 6, # 6 points for win
    'A' : [3, 1, 2], # Lose -> use scissors | Tie -> use rock | Win -> use paper
    'B' : [1, 2, 3], # Lose -> use rock | Tie -> use paper | Win -> use scissors 
    'C' : [2, 3, 1]  # Lose -> use paper | Tie -> use scissors | Win -> use rock 
}

def part_two():
    total_points = 0
    with open("Day2/input", "r") as input_file:
        for line in input_file:
            round_points = 0
            # Get opponent and my move
            round_turn = line.rstrip("\n").split(" ")
            opponent_shape = round_turn[0]
            my_outcome = round_turn[1]

            # Add score for outcome
            round_points += score_dict_pt2[my_outcome]
            # Add score for shape used
            if my_outcome == 'X':
                round_points += score_dict_pt2[opponent_shape][0]
            elif my_outcome == 'Y':
                round_points += score_dict_pt2[opponent_shape][1]
            else:
                round_points += score_dict_pt2[opponent_shape][2]
            
            # Add points for this round
            total_points += round_points
            
    print("2. Total points: " + str(total_points))


if __name__ == "__main__":
    part_one()
    part_two()

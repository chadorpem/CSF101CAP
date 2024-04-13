################################
# chador pem
# B.E ECE
# 02230093
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# https://www.codingal.com/coding-for-kids/blog/rock-paper-scissors-game-in-python/
# https://www.youtube.com/watch?v=1X2kGrryecE
# https://www.w3schools.com/python/python_dictionaries.asp#:~:text=Dictionaries%20are%20used%20to%20store,and%20earlier%2C%20dictionaries%20are%20unordered.
################################
# SOLUTION
# Your Solution Score:
# 49483
################################
def read_input_file(file_name):
    rounds = []
    with open(file_name, 'r') as file:
        for line in file:
            rounds.append(line.strip().split())
    return rounds

# Calculate the score for each round
def calculate_round_score(player_choice, opponent_choice, outcome):
    option = {'A': 1, 'B': 2, 'C': 3} #A for Rock, B for paper and C for scissors
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}# Score for outcomes: X=0, Y=3 and Z=6.
    player_score = option[player_choice] + outcomes[outcome]
    opponent_score = option[opponent_choice] + outcomes[outcome]
    return player_score, opponent_score

# solution
def calculate_total_score(rounds):
    total_score = 0
    for round_info in rounds:
        opponent_choice, outcome = round_info
        if outcome == 'Y':
            player_choice = opponent_choice  # If it is draw then choose the same as the opponent
        elif outcome == 'X':
            player_choice = 'C' if opponent_choice == 'A' else 'A' if opponent_choice == 'B' else 'B'  # Lose
        else:
            player_choice = 'B' if opponent_choice == 'A' else 'C' if opponent_choice == 'B' else 'A'  # Win
        player_score, _ = calculate_round_score(player_choice, opponent_choice, outcome)
        total_score += player_score
    return total_score


file_name = "input_3_cap1.txt"  


rounds = read_input_file(file_name)

# Total score
total_score = calculate_total_score(rounds)

# Output total score
print("Total score:", total_score)
# Write a program that accepts a list of football teams' games with the result of the match as standard input and outputs a summary table of the results of all matches to standard output.

# For a win, the team is awarded 3 points, for a loss — 0, for a draw — 1.

# The input format is as follows:
# The first line contains an integer 𝑛
# n — the number of confident players.

# After that comes 𝑛
# so, in which the articles of the game are written in the online format:
# First_comand;Scored by the First_comand;Second_comand;Scored by the Second_comand

dct = {}
n = int(input())

for _ in range(n):
    team_1, goals1, team_2, goals2 = input().split(';')

    for team in team_1, team_2:
        dct.setdefault(team, {'plays': 0, 'wins': 0, 'draws': 0, 'loss': 0, 'scores': 0})

    dct[team_1]['plays'] += 1
    dct[team_2]['plays'] += 1

    if int(goals1) > int(goals2):
        dct[team_1]['wins'] += 1
        dct[team_1]['scores'] += 3
        dct[team_2]['loss'] += 1
    elif int(goals1) == int(goals2):
        dct[team_1]['wins'] += 1
        dct[team_2]['loss'] += 1
        dct[team_1]['scores'] += 1
        dct[team_2]['scores'] += 1
    else:
        dct[team_2]['wins'] += 1
        dct[team_2]['scores'] += 3
        dct[team_1]['loss'] += 1
        
for k, v in dct.items():
    for v2 in v.values():
        print(f'{k}: {v2}')



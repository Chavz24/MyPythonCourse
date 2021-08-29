"""Challenge: Create a High Scores List 12.7"""

from pathlib import Path
import csv, pprint


# Write a script that reads the data from this CSV file and creates a new
# file called high_scores.csv where each row contains the player name
# and their highest score.

def row_procces(row, header):
    row[header] = int(row[header])
    return row

file_path = Path.cwd() / 'II_Scores.csv'
scores = []
with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append(dict(row_procces(row, 'score')))

player_name = []
for name_score in scores:
    if name_score['name'] in player_name:
        continue
    else:
        player_name.append(name_score['name'])
high_scores = []
for name in player_name:
    score_player = []
    for name_score in scores:
        if name_score['name'] == name:
            score_player.append(name_score['score'])
    highest_s = max(score_player)
    player_high_score = {'name': name, 'high_score': highest_s}
    high_scores.append(player_high_score)

file_path = Path.cwd() / 'II_High_scores.csv'

with file_path.open(mode='w', encoding='utf-8', newline='') as file:
    writer=csv.DictWriter(file,fieldnames=high_scores[0].keys())
    writer.writeheader()
    writer.writerows(high_scores)
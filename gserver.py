import socket
import random
import json

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = {}
    return leaderboard

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f)

def generate_number(difficulty):
    if difficulty == 'Easy':
        return random.randint(1, 50)
    elif difficulty == 'Medium':
        return random.randint(1, 100)
    elif difficulty == 'Hard':
        return random.randint(1, 500)
    else:
        return None
    
def update_leaderboard(leaderboard, name, score):
    if name in leaderboard:
        if score < leaderboard[name]:
            leaderboard[name] = score
    else:
        leaderboard[name] = score


import json

filename = "username.json"

with open(filename, "r") as f:
    username = str(json.load(f))
    print(f"Welcome back {username.title()}!")
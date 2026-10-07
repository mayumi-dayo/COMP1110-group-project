import json
def init_savefile():
    playerdata = {
        "name": "",
        "gender": "", 
        "hp" : {"hp": 100, "max":100},
        "stamina" : {"stamina": 100, "max": 100},
        "mana" : {"mana": 20, "max": 20},
        ""
        "inventory": [
            {"item": "Dull Sword", "Quantity": 1, "weight" :2}
        ]
    }
def load():
    with open("player.json","r") as file:
        playerData = json.load(file)
    return playerData

def save():
    return null
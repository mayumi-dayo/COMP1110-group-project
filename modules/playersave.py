import json
def init_savefile():
    playerdata = {
        "player" : {
            "name": "",
            "gender": "", 
            "hp" : {"hp": 100, "max":100},
            "stamina" : {"stamina": 100, "max": 100},
            "mana" : {"mana": 20, "max": 20},
            "inventory_max_weight" : 100,
            "gold": 50,
            "atk": "",
            "def": "",
            "inventory": [
                {
                    "item":"weap01",
                    "name":"Dull Sword",
                    "quantity":1, 
                    "weight":40, 
                    "data":{"weap"}, 
                    "description": "An iron blade which has since become worn of the past battles it has fought"
                    },
                {
                    "item":"pot01", 
                    "name":"Small Health Potion",
                    "quantity": 1,
                    "weight": 5,
                    "description": "A small health potion. Restores 20 health points."}
            ]
        },
        "scene": 0
    }
def load():
    with open("player.json","r") as file:
        playerData = json.load(file)
    return playerData

def save():
    return null
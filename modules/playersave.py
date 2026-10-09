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
                "weap1": {
                    "name":"Dull Sword",
                    "quantity":1,
                    "weight":40,
                    "weapon":{"is_weapon":True, "type":"melee","atk": 7, "consumable": False},
                    "description": "An iron blade which has since become worn of the past battles it has fought",
                    "script": {"has_script": False}
                    },
                "pot01": {
                    "name":"Small Health Potion",
                    "quantity": 1,
                    "weight": 5,
                    "weapon": {"is_weapon": False},
                    "description": "A small health potion. Restores 20 health points.",
                    "script": {"has_script": True, "script":"""
                        if if playerdata["player"]["inventory"]["pot01"]["quantity"] > 0:
                            if playerdata["player"]["hp"]["hp"] < playerdata["player"]["hp"]["max"]:
                                playerdata["player"]["hp"]["hp"] = playerdata["player"]["hp"]["hp"] + 20
                                if playerdata["player"]["hp"]["hp"] > playerdata["player"]["hp"]["max"]:
                                    playerdata["player"]["hp"]["hp"] = playerdata["player"]["hp"]["hp"]
                                playerdata["player"]["inventory"]["pot01"]["quantity"] = playerdata["player"]["inventory"]["pot01"]["quantity"] - 1
                                if playerdata["player"]["inventory"]["pot01"]["quantity"] <= 0:
                                    del playerdata["player"]["inventory"]["pot01"]
                            else:
                                return"You are already at full health, you can't drink the potion."
                        else:
                            del playerdata["player"]["inventory"]["pot01"]
                        """}
                }
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
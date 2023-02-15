import json


def load_data():
    try:
        with open("save_game.json", "r+") as file:
            game_data = json.load(file)
    except FileNotFoundError:
        return default_values
    return game_data


def save_on_close(program_data: dict):
    with open('save_game.json', 'w') as data:
        json.dump(program_data, data, indent=2)


default_values = {
    "Map": {'current_map': 0},
    "Hunter": {'level': 1, 'health': 100, 'mana': 80},
    "Mage": {'level': 1, 'health': 80, 'mana': 150},
    "Warrior": {'level': 1, 'health': 150},
}


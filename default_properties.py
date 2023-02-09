import pickle
from test_class import Mage
from class_maps.map_controller import MapController
# from hunter_character import Hunter
# from mage_character import Mage
# from warrior_character import Warrior


def load_data():
    try:
        with open("savegame", "rb") as file:
            # file.seek(0)
            take_from_file = pickle.load(file)
    except FileNotFoundError:
        return default_dictionary
    return take_from_file


def save_on_close(program_data: dict, map_data: MapController, current_hero: object):
    program_data["Map"].current_map = map_data.current_map

    with open('savegame', 'wb') as data:
        pickle.dump(program_data, data)


# default properties for the heroes
class Hero:
    def __init__(self, name: str, power: str, is_selected=False):
        self.name = name
        self.power = power
        self.is_selected = is_selected

    def get_name(self):
        return self.name

    def set_selected(self):
        self.is_selected = True
        return self.is_selected


hero = Hero("Superman", "super strength", True)
first_hero = Hero("Dark Wizard", "fireballs", True)
third_hero = Hero("Still no name", "warrior", False)

default_dictionary = {
    "Map": MapController(),
    "Hunter": Hero,
    "Mage": Mage(),
    "Warrior": Mage
}

test = load_data()
print(test)
save_on_close(default_dictionary, default_dictionary["Map"], default_dictionary["Hunter"])

print(test["Mage"].index)
print(test["Map"].current_map)
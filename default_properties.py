import pygame
import pickle
from class_maps.map_controller import MapController
from hunter_character import Hunter
from mage_character import Mage
from warrior_character import Warrior


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
    "Hunter": Hunter(),
    "Mage": Mage(),
    "Warrior": Warrior()
}

test = load_data()
# todo  get info from object or fix EOFError
print(test)
save_on_close(default_dictionary, default_dictionary["Map"], default_dictionary["Hunter"])

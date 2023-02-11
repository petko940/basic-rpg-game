import pickle
from class_maps.map_controller import MapController
from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior


def load_data():
    try:
        with open("savegame", "rb") as file:
            take_from_file = pickle.load(file)
    except FileNotFoundError:
        return default_dictionary
    return take_from_file


def save_on_close(program_data: dict, map_data: MapController, current_hero: (Mage, Warrior, Hunter)):
    program_data["Map"].current_map = map_data.current_map
    program_data[current_hero.__class__.__name__.capitalize()].index = current_hero.index

    with open('savegame', 'wb') as data:
        pickle.dump(program_data, data)


default_dictionary = {
    "Map": MapController(),      # must fix this dict Tamer
    "Hunter": Hunter(),
    "Mage": Mage(),
    "Warrior": Warrior()
}
# mage = Mage()
# map = MapController()
# test = load_data()
#
# print("##################################################")
# # print(f"from hunger_character this is the index of the Hunter: {test['Hunter'].index}")
# print(f"from mage_character this is the index of the Mage: {test['Mage'].index}")
# # print(f"from hunger_character this is the index of the Warrior: {test['Warrior'].index}")
# print(f"from map_controller this is the index of the current map: {test['Map'].current_map}")
# print("##################################################")
# print(test['Warrior'].jump_animation())
#
# save_on_close(default_dictionary, map, mage)

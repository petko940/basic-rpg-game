import json


# import Map -> eventually to set the index to zero, if there is no other JSON files


# default properties for the heroes
class Hero:
    def __init__(self, name: str, power: str, is_selected=False):
        self.name = name
        self.power = power
        self.is_selected = is_selected

    def set_selected(self):
        self.is_selected = True
        return self.is_selected


class HeroEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Hero):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


hero = Hero("Superman", "super strength", True)

first_hero = Hero("Dark Wizard", "fireballs", True)
third_hero = Hero("Still no name", "warrior", False)

default_dictionary = {
    "Map": "",  # map-controller.current-map
    "Hunter": Hero("Hunter", "Long range"),
    "Mage": Hero("Mage", "Fireballs"),
    "Warrior": Hero("Warrior", "Mad Axe")
}

with open("default.json", "w") as file:
    file.write(json.dumps(default_dictionary, cls=HeroEncoder, indent=4))

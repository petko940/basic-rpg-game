import json


class DataProcessor:

    def __init__(self, heroes: list):
        self.loaded_data = self.load_data()   # {"Mage": {'level': 1, 'health': 100, 'mana': 100}}
        self.heroes = heroes                  # [mage, warrior, hunter -> all objects]

    @property
    def default_game_values(self):
        return {
                "Hunter": {'level': 1, 'health': 100, 'mana': 80, 'exp': 0},
                "Mage": {'level': 1, 'health': 80, 'mana': 150, 'exp': 0},
                "Warrior": {'level': 1, 'health': 150, 'exp': 0},
            }

    def load_data(self):
        try:
            with open("save_game.json", "r+") as file:
                game_data = json.load(file)
        except FileNotFoundError:
            return self.default_game_values
        return game_data

    @staticmethod
    def power_hero_to_his_level(hero):
        for _ in range(hero.level - 1):
            hero.get_stronger_after_level_up()

    def set_hero_experience(self, hero):
        hero.experience_gained = self.loaded_data[type(hero).__name__]['exp']
        hero.increase_experience_bar()

    def set_loaded_hero_data(self):
        for hero in self.heroes:
            hero.level = self.loaded_data[type(hero).__name__]['level']
            self.set_hero_experience(hero)
            self.power_hero_to_his_level(hero)

    def save_progress_of_game(self):
        progress_of_game = {}

        for hero in self.heroes:
            hero_name = type(hero).__name__

            progress_of_game[hero_name] = {}

            if hero_name == "Warrior":
                progress_of_game[hero_name] = {'level': hero.level, 'health': hero.health, 'exp': hero.experience_gained}
                continue

            progress_of_game[hero_name] = {'level': hero.level, 'health': hero.health, 'mana': hero.mana, 'exp': hero.experience_gained}

        with open('save_game.json', 'w') as data:
            json.dump(progress_of_game, data, indent=2)

from typing import List
from monsters.monster import Monster


class MonsterController:

    def __init__(self, *monsters: Monster):
        self.monsters: List[Monster] = [*monsters]

    def spawn_monster(self):
        monster = self.monsters[0]

        if monster.can_spawn_monster():
            monster.increase_monsters_on_screen()


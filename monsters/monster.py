from abc import ABC, abstractmethod


class Monster(ABC):
    MONSTERS_ON_SCREEN_LIMIT = 1

    def __init__(self, x_pos: int, y_pos: int):
        self.monsters_on_screen = 0

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.walk_and_idle_index = 0

        self.first_spawn = False
        self.left_direction = True

    @abstractmethod
    def idle(self):
        pass

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def walk(self, hero_x_pos: int):
        pass

    @abstractmethod
    def attack(self):
        pass

    def monster_position(self):
        return self.x_pos, self.y_pos

    def change_direction(self):
        if self.left_direction:
            self.left_direction = False

        elif not self.left_direction:
            self.left_direction = True

    def can_spawn_monster(self):
        return Monster.MONSTERS_ON_SCREEN_LIMIT > self.monsters_on_screen

    def increase_monsters_on_screen(self):
        if self.can_spawn_monster():
            self.monsters_on_screen += 1
from abc import ABC, abstractmethod


class Monster(ABC):
    MONSTERS_ON_SCREEN_LIMIT = 1

    HEALTH_GAIN_AFTER_DEATH = 50

    def __init__(self, health: int, x_pos: int, y_pos: int):
        self.monsters_on_screen = 0

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.max_health = health

        self.walk_and_idle_index = 0

        self.left_direction = True
        self.target_reached = False
        self.is_attacking = False

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

    @abstractmethod
    def check_target_reached(self, hero_x_pos: int):
        pass

    @property
    def is_dead(self):
        return self.health <= 0

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

    def power_up_after_death(self):
        self.max_health += Monster.HEALTH_GAIN_AFTER_DEATH
        self.health = self.max_health
        self.left_direction = True

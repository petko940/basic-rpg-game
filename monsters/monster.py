from abc import ABC, abstractmethod
from pygame import Rect


class Monster(ABC):
    X_POS_SPAWN_AFTER_DEATH = 1400

    MONSTERS_ON_SCREEN_LIMIT = 1

    HEALTH_GAIN_AFTER_DEATH = 50
    DAMAGE_INCREASE_AFTER_DEATH = 3

    HEALTH_BAR_LENGTH = 125
    HEALTH_BAR_HEIGHT = 20

    HEALTH_BAR_COLOR = (178, 247, 125)
    HEALTH_BAR_PAD_COLOR = (105, 105, 105)

    def __init__(self, health: int, damage: int, x_pos: int, y_pos: int):
        self.experience_reward = 50

        self.monsters_on_screen = 0

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.max_health = health
        self.damage = damage
        self.attack_cooldown = 0

        self.walk_and_idle_index = 0
        self.non_looped_index = 0

        self.left_direction = True
        self.is_attacking = False

        self.health_bar = Rect(self.x_pos, self.y_pos, self.HEALTH_BAR_LENGTH, self.HEALTH_BAR_HEIGHT)
        self.background_health_bar = Rect(self.x_pos, self.y_pos, self.HEALTH_BAR_LENGTH, self.HEALTH_BAR_HEIGHT)

    @property
    def is_dead(self):
        return self.health <= 0

    @property
    @abstractmethod
    def rect_hit_box(self):
        pass

    @abstractmethod
    def idle(self):
        pass

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def walk(self, hero_x_pos: int):
        pass

    def attack(self):
        if not self.attack_cooldown and not self.is_attacking:
            self.is_attacking = True

    @abstractmethod
    def increase_index_attack_animation(self):
        pass

    @abstractmethod
    def check_target_reached(self, hero_x_pos: int):
        pass

    @staticmethod
    def check_valid_index(index: float, collection: list):
        if 0 <= index < len(collection):
            return True

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

    def set_default_values_after_death(self):
        self.left_direction = True
        self.background_health_bar.x = Monster.X_POS_SPAWN_AFTER_DEATH
        self.health_bar.x = Monster.X_POS_SPAWN_AFTER_DEATH
        self.health_bar.width = self.HEALTH_BAR_LENGTH
        self.x_pos = Monster.X_POS_SPAWN_AFTER_DEATH
        self.non_looped_index = 0

    def remove_monster_from_screen(self):
        self.monsters_on_screen -= 1

    def power_up_after_death(self):
        self.max_health += Monster.HEALTH_GAIN_AFTER_DEATH
        self.health = self.max_health
        self.experience_reward += 15
        self.damage += self.DAMAGE_INCREASE_AFTER_DEATH

    def lower_health_bar(self, damage_received: int or float):
        self.health_bar.width = self.HEALTH_BAR_LENGTH * ((self.health - damage_received) / self.max_health)

    def take_damage(self, damage_received: int or float):
        self.health -= damage_received

        if self.health <= 0:
            self.health = 0

    def take_experience_reward_on_kill(self):
        return self.experience_reward

    def get_image(self, index: int, images_left: list, images_right: list):
        if self.left_direction:
            return images_left[index]
        return images_right[index]

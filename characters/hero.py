from abc import abstractmethod, ABC

from pygame import transform, Rect, Surface


class Hero(ABC):
    __IMAGE_LOOP_SPEED = 0.25
    __ATK_SPEED = 0.2
    __MOVE_SPEED = 5
    BAR_LENGTH = 275

    EXP_BAR_LENGTH = 250
    MAX_LEVEL = 30

    def __init__(self, x: int, y: int, health: int, max_health: int, attack_images: list, die_image: Surface, idle_images: list,
                 jump_images: list, walk_images: list, profile_pic: object):
        self.x = x
        self.y = y
        self.level = 1

        self.max_health = max_health
        self.health = health

        self.attack_images_right = attack_images
        self.attack_images_left = [transform.flip(self.attack_images_right[i], True, False) for i in range(len(self.attack_images_right))]

        self.die_image = die_image

        self.idle_images_right = idle_images
        self.idle_images_left = [transform.flip(self.idle_images_right[i], True, False) for i in range((len(self.idle_images_right)))]

        self.jump_images = jump_images

        self.walk_images_right = walk_images
        self.walk_images_left = [transform.flip(self.walk_images_right[i], True, False) for i in range(len(self.walk_images_right))]

        self.profile_pic = profile_pic  # Surface object

        self.idle_index = 0
        self.on_press_index = 0

        self.is_attacking = False

        self.is_right_direction = True

        self.frame = self.make_bar(0, 0, 70, 70)

        self.experience_gained = 0

        self.experience_bar = self.make_bar(558, 630, 0, 35)
        self.experience_bar_pad = self.make_bar(558, 630, self.EXP_BAR_LENGTH, 35)

        self.health_bar = self.make_bar(self.frame.width, 0, self.BAR_LENGTH, 35)

        self.background_rect_health_bar = self.make_bar(self.frame.width, 0, self.BAR_LENGTH, 35)
        self.background_rect_mana_bar = self.make_bar(self.frame.width, 35, self.BAR_LENGTH, 35)

    @property
    def is_dead(self):
        return self.health <= 0

    @abstractmethod
    def get_stronger_after_level_up(self):
        pass

    @property
    def experience_per_level(self):
        level_exp = {}
        experience = 100
        for level in range(2, self.MAX_LEVEL + 1):
            level_exp[level] = experience
            experience += 200
        return level_exp

    @staticmethod
    def make_bar(x, y, width, height):
        return Rect(x, y, width, height)

    def lower_bar_width(self, current_value: int or float, max_value: int or float, extract_value: int or float):
        bar_width = self.BAR_LENGTH * ((current_value - extract_value) / max_value)

        if bar_width < 0:
            return 0
        return bar_width

    @staticmethod
    def increase_bar_width(current_value: int or float, max_value: int or float, add_value: int or float, BAR_LENGTH: int):
        bar_width = BAR_LENGTH * ((current_value + add_value) / max_value)

        if bar_width > BAR_LENGTH:
            return BAR_LENGTH
        return bar_width

    def increase_health_bar_width(self, heal_power: int or float):
        self.health_bar.width = self.increase_bar_width(self.health, self.max_health, heal_power, self.BAR_LENGTH)

    def check_health_limit(self):
        if self.health > self.max_health:
            self.health = self.max_health

    def receive_healing(self, amount: int or float):
        self.health += amount
        self.check_health_limit()

    def take_damage(self, damage: int):
        self.health_bar.width = self.lower_bar_width(self.health, self.max_health, damage)

        if self.health - damage > 0:
            self.health -= damage
        else:
            self.health = 0

    def idle_animation(self):
        self.idle_index += self.__IMAGE_LOOP_SPEED
        if self.is_right_direction:
            return self.idle_images_right[int(self.idle_index) % len(self.idle_images_right)]
        return self.idle_images_left[int(self.idle_index) % len(self.idle_images_left)]

    def walk_images(self):
        self.idle_index += self.__IMAGE_LOOP_SPEED
        if self.is_right_direction:
            return self.walk_images_right[int(self.idle_index) % len(self.walk_images_right)]
        return self.walk_images_left[int(self.idle_index) % len(self.walk_images_left)]

    def attack_animation(self):
        self.on_press_index += self.__ATK_SPEED

        if self.on_press_index >= len(self.attack_images_right):
            self.is_attacking = False
            self.on_press_index = 0

        if self.is_right_direction:
            return self.attack_images_right[int(self.on_press_index)]
        return self.attack_images_left[int(self.on_press_index)]

    def jump_animation(self):
        self.idle_index += self.__IMAGE_LOOP_SPEED
        return self.jump_images[int(self.idle_index) % len(self.jump_images)]

    def walk(self):
        if self.is_right_direction:
            self.x += self.__MOVE_SPEED
        else:
            self.x -= self.__MOVE_SPEED

    def get_hero_pos(self):
        return self.x, self.y

    def change_direction(self):
        if self.is_right_direction:
            self.is_right_direction = False
        else:
            self.is_right_direction = True

    def increase_experience_bar(self):
        width = self.EXP_BAR_LENGTH * (self.experience_gained / self.experience_per_level[self.level + 1])

        if width >= self.EXP_BAR_LENGTH:
            diff = abs(width - self.EXP_BAR_LENGTH)
            self.experience_bar.width = diff

        elif width < self.EXP_BAR_LENGTH:
            self.experience_bar.width = width

    def gain_experience(self, amount: int):
        self.experience_gained += amount

        if self.level + 1 not in self.experience_per_level:
            return

        self.increase_experience_bar()

        if self.experience_gained >= self.experience_per_level[self.level + 1]:
            self.experience_gained = abs(self.experience_per_level[self.level + 1] - self.experience_gained)
            self.level += 1
            self.get_stronger_after_level_up()

    def exp_until_next_level_percentage(self):
        if self.level + 1 not in self.experience_per_level:
            self.experience_bar.width = self.EXP_BAR_LENGTH
            return "100%"
        return f"{(self.experience_gained / self.experience_per_level[self.level + 1]) * 100:.1f}%"

from abc import ABC, abstractmethod
from pygame import transform, image
from random import randint


class Skill(ABC):
    MAP_WIDTH = 1366

    HEIGHT_OF_SKILL_ICON = 58

    def __init__(self, skill_cost: int, level_required: int):
        self.skill_cost = skill_cost
        self.level_required = level_required
        self.text_box = image.load('characters/skill_info_box/info_text_box.png')
        self.is_animating = False
        self.is_on_cooldown = False
        self.skill_level = 1

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def level_up(self):
        pass


class BlueBall(Skill):
    BALL_SPEED = 9
    DAMAGE_INCREASE_PER_LEVEL = 15
    MANA_COST_INCREASE_PER_LEVEL = 3
    LEVEL_REQUIRED = 1

    RIGHT_X_POS_FIXATION = 200
    BALL_Y_POS = 300

    LOCKED_COOLDOWN = 1

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/mage/skill_icons/blue_ball_skill_image.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.images_right = [image.load(f'characters/mage/skill_animations/blue_ball_sprites/{i}.png') for i in range(1, 6 + 1)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.y_pos = self.BALL_Y_POS
        self.img_index = 0
        self.damage = 25
        self.right_direction = None
        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            self.moving_the_ball()
            self.check_for_end_point()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        if self.right_direction:
            return self.images_right[int(self.img_index) % len(self.images_right)]
        return self.images_left[int(self.img_index) % len(self.images_left)]

    def moving_the_ball(self):
        if self.right_direction:
            self.x_pos += self.BALL_SPEED
        else:
            self.x_pos -= self.BALL_SPEED

        self.img_index += 0.2

    def check_for_end_point(self):
        if self.x_pos > self.MAP_WIDTH or self.x_pos < -self.images_right[0].get_rect().width:
            self.reset_skill_position()

    def reset_skill_position(self):
        self.img_index = 0
        self.is_animating = False
        self.right_direction = None

    def set_skill_pos(self, new_x_pos: int):
        if self.right_direction:
            self.x_pos = new_x_pos + self.RIGHT_X_POS_FIXATION
        else:
            self.x_pos = new_x_pos

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Blue Ball",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class HealAndMana(Skill):
    LEVEL_REQUIRED = 1
    HEAL_MANA_INCREASE_PER_LEVEL = 5

    LOCKED_COOLDOWN = 5

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/hp_mp_gain.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.healing = 20
        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def heal(self):
        self.is_on_cooldown = True
        return self.healing

    def level_up(self):
        self.skill_level += 1
        self.healing += self.HEAL_MANA_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal and Mana",
                f"Cost: {self.skill_cost} mana",
                f"Heal power: {self.healing}",
                f"Mana gain: {self.healing}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class Lightning(Skill):
    IMAGE_LOOP_SPEED = 0.2
    LEVEL_REQUIRED = 3
    DAMAGE_INCREASE_PER_LEVEL = 10
    MANA_COST_INCREASE_PER_LEVEL = 5

    HEIGHT_OF_SKILL_FIXATION = -30

    LOCKED_COOLDOWN = 3

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/thunderstorm_skill_icon.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.images = [image.load(f'characters/mage/skill_animations/thunder_sprites/{x}.png') for x in range(1, 9 + 1)]
        self.x_pos = None
        self.y_pos = self.HEIGHT_OF_SKILL_FIXATION
        self.img_index = 0
        self.damage = 30
        self.has_target = False
        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            self.release_lightning()
            self.check_for_end_point()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        return self.images[int(self.img_index)]

    def release_lightning(self):
        self.img_index += self.IMAGE_LOOP_SPEED

    def check_for_end_point(self):
        if int(self.img_index) >= len(self.images):
            self.reset_skill_position()

    def reset_skill_position(self):
        self.img_index = 0
        self.is_animating = False
        self.has_target = False

    def set_skill_pos(self, new_x_pos: int):
        if self.has_target:
            self.x_pos = new_x_pos
        else:
            self.x_pos = 1000

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Lightning",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class MeteorStrike(Skill):
    LEVEL_REQUIRED = 4
    DAMAGE_INCREASE_PER_LEVEL = 25
    MANA_COST_INCREASE_PER_LEVEL = 10

    METEOR_Y_START_LOCATION = -700
    METEOR_DROP_SPEED = 10
    IMAGE_LOOP_SPEED = 0.2
    REVERSE_IMAGE_LOOP_SPEED = 0.3

    LOCKED_COOLDOWN = 8

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/meteor_strike.jpg')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.images = [transform.scale(image.load(f'characters/mage/skill_animations/explosion_sprites/{x}.png'), (930, 630)) for x in range(13)]
        self.img_index = 0
        self.damage = 40

        self.x_pos = None
        self.y_pos = self.METEOR_Y_START_LOCATION

        self.explosion_y_target = -30

        self.has_target = False
        self.explosion_reached = False

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            if not self.check_if_explosion_reached():
                self.moving_the_meteor()

            elif not self.explosion_reached:
                self.release_explosion()
                self.check_for_end_point()

            elif self.explosion_reached:
                self.reverse_explosion()
                self.check_for_end_of_reversed_explosion()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        return self.images[int(self.img_index)]

    def moving_the_meteor(self):
        self.y_pos += self.METEOR_DROP_SPEED

    def release_explosion(self):
        self.img_index += self.IMAGE_LOOP_SPEED

    def reverse_explosion(self):
        self.img_index -= self.REVERSE_IMAGE_LOOP_SPEED

    def check_if_explosion_reached(self):
        return self.y_pos >= self.explosion_y_target

    def check_for_end_point(self):
        if int(self.img_index) >= len(self.images):
            self.explosion_reached = True
            self.set_img_index_for_reverse_explosion()

    def set_img_index_for_reverse_explosion(self):
        self.img_index = 9

    def check_for_end_of_reversed_explosion(self):
        # showing image 0 is very weird, that's why it's set to < 1
        if self.img_index < 1:
            self.reset_skill_position()

    def reset_skill_position(self):
        self.img_index = 0
        self.y_pos = self.METEOR_Y_START_LOCATION
        self.is_animating = False
        self.has_target = False
        self.explosion_reached = False

    def set_skill_pos(self, new_x_pos: int):
        if self.has_target:
            self.x_pos = new_x_pos - 400
        else:
            self.x_pos = 600

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Meteor Strike",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class AxeBasicAttack(Skill):
    DAMAGE_PER_LEVEL_INCREASE = 20
    LEVEL_REQUIRED = 1

    LOCKED_COOLDOWN = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/skill_icons/axe_basic_attack.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.damage = 25

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def gain_damage(self, amount: int or float):
        self.damage += amount

    def drop_damage(self, amount: int or float):
        self.damage -= amount

    def cast_skill(self):
        self.is_on_cooldown = True

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_PER_LEVEL_INCREASE

    def get_description(self):
        return ["Axe Attack",
                f"Cost: {self.skill_cost}",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class Heal(Skill):
    HEAL_INCREASE_PER_LEVEL = 20
    LEVEL_REQUIRED = 1

    LOCKED_COOLDOWN = 5

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/skill_icons/heal.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.healing = 25

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def heal(self):
        self.is_on_cooldown = True
        return self.healing

    def level_up(self):
        self.skill_level += 1
        self.healing += self.HEAL_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal",
                f"Cost: {self.skill_cost}",
                f"Heal power: {self.healing}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class DamageBoost(Skill):
    DAMAGE_BOOST_PER_LEVEL = 15
    LEVEL_REQUIRED = 3

    LOCKED_COOLDOWN = 5

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/war/skill_icons/damage_boost.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.damage_boost = 5

        self.cooldown_left = self.LOCKED_COOLDOWN

        self.is_clicked = False
        self.has_gained_damage = False

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.is_clicked = False
                self.has_gained_damage = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def check_if_consumed(self):
        if self.is_clicked and self.has_gained_damage:
            self.is_on_cooldown = True
            return True

    def cast_skill(self):
        self.is_clicked = True

    def set_boost_damage(self):
        self.has_gained_damage = True

    def unset_boost_damage(self):
        self.has_gained_damage = False

    def level_up(self):
        self.skill_level += 1
        self.damage_boost += self.DAMAGE_BOOST_PER_LEVEL

    def get_description(self):
        return ["Damage Boost",
                f"Cost: {self.skill_cost}",
                f"Damage boost: {self.damage_boost}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class PassiveCrit(Skill):
    PASSIVE_CRIT_INCREASE_PER_LEVEL = 5
    CRITICAL_DAMAGE_MULTIPLIER = 1.5
    MAX_CRIT_CHANCE = 100

    LEVEL_REQUIRED = 4

    LOCKED_COOLDOWN = 0

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/war/skill_icons/passive_crit.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.crit_chance = 5

        self.cooldown_left = self.LOCKED_COOLDOWN
        self.is_critical = False

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def check_for_critical_strike(self):
        if self.crit_chance >= randint(0, self.MAX_CRIT_CHANCE):
            self.switch_is_critical_state()
            return True
        return False

    def switch_is_critical_state(self):
        if self.is_critical:
            self.is_critical = False
        else:
            self.is_critical = True

    def get_critical_multiplier(self):
        return self.CRITICAL_DAMAGE_MULTIPLIER

    def level_up(self):
        if self.crit_chance + self.PASSIVE_CRIT_INCREASE_PER_LEVEL <= self.MAX_CRIT_CHANCE:
            self.crit_chance += self.PASSIVE_CRIT_INCREASE_PER_LEVEL
            self.skill_level += 1

    def get_description(self):
        return ["Passive",
                f"Chance to crit: {self.crit_chance}%",
                ]


class ArrowShot(Skill):
    ARROW_SPEED = 9
    DAMAGE_INCREASE_PER_LEVEL = 10
    MANA_INCREASE_PER_LEVEL = 3
    LEVEL_REQUIRED = 1

    RIGHT_ARROW_X_POS_FIXATION = 225
    ARROW_Y_POS = 400

    LOCKED_COOLDOWN = 1

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/hunt/skill_icons/arrow_shot.jpg')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()
        self.images_right = [image.load(f'characters/hunt/skill_animations/arrow_shot_sprites/{i}.png') for i in range(1, 5 + 1)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.y_pos = self.ARROW_Y_POS
        self.img_index = 0
        self.damage = 20
        self.right_direction = None

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            self.moving_the_arrow()
            self.check_for_end_point()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        if self.right_direction:
            return self.images_right[int(self.img_index) % len(self.images_right)]
        return self.images_left[int(self.img_index) % len(self.images_left)]

    def moving_the_arrow(self):
        if self.right_direction:
            self.x_pos += self.ARROW_SPEED
        else:
            self.x_pos -= self.ARROW_SPEED

        self.img_index += 0.2

    def check_for_end_point(self):
        if self.x_pos > self.MAP_WIDTH or self.x_pos < -self.images_right[0].get_rect().width:
            self.reset_skill_position()

    def reset_skill_position(self):
        self.img_index = 0
        self.is_animating = False
        self.right_direction = None

    def set_skill_pos(self, new_x_pos: int):
        if self.right_direction:
            self.x_pos = new_x_pos + self.RIGHT_ARROW_X_POS_FIXATION
        else:
            self.x_pos = new_x_pos

    def get_description(self):
        return [f"Arrow Shot",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_INCREASE_PER_LEVEL


class RapidShot(Skill):
    ARROW_SPEED = 9
    LEVEL_REQUIRED = 3
    DAMAGE_INCREASE_PER_LEVEL = 20
    MANA_COST_INCREASE_PER_LEVEL = 3

    RIGHT_ARROW_X_POS_FIXATION = 225
    ARROW_Y_POS = 400

    LOCKED_COOLDOWN = 3

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/hunt/skill_icons/rapid_shot.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()

        self.images_right = [image.load(f'characters/hunt/skill_animations/rapid_shot_sprites/{i}.png') for i in range(7)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.y_pos = self.ARROW_Y_POS
        self.img_index = 0
        self.damage = 35
        self.right_direction = None

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            self.moving_the_arrow()
            self.check_for_end_point()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        if self.right_direction:
            return self.images_right[int(self.img_index) % len(self.images_right)]
        return self.images_left[int(self.img_index) % len(self.images_left)]

    def moving_the_arrow(self):
        if self.right_direction:
            self.x_pos += self.ARROW_SPEED
        else:
            self.x_pos -= self.ARROW_SPEED

        self.img_index += 0.2

    def check_for_end_point(self):
        if self.x_pos > self.MAP_WIDTH or self.x_pos < -self.images_right[0].get_rect().width:
            self.reset_skill_position()

    def reset_skill_position(self):
        self.img_index = 0
        self.is_animating = False
        self.right_direction = None

    def set_skill_pos(self, new_x_pos: int):
        if self.right_direction:
            self.x_pos = new_x_pos + self.RIGHT_ARROW_X_POS_FIXATION
        else:
            self.x_pos = new_x_pos

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Rapid Shot",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]


class ArrowRain(Skill):
    ARROWS_FALL_SPEED = 10
    LEVEL_REQUIRED = 4
    DAMAGE_INCREASE_PER_LEVEL = 30
    MANA_COST_INCREASE_PER_LEVEL = 10

    IMAGE_LOOP_SPEED = 0.2

    MAX_ARROW_DROPS_COUNTER = 3

    ARROWS_Y_START_LOCATION = -200

    LOCKED_COOLDOWN = 8

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/hunt/skill_icons/ultimate_hunter.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.cooldown_rect = self.skill_icon.get_rect()

        self.images = [image.load(f'characters/hunt/skill_animations/arrow_rain/{x}.png') for x in range(10)]
        self.img_index = 0

        self.drop_counter = 0

        self.damage = 10

        self.x_pos = None
        self.y_pos = self.ARROWS_Y_START_LOCATION

        self.arrows_y_target = 350

        self.has_target = False

        self.cooldown_left = self.LOCKED_COOLDOWN

    def lower_icon_height(self, extract_value: int or float):
        if self.is_on_cooldown:
            self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON * ((self.cooldown_left - extract_value) / self.LOCKED_COOLDOWN)

    def lower_cooldown(self, amount_to_remove: int or float):
        if self.is_on_cooldown:
            self.cooldown_left -= amount_to_remove

            if self.cooldown_left <= 0:
                self.is_on_cooldown = False
                self.cooldown_rect.height = self.HEIGHT_OF_SKILL_ICON
                self.cooldown_left = self.LOCKED_COOLDOWN

    def animate(self):
        if self.is_animating:
            if not self.check_if_arrows_dropped():
                self.moving_the_arrows()

            elif self.check_if_arrows_dropped():
                self.increase_drop_counter()
                self.set_default_arrow_y_position()

        if self.check_for_max_arrow_drops():
            self.reset_skill_position()

    def cast_skill(self):
        self.is_on_cooldown = True
        self.is_animating = True

    def show_image(self):
        return self.images[int(self.img_index) % len(self.images)]

    def moving_the_arrows(self):
        self.y_pos += self.ARROWS_FALL_SPEED
        self.img_index += self.IMAGE_LOOP_SPEED

    def increase_drop_counter(self):
        self.drop_counter += 1

    def set_default_arrow_y_position(self):
        self.y_pos = self.ARROWS_Y_START_LOCATION
        self.img_index = 0

    def check_if_arrows_dropped(self):
        return self.y_pos >= self.arrows_y_target

    def check_for_max_arrow_drops(self):
        return self.drop_counter >= self.MAX_ARROW_DROPS_COUNTER

    def reset_skill_position(self):
        self.img_index = 0
        self.drop_counter = 0
        self.y_pos = self.ARROWS_Y_START_LOCATION
        self.x_pos = None
        self.is_animating = False
        self.has_target = False

    def set_skill_pos(self, new_x_pos: int):
        if self.has_target:
            self.x_pos = new_x_pos
        else:
            self.x_pos = 950

    def level_up(self):
        self.skill_level += 1
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Arrow Rain",
                f"Cost: {self.skill_cost} mana",
                f"Damage per hit: {self.damage}",
                f"Cooldown: {self.LOCKED_COOLDOWN} secs"
                ]

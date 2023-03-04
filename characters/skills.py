from abc import ABC, abstractmethod
from pygame import transform, image


class Skill(ABC):
    MAP_WIDTH = 1366

    def __init__(self, skill_cost: int, level_required: int):
        self.skill_cost = skill_cost
        self.level_required = level_required
        self.text_box = image.load('characters/skill_info_box/info_text_box.png')
        self.is_animating = False

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def level_up(self):
        pass


class BlueBall(Skill):
    BALL_SPEED = 9
    DAMAGE_INCREASE_PER_LEVEL = 5
    MANA_COST_INCREASE_PER_LEVEL = 5
    LEVEL_REQUIRED = 1

    RIGHT_X_POS_FIXATION = 200
    BALL_Y_POS = 300

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/mage/skill_icons/blue_ball_skill_image.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.images_right = [image.load(f'characters/mage/skill_animations/blue_ball_sprites/{i}.png') for i in range(1, 6 + 1)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.y_pos = self.BALL_Y_POS
        self.img_index = 0
        self.damage = 25
        self.right_direction = None

    def animate(self):
        if self.is_animating:
            self.moving_the_ball()
            self.check_for_end_point()

    def cast_skill(self):
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
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Blue Ball",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}"
                ]


class HealAndMana(Skill):
    LEVEL_REQUIRED = 2
    HEAL_MANA_INCREASE_PER_LEVEL = 10

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/hp_mp_gain.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += self.HEAL_MANA_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal and Mana",
                f"Cost: {self.skill_cost} mana",
                f"Heal power: {self.healing}",
                f"Mana gain: {self.healing}"
                ]


class Lightning(Skill):
    IMAGE_LOOP_SPEED = 0.2
    LEVEL_REQUIRED = 3
    DAMAGE_INCREASE_PER_LEVEL = 10
    MANA_COST_INCREASE_PER_LEVEL = 5

    HEIGHT_OF_SKILL_FIXATION = -30

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/thunderstorm_skill_icon.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.images = [image.load(f'characters/mage/skill_animations/thunder_sprites/{x}.png') for x in range(1, 9 + 1)]
        self.x_pos = None
        self.y_pos = self.HEIGHT_OF_SKILL_FIXATION
        self.img_index = 0
        self.damage = 30
        self.has_target = False

    def animate(self):
        if self.is_animating:
            self.release_lightning()
            self.check_for_end_point()

    def cast_skill(self):
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
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Lightning",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}"
                ]


class MeteorStrike(Skill):
    LEVEL_REQUIRED = 4
    DAMAGE_INCREASE_PER_LEVEL = 10
    MANA_COST_INCREASE_PER_LEVEL = 5

    METEOR_Y_START_LOCATION = -700
    METEOR_DROP_SPEED = 10
    IMAGE_LOOP_SPEED = 0.2
    REVERSE_IMAGE_LOOP_SPEED = 0.3

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/mage/skill_icons/meteor_strike.jpg')
        self.rect_icon = self.skill_icon.get_rect()
        self.images = [transform.scale(image.load(f'characters/mage/skill_animations/explosion_sprites/{x}.png'), (930, 630)) for x in range(13)]
        self.img_index = 0
        self.damage = 40

        self.x_pos = None
        self.y_pos = self.METEOR_Y_START_LOCATION

        self.explosion_y_target = -30

        self.has_target = False
        self.explosion_reached = False

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
            self.x_pos = new_x_pos
        else:
            self.x_pos = 600

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Meteor Strike",
                f"Cost: {self.skill_cost} mana",
                f"Damage: {self.damage}"
                ]


class AxeBasicAttack(Skill):
    DAMAGE_PER_LEVEL_INCREASE = 5
    LEVEL_REQUIRED = 1

    # should add the basic attack of warrior images here
    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/skill_icons/axe_basic_attack.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.damage = 25

    def level_up(self):
        self.damage += self.DAMAGE_PER_LEVEL_INCREASE

    def get_description(self):
        return ["Axe Attack",
                f"Cost: {self.skill_cost}",
                f"Damage: {self.damage}"]


class Heal(Skill):
    HEAL_INCREASE_PER_LEVEL = 5
    LEVEL_REQUIRED = 1

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)
        self.skill_icon = image.load('characters/war/skill_icons/heal.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.healing = 25

    def heal(self):
        return self.healing

    def level_up(self):
        self.healing += self.HEAL_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Heal",
                f"Cost: {self.skill_cost}",
                f"Heal power: {self.healing}"
                ]


class DamageBoost(Skill):
    DAMAGE_BOOST_PER_LEVEL = 5
    LEVEL_REQUIRED = 3

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/war/skill_icons/damage_boost.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.damage_boost = 5

    def level_up(self):
        self.damage_boost += self.DAMAGE_BOOST_PER_LEVEL

    def get_description(self):
        return ["Damage Boost",
                f"Cost: {self.skill_cost}",
                f"Damage boost: {self.damage_boost}",
                ]


class PassiveCrit(Skill):
    PASSIVE_CRIT_INCREASE_PER_LEVEL = 5
    MAX_CRIT_CHANCE = 100

    LEVEL_REQUIRED = 4

    def __init__(self):
        super().__init__(0, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/war/skill_icons/passive_crit.png')
        self.rect_icon = self.skill_icon.get_rect()
        self.crit_chance = 5  # must work with random method like this - if self.crit_chance >= random.randint(0, 100)

    def level_up(self):
        if self.crit_chance + self.PASSIVE_CRIT_INCREASE_PER_LEVEL <= self.MAX_CRIT_CHANCE:
            self.crit_chance += self.PASSIVE_CRIT_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Passive",
                f"Chance to crit: {self.crit_chance}%"
                ]


class ArrowShot(Skill):
    ARROW_SPEED = 9
    DAMAGE_INCREASE_PER_LEVEL = 5
    MANA_INCREASE_PER_LEVEL = 5
    LEVEL_REQUIRED = 1

    RIGHT_ARROW_X_POS_FIXATION = 225
    ARROW_Y_POS = 400

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/hunt/skill_icons/arrow_shot.jpg')
        self.rect_icon = self.skill_icon.get_rect()
        self.images_right = [image.load(f'characters/hunt/skill_animations/arrow_shot_sprites/{i}.png') for i in range(1, 5 + 1)]
        self.images_left = [transform.flip(self.images_right[i], True, False) for i in range(len(self.images_right))]
        self.x_pos = 0
        self.y_pos = self.ARROW_Y_POS
        self.img_index = 0
        self.damage = 20
        self.right_direction = None

    def animate(self):
        if self.is_animating:
            self.moving_the_arrow()
            self.check_for_end_point()

    def cast_skill(self):
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
                f"Damage: {self.damage}"
                ]

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_INCREASE_PER_LEVEL


class ArrowRain(Skill):
    LEVEL_REQUIRED = 4
    DAMAGE_INCREASE_PER_LEVEL = 5
    MANA_COST_INCREASE_PER_LEVEL = 5

    def __init__(self, skill_cost: int):
        super().__init__(skill_cost, self.LEVEL_REQUIRED)

        self.skill_icon = image.load('characters/hunt/skill_icons/ultimate_hunter.png')
        self.rect_icon = self.skill_icon.get_rect()

        self.damage = 10

    def level_up(self):
        self.damage += self.DAMAGE_INCREASE_PER_LEVEL
        self.skill_cost += self.MANA_COST_INCREASE_PER_LEVEL

    def get_description(self):
        return ["Arrow Rain",
                f"Cost: {self.skill_cost} mana",
                f"Damage per hit: {self.damage}"
                ]

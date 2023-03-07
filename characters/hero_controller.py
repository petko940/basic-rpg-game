from typing import Dict

from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
import pygame

pygame.font.init()

resized = 1.4

font = pygame.font.SysFont('Cosmic Sans bold', 40)
level_font = pygame.font.SysFont('Cosmic Sans', 25)
cooldown_font = pygame.font.SysFont('Cosmic Sans bold', 60)


class HeroController:
    HEALTH_BAR_COLOR = (180, 0, 0)
    MANA_BAR_COLOR = (0, 0, 220)

    BACKGROUND_BAR_COLOR = (105, 105, 105)

    HERO_FRAME_COLOR = (98, 0, 0)

    FONT_COLOR = (255, 255, 255)

    PROFILE_FRAME_THICKNESS = 5

    BLACK_COLOR = (0, 0, 0)

    LOCKED_SKILL_COLOR_AND_TRANSPARENCY = (150, 150, 150, 150)   # last value is transparency

    COOLDOWN_SECONDS_COLOR = (220, 0, 0)

    def __init__(self):
        self.heroes: Dict[str: object] = {}
        self.skill_to_use = None

    @property
    def valid_heroes(self):
        return {"Warrior": Warrior, "Mage": Mage, "Hunter": Hunter}

    @property
    def get_load_funcs(self):
        return {"Warrior": self.load_warrior_images, "Mage": self.load_mage_images, "Hunter": self.load_hunter_images}

    def create_hero(self, hero_type: str, x_pos: int, y_pos: int):
        if hero_type in self.valid_heroes:
            loaded_images = self.get_load_funcs[hero_type.capitalize()]()

            new_hero = self.valid_heroes[hero_type.capitalize()](x_pos, y_pos, *loaded_images)

            self.heroes[hero_type.capitalize()] = self.heroes.get(hero_type.capitalize(), new_hero)

            print(f"hero of type {type(new_hero)} has been added")

    def get_hero_object(self, hero_name: str):
        """
        returns hero as object and if not found, returns "Not Found"
        """
        return self.heroes.get(hero_name.capitalize(), "Not Found")

    @staticmethod
    def mana_regen(hero: (Warrior, Mage, Hunter)):
        if type(hero).__name__ != "Warrior":
            hero.receive_mana(hero.MANA_REGEN_PER_SECOND)
            hero.increase_mana_bar_width(hero.MANA_REGEN_PER_SECOND)

    @staticmethod
    def lower_skill_cooldown(hero: (Warrior, Mage, Hunter), amount: int or float):
        for skill in hero.skills.values():
            skill.lower_icon_height(amount)  # it is very important that this is executed first
            skill.lower_cooldown(amount)

    def use_skill(self, hero: (Warrior, Hunter, Mage), screen):
        if type(hero).__name__ in "Mage":
            self.use_mage_skills(hero, screen)

        elif type(hero).__name__ == "Warrior":
            self.use_warrior_skills(hero)

        elif type(hero).__name__ == "Hunter":
            self.use_hunter_skills(hero, screen)

    def use_warrior_skills(self, hero: Warrior):
        skill = hero.skills.get(self.skill_to_use, False)

        if skill:

            if not hero.is_attacking or skill.is_on_cooldown:
                self.skill_to_use = None

            if not skill.is_on_cooldown:

                if type(skill).__name__ == "Heal":
                    hero.increase_health_bar_width(skill.heal())
                    hero.receive_healing(skill.heal())

                if type(skill).__name__ == "AxeBasicAttack":
                    skill.cast_skill()

                    # TO DO
                    # MUST CHECK FOR COLLISION HERE

                    damage_boost_skill = hero.skills[3]
                    if damage_boost_skill.check_if_consumed():
                        skill.drop_damage(damage_boost_skill.damage_boost)

                    hero.is_attacking = True

                if type(skill).__name__ == "DamageBoost":
                    skill.cast_skill()

                    axe_attack_skill = hero.skills[1]
                    axe_attack_skill.gain_damage(skill.damage_boost)

    def use_mage_skills(self, hero: Mage, screen):
        for c_skill in hero.skills.values():
            if c_skill.is_animating and type(c_skill).__name__ != "HealAndMana":
                screen.blit(c_skill.show_image(), (c_skill.x_pos, c_skill.y_pos))

                c_skill.animate()

        skill = hero.skills.get(self.skill_to_use, False)

        if skill:

            if skill.is_animating or not hero.check_enough_mana_to_cast(skill.skill_cost) or skill.is_on_cooldown:
                self.skill_to_use = None
                hero.is_attacking = False

            if not skill.is_on_cooldown and hero.check_enough_mana_to_cast(skill.skill_cost):

                if type(skill).__name__ == "HealAndMana":
                    hero.increase_health_bar_width(skill.heal())
                    hero.increase_mana_bar_width(skill.heal())

                    hero.receive_mana(skill.heal())
                    hero.receive_healing(skill.heal())

                if not skill.is_animating and type(skill).__name__ != "HealAndMana":
                    skill.right_direction = hero.is_right_direction

                    skill.set_skill_pos(hero.x)
                    skill.cast_skill()
                    hero.is_attacking = True

                    hero.decrease_mana_bar_width(skill.skill_cost)
                    hero.consume_mana_on_skill(skill.skill_cost)

                self.skill_to_use = None

    def use_hunter_skills(self, hero: Hunter, screen):
        for c_skill in hero.skills.values():
            if c_skill.is_animating and type(c_skill).__name__ != "HealAndMana":
                screen.blit(c_skill.show_image(), (c_skill.x_pos, c_skill.y_pos))

                c_skill.animate()

        skill = hero.skills.get(self.skill_to_use, False)

        if skill:

            if skill.is_animating or not hero.check_enough_mana_to_cast(skill.skill_cost) or skill.is_on_cooldown:
                self.skill_to_use = None
                hero.is_attacking = False

            if not skill.is_on_cooldown and hero.check_enough_mana_to_cast(skill.skill_cost):

                if type(skill).__name__ == "HealAndMana":
                    hero.increase_health_bar_width(skill.heal())
                    hero.increase_mana_bar_width(skill.heal())

                    hero.receive_mana(skill.heal())
                    hero.receive_healing(skill.heal())

                if not skill.is_animating and type(skill).__name__ != "HealAndMana":
                    skill.right_direction = hero.is_right_direction

                    skill.set_skill_pos(hero.x)
                    skill.cast_skill()
                    hero.is_attacking = True

                    hero.decrease_mana_bar_width(skill.skill_cost)
                    hero.consume_mana_on_skill(skill.skill_cost)

                self.skill_to_use = None

    @staticmethod
    def take_damage(hero: (Warrior, Hunter, Mage), monster: object) -> None:
        # this method is not working since there are still NO monster objects
        """
        Gets the hero health_bar and goes into the method (lower bar width) which is inside the Hero class.
        lower_bar_width returns the new health_bar width and take_damage method applies the changes
        THIS METHOD must be used hand by hand with check_if_hero_died
        """
        hero.health_bar.width = hero.lower_bar_width(hero.health, hero.max_health, monster.damage)
        if hero.health - monster.damage > 0:
            hero.health -= monster.damage
        else:
            hero.health = 0

    def display_skill_icons(self, screen, hero: (Warrior, Hunter, Mage), x_pos: int, y_pos: int):
        """
        x_y_offset is the pixels fixation to perfectly fit inside the action bar

        x_pos is increasing so the images don't overlap

        setting the rect_icon x and y positions, because they are not set by default
        this is helping for show_skill_info descriptions.
        It works very good since you can't hover the mouse before the skills are being shown on screen and there is no
        chance for a problem to occur
        """

        def draw_rect_alpha(color, rect: pygame.Rect):
            """
            displays semi transparent image above the skill icon that is higher level than the hero level
            """
            surface = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
            pygame.draw.rect(surface, color, surface.get_rect())
            screen.blit(surface, rect)

        def cooldown_seconds_counter(seconds_remaining, icon: pygame.Rect):
            seconds_surface = cooldown_font.render(f"{seconds_remaining:.0f}" if seconds_remaining > 1
                                                   else f"{seconds_remaining:.1f}", True, self.COOLDOWN_SECONDS_COLOR)

            middle_of_skill_icon = (icon.width // 2) - (seconds_surface.get_width() // 2) + icon.x
            middle_of_y_position = (icon.height // 2) - (seconds_surface.get_height() // 2) + icon.y

            screen.blit(seconds_surface, (middle_of_skill_icon, middle_of_y_position))

        icon_width, space_between_icons, x_y_offset = 57, 5, 4
        for skill in hero.skills.values():
            screen.blit(skill.skill_icon, (x_pos + x_y_offset, y_pos + x_y_offset))

            if not skill.rect_icon.x or not skill.cooldown_rect.x:
                skill.rect_icon.x, skill.rect_icon.y = x_pos + x_y_offset, y_pos + x_y_offset
                skill.cooldown_rect.x, skill.cooldown_rect.y = x_pos + x_y_offset, y_pos + x_y_offset

            # if hero.level < skill.LEVEL_REQUIRED:
            #     draw_rect_alpha(self.LOCKED_SKILL_COLOR_AND_TRANSPARENCY, skill.rect_icon)

            if type(skill).__name__ == "DamageBoost" and skill.is_clicked:
                draw_rect_alpha(self.LOCKED_SKILL_COLOR_AND_TRANSPARENCY, skill.cooldown_rect)

            if skill.is_on_cooldown:
                draw_rect_alpha(self.LOCKED_SKILL_COLOR_AND_TRANSPARENCY, skill.cooldown_rect)
                cooldown_seconds_counter(skill.cooldown_left, skill.rect_icon)

            x_pos += icon_width + space_between_icons

    def show_skill_description(self, screen, hero: (Warrior, Hunter, Mage), mouse_pos: tuple):
        space_between_lines = 15

        space_between_mouse_and_text_box = 10

        pixels_above_mouse = 100

        text_inside_y_pos = pixels_above_mouse - 10
        text_inside_x_pos = space_between_mouse_and_text_box * 2

        for skill in hero.skills.values():
            if skill.rect_icon.collidepoint(mouse_pos):
                mouse_x_pos, mouse_y_pos = mouse_pos
                screen.blit(skill.text_box, (mouse_x_pos + space_between_mouse_and_text_box, mouse_y_pos - pixels_above_mouse))

                for sentence in skill.get_description():
                    text_surface = level_font.render(sentence, True, self.FONT_COLOR)
                    text_x_pos, text_y_pos = mouse_x_pos + text_inside_x_pos, mouse_y_pos - text_inside_y_pos

                    screen.blit(text_surface, (text_x_pos, text_y_pos))

                    # increasing this, so it makes a new line to display the next sentence
                    # also it is needed so the text doesn't overlap
                    mouse_y_pos += space_between_lines

    def display_health_and_mana_bars(self, screen, hero: (Warrior, Hunter, Mage)):
        # drawing the base health bar on screen
        pygame.draw.rect(screen, self.BACKGROUND_BAR_COLOR, hero.background_rect_health_bar)
        # drawing the actual health bar above the base health bar
        pygame.draw.rect(screen, self.HEALTH_BAR_COLOR, hero.health_bar)
        # everyone except warrior has mana bar
        if type(hero).__name__ != "Warrior":
            # drawing the base mana bar on screen
            pygame.draw.rect(screen, self.BACKGROUND_BAR_COLOR, hero.background_rect_mana_bar)
            # drawing the actual mana bar above the base mana bar
            pygame.draw.rect(screen, self.MANA_BAR_COLOR, hero.mana_bar)

    @staticmethod
    def check_if_hero_died(hero: (Warrior, Hunter, Mage)) -> bool:
        """
        returns True if the health is less than or equal to zero, otherwise returns False
        """
        return hero.health <= 0

    def display_health_and_mana_stats(self, screen, hero: (Warrior, Hunter, Mage)):
        # creating health surface
        health_surface = font.render(f"{hero.health}/{hero.max_health}", True, self.FONT_COLOR)

        # finding the middle of the health bar
        middle_of_hp_bar = (hero.BAR_LENGTH // 2) - (health_surface.get_rect().width // 2) + hero.frame.width

        # displaying the health surface
        screen.blit(health_surface, (middle_of_hp_bar, 5))
        if type(hero).__name__ != "Warrior":
            # creating mana surface
            mana_surface = font.render(f"{hero.mana}/{hero.max_mana}", True, self.FONT_COLOR)

            # finding the middle of the mana bar, we can't use the same result of middle_of_hp_bar, because
            # you can have 500 health and 2000 mana and that's when you will get bad centering position
            middle_of_mana_bar = (hero.BAR_LENGTH // 2) - (mana_surface.get_rect().width // 2) + hero.frame.width

            # displaying the mana surface on screen
            screen.blit(mana_surface, (middle_of_mana_bar, 40))

    def display_hero_frame_and_level(self, screen, hero: (Warrior, Hunter, Mage)):
        # making the hero profile frame
        pygame.draw.rect(screen, self.HERO_FRAME_COLOR, hero.frame, self.PROFILE_FRAME_THICKNESS)
        # displaying the image inside the hero profile frame
        screen.blit(hero.profile_pic,
                    (hero.frame.x + self.PROFILE_FRAME_THICKNESS, hero.frame.y + self.PROFILE_FRAME_THICKNESS))

        # drawing a circle
        pygame.draw.circle(screen, self.HERO_FRAME_COLOR, (10, 10), 15)
        # drawing the frame around the circle (black color), (x, y), radius(15), line thickness(4) - grows inwards
        pygame.draw.circle(screen, self.BLACK_COLOR, (12, 12), 15, 4)

        # creating surface so it can be displayed on screen
        level_surface = level_font.render(str(hero.level), True, self.FONT_COLOR)

        # finding the middle of the circle. The width of the circle is 25 and i don't think it will be changed
        middle_of_circle = (25 // 2) - (level_surface.get_rect().width // 2)
        # displaying the level surface inside the frame of the circle
        screen.blit(level_surface, (middle_of_circle, 4))

    @staticmethod
    def load_warrior_images():
        attack_images = [pygame.transform.scale(pygame.image.load(f'characters/war/attack/{i}.png'),
                                                (580 / resized, 520 / resized)) for i in range(1, 8)]

        die_image = pygame.transform.scale(pygame.image.load(f'characters/war/die/1.png'),
                                           (765 / resized, 615 / resized))

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/war/idle/({i}).png'),
                                              (580 / resized, 520 / resized)) for i in range(1, 11)]

        jump_images = [pygame.transform.scale(pygame.image.load(f'characters/war/jump/({i}).png'),
                                              (703 / resized, 678 / resized)) for i in range(1, 11)]

        walk_images = [pygame.transform.scale(pygame.image.load(f'characters/war/walk/({i}).png'),
                                              (610 / resized, 555 / resized)) for i in range(1, 11)]

        profile_picture = pygame.image.load(f'characters/war/warrior_profile.png')

        return attack_images, die_image, idle_images, jump_images, walk_images, profile_picture

    @staticmethod
    def load_mage_images():
        attack_images = [pygame.transform.scale(pygame.image.load(f'characters/mage/attack/({i}).png'),
                                                (466 / resized, 561 / resized)) for i in range(1, 8)]

        die_image = pygame.transform.scale(pygame.image.load(f'characters/mage/die/1.png'),
                                           (671 / resized, 550 / resized))

        idle_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/idle/({i}).png'), (466 / resized, 535 / resized))
            for i in range(1, 11)]

        jump_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/jump/({i}).png'), (478 / resized, 675 / resized))
            for i in range(1, 11)]

        walk_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/walk/({i}).png'), (467 / resized, 561 / resized))
            for i in range(1, 11)]

        profile_picture = pygame.image.load(f'characters/mage/mage_profile.png')

        return attack_images, die_image, idle_images, jump_images, walk_images, profile_picture

    @staticmethod
    def load_hunter_images():
        attack_images = [pygame.transform.scale(pygame.image.load(f'characters/hunt/attack/{i}.png'), (547 / resized, 556 / resized)) for i in range(6)]

        die_image = pygame.transform.scale(pygame.image.load(f'characters/hunt/die/1.png'), (554 / resized, 550 / resized))

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/hunt/idle/({i}).png'), (483 / resized, 550 / resized)) for i in range(1, 11)]

        jump_images = [pygame.transform.scale(pygame.image.load(f'characters/hunt/jump/({i}).png'), (527 / resized, 618 / resized)) for i in range(1, 11)]

        walk_images = [pygame.transform.scale(pygame.image.load(f'characters/hunt/walk/({i}).png'), (458 / resized, 539 / resized)) for i in range(1, 11)]

        profile_picture = pygame.image.load(f'characters/hunt/hunter_profile.png')

        return attack_images, die_image, idle_images, jump_images, walk_images, profile_picture

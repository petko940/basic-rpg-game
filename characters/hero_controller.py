from characters.hunter_character import Hunter
from characters.mage_character import Mage
from characters.warrior_character import Warrior
import pygame

pygame.font.init()

resized = 1.4

font = pygame.font.SysFont('Cosmic Sans bold', 40)
level_font = pygame.font.SysFont('Cosmic Sans', 25)
description_font = pygame.font.SysFont('Cosmic Sans', 25)


class HeroController:
    HEALTH_BAR_COLOR = (180, 0, 0)
    MANA_BAR_COLOR = (0, 0, 220)

    BACKGROUND_BAR_COLOR = (105, 105, 105)

    HERO_FRAME_COLOR = (98, 0, 0)

    FONT_COLOR = (255, 255, 255)

    PROFILE_FRAME_THICKNESS = 5

    BLACK_COLOR = (0, 0, 0)

    def __init__(self):
        self.heroes: dict[str, object] = {}

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

    # method to display all skill icons
    @staticmethod
    def display_skill_icons(screen, hero: (Warrior, Hunter, Mage), x_pos: int, y_pos: int):
        """
        x_y_offset is the pixels fixation to perfectly fit inside the action bar

        x_pos is increasing so the images don't overlap

        setting the rect_icon x and y positions, because they are not set by default
        this is helping for show_skill_info descriptions.
        It works very good since you can't hover the mouse before the skills are being shown on screen and there is no
        chance for a problem to occur
        """
        icon_width, space_between_icons, x_y_offset = 57, 5, 4
        for value in hero.skills.values():
            if not isinstance(value, str):
                screen.blit(value.skill_icon, (x_pos + x_y_offset, y_pos + x_y_offset))
                value.rect_icon.x, value.rect_icon.y = x_pos + x_y_offset, y_pos + x_y_offset

            x_pos += icon_width + space_between_icons

    def show_skill_description(self, screen, hero: (Warrior, Hunter, Mage), mouse_pos: tuple, action_bar_x_pos: int, action_bar_y_pos, action_bar_width: int):
        space_between_lines = 15
        space_between_action_bar_and_text_box = 30

        pixels_inside_text_box = 10

        for value in hero.skills.values():
            # this if statement will be here until we add all the spells
            if not isinstance(value, str):
                if value.rect_icon.collidepoint(mouse_pos):
                    x_pos = action_bar_x_pos + action_bar_width + space_between_action_bar_and_text_box
                    screen.blit(value.text_box, (x_pos, action_bar_y_pos))

                    for sentence in value.get_description():
                        text_surface = description_font.render(sentence, True, self.FONT_COLOR)
                        text_x_pos = action_bar_x_pos + action_bar_width + space_between_action_bar_and_text_box + pixels_inside_text_box
                        screen.blit(text_surface, (text_x_pos, action_bar_y_pos + pixels_inside_text_box))

                        action_bar_y_pos += space_between_lines

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
        screen.blit(hero.profile_pic, (hero.frame.x + self.PROFILE_FRAME_THICKNESS, hero.frame.y + self.PROFILE_FRAME_THICKNESS))

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

        die_images = [pygame.transform.scale(pygame.image.load(f'characters/war/die/({i}).png'),
                                             (668 / resized, 540 / resized)) for i in range(1, 11)]

        idle_images = [pygame.transform.scale(pygame.image.load(f'characters/war/idle/({i}).png'),
                                              (580 / resized, 520 / resized)) for i in range(1, 11)]

        jump_images = [pygame.transform.scale(pygame.image.load(f'characters/war/jump/({i}).png'),
                                              (703 / resized, 678 / resized)) for i in range(1, 11)]

        walk_images = [pygame.transform.scale(pygame.image.load(f'characters/war/walk/({i}).png'),
                                              (610 / resized, 555 / resized)) for i in range(1, 11)]

        profile_picture = pygame.image.load(f'characters/war/warrior_profile.png')

        return attack_images, die_images, idle_images, jump_images, walk_images, profile_picture

    @staticmethod
    def load_mage_images():
        attack_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/attack/({i}).png'),
                                   (466 / resized, 561 / resized)) for i in
            range(1, 8)]

        die_images = [
            pygame.transform.scale(pygame.image.load(f'characters/mage/die/({i}).png'), (671 / resized, 550 / resized))
            for
            i in range(1, 10)]

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

        return attack_images, die_images, idle_images, jump_images, walk_images, profile_picture

    @staticmethod
    def load_hunter_images():
        attack_images = [pygame.image.load(f'characters/hunt/attack/({i}).png') for i in range(1, 11)]

        die_images = [pygame.image.load(f'characters/hunt/die/({i}).png') for i in range(1, 11)]

        idle_images = [
            pygame.transform.scale(pygame.image.load(f'characters/hunt/idle/({i}).png'), (483 / resized, 550 / resized))
            for i in range(1, 11)]

        jump_images = [pygame.image.load(f'characters/hunt/jump/({i}).png') for i in range(1, 11)]

        walk_images = [pygame.image.load(f'characters/hunt/walk/({i}).png') for i in range(1, 11)]

        profile_picture = pygame.image.load(f'characters/hunt/hunter_profile.png')

        return attack_images, die_images, idle_images, jump_images, walk_images, profile_picture

import pygame
from music import music
from fullscreen_windowed import full_screen, windowed

pygame.mixer.init()
WIDTH, HEIGHT = (1366, 768)
resized = 1920 / WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Menu:
    arrow = [pygame.transform.scale(pygame.image.load(f'images/menu/arrow/({i}).png'), (150 / resized, 150 / resized))
             for i in range(1, 9)]
    arrow_pos = ((225 / resized, 80 / resized), (900 / resized, 80 / resized), ((790 + 740) / resized, 80 / resized))

    music('images/menu/music.mp3')

    buttons_x, buttons_y = (1920 / 2 - 100) / resized, (1080 / 1.01 - 210) / resized
    menu_image = pygame.transform.scale(pygame.image.load('images/menu/make_character.jpg'), (WIDTH, HEIGHT))
    menu_image_rect = menu_image.get_rect()

    button_play = pygame.transform.scale(pygame.image.load('images/menu/play.png'), (270 / resized, 100 / resized))
    button_play_rect = button_play.get_rect()
    button_play_rect.x = buttons_x
    button_play_rect.y = buttons_y

    fake_start = pygame.transform.scale(pygame.image.load('images/menu/fake_start.png'), (270 / resized, 100 / resized))

    button_quit = pygame.transform.scale(pygame.image.load('images/menu/exit.png'), (270 / resized, 100 / resized))
    button_quit_rect = button_quit.get_rect()
    button_quit_rect.x = buttons_x
    button_quit_rect.y = buttons_y + 80

    is_full_screen = False

    button_full_screen = pygame.transform.scale(pygame.image.load('images/menu/fullscreen_button.png'),
                                                (500 / resized, 100 / resized))

    button_full_screen_rect = button_full_screen.get_rect()
    button_full_screen_rect.x = buttons_x + 400
    button_full_screen_rect.y = buttons_y - 600

    button_windowed = pygame.transform.scale(pygame.image.load('images/menu/windowed_button.png'),
                                             (500 / resized, 100 / resized))
    button_windowed_rect = button_windowed.get_rect()
    button_windowed_rect.x = buttons_x + 400
    button_windowed_rect.y = buttons_y - 600

    platform = pygame.transform.scale(pygame.image.load('images/menu/platform.png'), (500 / resized, 320 / resized))
    new_platform = pygame.transform.scale(pygame.image.load('images/menu/new_platform.png'), (500 / resized, 430 ))
    heroes_x_y = [(120 / resized, 240 / resized), (790 / resized, 240 / resized),
                  ((790 + 630) / resized, 240 / resized)]

    war_surface = pygame.Surface((580 / resized, 520 / resized))  # hardcoded
    warrior_rect = war_surface.get_rect()
    warrior_rect.x = heroes_x_y[0][0]
    warrior_rect.y = heroes_x_y[0][1]

    mage_surface = pygame.Surface((580 / resized, 520 / resized))  # hardcoded
    mage_rect = mage_surface.get_rect()
    mage_rect.x = heroes_x_y[1][0]
    mage_rect.y = heroes_x_y[1][1]

    hunter_surface = pygame.Surface((580 / resized, 520 / resized))  # hardcoded
    hunter_rect = hunter_surface.get_rect()
    hunter_rect.x = heroes_x_y[2][0]
    hunter_rect.y = heroes_x_y[2][1]

    selected = {"Warrior": False, "Mage": False, "Hunter": False}

    index = 0
    see_arrow = arrow[int(index) % len(arrow)]

    class_names = ["Warrior", "Mage", "Hunter"]

    is_ready_to_start = False

    def __init__(self, warrior: object, mage: object, hunter: object):
        self.main_menu = True
        self.warrior = warrior
        self.mage = mage
        self.hunter = hunter
        self.chosen_hero = ''

    @property
    def get_current_hero(self):
        return {"Warrior": self.warrior, "Mage": self.mage, "Hunter": self.hunter}

    def menu(self, ):
        while self.main_menu:
            screen.blit(self.menu_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.button_full_screen_rect.collidepoint(mouse_pos) and not self.is_full_screen:
                        full_screen()
                        self.is_full_screen = True
                    elif self.button_windowed_rect.collidepoint(mouse_pos):
                        windowed()
                        self.is_full_screen = False

                    if self.warrior_rect.collidepoint(mouse_pos):
                        self.selected['Warrior'] = True
                        self.selected['Mage'] = False
                        self.selected['Hunter'] = False
                        self.button_play_rect.x = 150 / resized

                    elif self.mage_rect.collidepoint(mouse_pos):
                        self.selected['Warrior'] = False
                        self.selected['Mage'] = True
                        self.selected['Hunter'] = False
                        self.button_play_rect.x = self.buttons_x

                    elif self.hunter_rect.collidepoint(mouse_pos):
                        self.selected['Warrior'] = False
                        self.selected['Mage'] = False
                        self.selected['Hunter'] = True
                        self.button_play_rect.x = (790 + 670 + 30) / resized

                    elif self.button_quit_rect.collidepoint(mouse_pos):
                        quit()

                    elif self.button_play_rect.collidepoint(mouse_pos):
                        self.main_menu = False
                        # self.before_game_start()

            if self.is_full_screen:
                screen.blit(self.button_windowed, self.button_windowed_rect)
            else:
                screen.blit(self.button_full_screen, self.button_full_screen_rect)

            if not self.main_menu:
                break

            screen.blit(self.new_platform, (70 / resized, 600 / resized))
            screen.blit(self.new_platform, (755 / resized, 600 / resized))
            screen.blit(self.new_platform, (1400 / resized, 600 / resized))
            screen.blit(self.button_quit, self.button_quit_rect)
            # screen.blit(self.platform, (70 / resized, 600 / resized))
            # screen.blit(self.platform, (750 / resized, 600 / resized))
            # screen.blit(self.platform, (1400 / resized, 600 / resized))
            if not self.is_ready_to_start:
                screen.blit(self.fake_start, self.button_play_rect)

            screen.blit(self.warrior.idle_animation("right"), (self.heroes_x_y[0][0], self.heroes_x_y[0][1]))
            screen.blit(self.mage.idle_animation('right'), (self.heroes_x_y[1][0], self.heroes_x_y[1][1]))
            screen.blit(self.hunter.idle_animation('right'), (self.heroes_x_y[2][0], self.heroes_x_y[2][1]))
            i = 0
            for key, value in self.selected.items():
                self.index += 0.13
                if value:
                    see_arrow = self.arrow[int(self.index) % len(self.arrow)]
                    screen.blit(see_arrow, (self.arrow_pos[i][0], self.arrow_pos[i][1]))

                    self.is_ready_to_start = True
                    screen.blit(self.button_play, self.button_play_rect)

                    self.chosen_hero = self.get_current_hero[key]

                i += 1

            pygame.display.update()

    def before_game_start(self):
        mouse_pos = pygame.mouse.get_pos()
        chosen_hero = self.chosen_hero
        if self.button_play_rect.collidepoint(mouse_pos):
            music('images/maps/map1/map1_song.mp3')
            for i in range(510):
                screen.blit(self.menu_image, (0, 0))
                screen.blit(chosen_hero.jump_animation(), (650 / resized, 200 / resized))
                pygame.draw.rect(screen, (50, (255 - i // 2), 0), self.menu_image_rect, int(i * 1.1))
                pygame.display.update()

# menu = Menu()
# menu.menu()

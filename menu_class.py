import pygame

from mage_character import Mage
from warrior_character import Warrior


class Menu:
    arrow = [pygame.image.load(f'images/menu/arrow/({i}).png') for i in range(1, 9)]

    pygame.mixer.init()
    pygame.mixer.music.load("images/menu/music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

    buttons_x, buttons_y = 1920 / 2 - 200, 1080 / 1.01 - 150
    menu_image = pygame.image.load('images/menu/make_character.jpg')

    button_play = pygame.image.load('images/menu/play.png')
    button_play_rect = button_play.get_rect()
    button_play_rect.x = buttons_x
    button_play_rect.y = buttons_y

    button_quit = pygame.image.load('images/menu/exit.png')
    button_quit_rect = button_quit.get_rect()
    button_quit_rect.x = buttons_x
    button_quit_rect.y = buttons_y + 100

    platform = pygame.image.load('images/menu/platform.png')

    heroes_x_y = [(120, 240), (790, 240)]

    warrior_rect = Warrior().idle_animation().get_rect()
    warrior_rect.x = heroes_x_y[0][0]
    warrior_rect.y = heroes_x_y[0][1]

    mage_rect = Mage().idle_animation().get_rect()
    mage_rect.x = heroes_x_y[1][0]
    mage_rect.y = heroes_x_y[1][1]

    WIDTH, HEIGHT = (1920, 1080)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    selected = {"warrior": False, "mage": False, }
    arrow_pos = [(225, 80),(900,80)]

    index = 0

    def __init__(self, ):
        self.main_menu = True
        self.warrior = Warrior()
        self.mage = Mage()

    @property
    def get_character_objects(self):
        return {'warrior': self.warrior}

    def menu(self, ):
        while self.main_menu:
            self.screen.blit(self.menu_image, (0, 0))

            self.screen.blit(self.button_quit, self.button_quit_rect)
            self.screen.blit(self.platform, (70, 600))
            self.screen.blit(self.platform, (750, 600))
            self.screen.blit(self.platform, (1400, 600))

            self.screen.blit(self.warrior.idle_animation(), (self.heroes_x_y[0][0], self.heroes_x_y[0][1]))
            self.screen.blit(self.mage.idle_animation(), (self.heroes_x_y[1][0], self.heroes_x_y[1][1]))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_play_rect.collidepoint(mouse_pos):
                        self.main_menu = False
                    elif self.warrior_rect.collidepoint(mouse_pos):
                        self.selected['warrior'] = True
                        self.selected['mage'] = False
                    elif self.mage_rect.collidepoint(mouse_pos):
                        self.selected['warrior'] = False
                        self.selected['mage'] = True

                    elif self.button_quit_rect.collidepoint(mouse_pos):
                        quit()

            print(self.selected)
            if any(x for x in self.selected.values()):
                self.screen.blit(self.button_play, self.button_play_rect)

                self.index += 0.3
                see_arrow = self.arrow[int(self.index) % len(self.arrow)]
                if self.selected["warrior"]:
                    self.screen.blit(see_arrow, (self.arrow_pos[0][0], self.arrow_pos[0][1]))
                elif self.selected['mage']:
                    self.screen.blit(see_arrow, (self.arrow_pos[1][0], self.arrow_pos[1][1]))
            pygame.display.flip()


menu = Menu()
menu.menu()

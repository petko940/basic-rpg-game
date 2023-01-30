import pygame


class Menu:
    pygame.mixer.init()
    pygame.mixer.music.load("images/menu/music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

    buttons_x, buttons_y = 1920 / 2 - 200, 1080 / 2 - 150
    menu_image = pygame.image.load('images/menu/menu.jpg')
    make_character = pygame.image.load('images/menu/make_character.jpg')

    button_play = pygame.image.load('images/menu/play.png')
    button_play_rect = button_play.get_rect()
    button_play_rect.x = buttons_x
    button_play_rect.y = buttons_y

    button_quit = pygame.image.load('images/menu/exit.png')
    button_quit_rect = button_quit.get_rect()
    button_quit_rect.x = buttons_x
    button_quit_rect.y = buttons_y + 100

    button_back = pygame.image.load('images/menu/back.png')
    button_back_rect = button_back.get_rect()
    button_back_rect.x = buttons_x
    button_back_rect.y = buttons_y + 200

    WIDTH, HEIGHT = (1920, 1080)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self, ):
        self.main_menu = True
        self.podmenu = False

    def menu(self, ):
        while self.main_menu:
            self.screen.blit(self.menu_image, (0, 0))
            self.screen.blit(self.button_play, self.button_play_rect)
            self.screen.blit(self.button_quit, self.button_quit_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_play_rect.collidepoint(mouse_pos):
                        self.main_menu = False
                        self.podmenu = True
                        self.screen.blit(self.make_character, (0, 0))
                        self.screen.blit(self.button_back, self.button_back_rect)
                    elif self.button_quit_rect.collidepoint(mouse_pos):
                        quit()
            pygame.display.flip()

    def podmenu1(self):
        while self.podmenu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_back_rect.collidepoint(mouse_pos):
                        self.main_menu = True
                        self.podmenu = False

            pygame.display.flip()
        return self.podmenu1

import pygame


class Warrior:
    __IDLE_SPEED = 0.2

    def __init__(self):
        self.idle_images = [pygame.image.load(f'images/war/idle/({i}).png') for i in range(1, 11)]
        self.attack_images = [pygame.image.load(f'images/war/attack/({i}).png') for i in range(1, 11)]
        self.die_images = [pygame.image.load(f'images/war/die/({i}).png') for i in range(1, 11)]
        self.walk_images_right = [pygame.image.load(f'images/war/walk/({i}).png') for i in range(1, 11)]

        self.index = 0

    def idle_animation(self):
        self.index += self.__IDLE_SPEED
        return self.idle_images[int(self.index) % len(self.idle_images)]


test = Warrior()

##########################
"""TO TEST ANIMATIONS"""
WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
    screen.fill((255, 255, 255))

    screen.blit(test.idle_animation(), (300, 300))

    pygame.display.flip()
##########################
"""TO TEST ANIMATIONS"""

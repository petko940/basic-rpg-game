import pygame

idle_images = [pygame.image.load(f'images/war/idle/({i}).png') for i in range(1, 11)]
attack_images = [pygame.image.load(f'images/war/attack/({i}).png') for i in range(1, 11)]
die_images = [pygame.image.load(f'images/war/die/({i}).png') for i in range(1, 11)]
walk_images_right = [pygame.image.load(f'images/war/walk/({i}).png') for i in range(1, 11)]


class Warrior:
    __IDLE_SPEED = 0.16

    def __init__(self):
        self.index = 0

    def idle_animation(self):
        self.index += self.__IDLE_SPEED
        return idle_images[int(self.index) % len(idle_images)]

# test = Warrior()
#
# WIDTH, HEIGHT = (1920, 1080)
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
#
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 quit()
#     screen.fill((255, 255, 255))
#
#     screen.blit(test.idle_animation(), (300, 300))
#
#     pygame.display.flip()

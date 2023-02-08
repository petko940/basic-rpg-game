import pygame

idle_images_right = [pygame.image.load(f'images/war/idle/({i}).png') for i in range(1, 11)]
idle_images_left = [pygame.transform.flip(idle_images_right[i], True, False) for i in range(10)]
# idle_mask_right = [pygame.mask.from_surface(x) for x in idle_images_right]

attack_images_right = [pygame.image.load(f'images/war/attack/({i}).png') for i in range(1, 11)]
attack_images_left = [pygame.transform.flip(attack_images_right[i], True, False) for i in range(10)]

die_images = [pygame.image.load(f'images/war/die/({i}).png') for i in range(1, 11)]

walk_images_right = [pygame.image.load(f'images/war/walk/({i}).png') for i in range(1, 11)]
walk_images_left = [pygame.transform.flip(walk_images_right[i], True, False) for i in range(10)]

jump_images = [pygame.image.load(f'images/war/jump/({i}).png') for i in range(1, 11)]


class Warrior:
    __IDLE_SPEED = 0.16

    def __init__(self):
        self.index = 0
        self.idle_mask_right = [pygame.mask.from_surface(x) for x in idle_images_right]

    def idle_animation(self, direction):
        self.index += self.__IDLE_SPEED
        if direction == "right":
            return idle_images_right[int(self.index) % len(idle_images_right)]
        return idle_images_left[int(self.index) % len(idle_images_left)]

    def walk_images(self, direction):
        self.index += self.__IDLE_SPEED
        if direction == "right":
            return walk_images_right[int(self.index) % len(walk_images_right)]
        return walk_images_left[int(self.index) % len(walk_images_left)]

    def attack_animation(self,direction ):
        self.index += 0.1
        if direction == "right":
            return attack_images_right[int(self.index) % len(attack_images_right)]
        return attack_images_left[int(self.index) % len(attack_images_left)]

    def jump_animation(self):
        self.index += 0.1
        return jump_images[int(self.index) % len(jump_images)]
#
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
#             elif event.key == pygame.K_a:
#                 for i in range(100):
#                     screen.blit(test.walk_images("left"), (650, 200))
#                     pygame.display.flip()
#         pygame.display.flip()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RIGHT]:
        #     screen.blit(test.walk_images("right"), (300, 300))
        #     pygame.display.flip()
        # # elif event.key == pygame.K_a:
        # #     screen.blit(test.walk_images("left"), (300, 300))
        # #     pygame.display.flip()

    # pygame.display.flip()

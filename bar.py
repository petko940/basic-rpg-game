import pygame


class Bar:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        # if we want to fill the surface with transparency:
        # alpha 0 -> full transparency, alpha 255 -> full color
        self.surface.set_alpha(35)

        # if we want to fill the surface with solid color:
        # self.surface.fill((255, 255, 255))

    def draw_surface(self, x, y):
        return self.surface.blit(self.surface, (x, y))

    # pygame.Rect(x, y, width, height)
    def draw_bar(self):
        return pygame.Rect(11, 11, 100, 18)


# General Setup
# pygame.init()
# clock = pygame.time.Clock()

# Create display surface
# we have to use the map screen here:
# screen = pygame.display.set_mode((400, 400))
# bar = Bar(200, 20)
# current_health = 200
# while True:
#     screen.fill((255, 255, 255))
#     screen.blit(bar.surface, (10, 10))
#     # red-example
#     # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(11, 11, 65, 18))
#     
#     print(f"Current health is: {current_health}")
#     current_hit = randint(0, 50)
#     print(f"Current hit is: {current_hit}")
#     if current_hit >= current_health:
#         current_health = 0
#         print("dead!")
#         sys.exit()
#     else:
#         current_health -= current_hit
#         print(f"Current health is: {current_health}")
#     # blue-example
#     bar.draw_bar(screen, (0, 0, 255), pygame.Rect(11, 11, current_health, 18))
#     pygame.display.flip()
#     clock.tick(1)

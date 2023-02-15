# this file is created only for testing of the surface on a screen x by y (in this case 800x800 white)
# over it we have surface 200 X 20 with transparency 20 (from 255) on position 10, 10
# over the surface we draw a rectangle with dynamic width on position 11, 11, red
import sys
import pygame

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Create display surface
screen = pygame.display.set_mode((800, 800))
second_surface = pygame.Surface([200, 20])  # dimensions
second_surface.set_alpha(20)
color = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(second_surface, (10, 10))  # position on the screen
    for index in range(200):
        test_bar = index
        pygame.draw.rect(screen, color, pygame.Rect(11, 11, index, 18))
        pygame.display.flip()
        clock.tick(60)

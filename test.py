import pygame


window = pygame.display.set_mode((500, 500))

surface = pygame.Surface((100, 100))

square = surface.get_rect()
square.x, square.y = 80, 120


def draw_rect_alpha(surface, color, rect):
    cooldown_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(cooldown_surf, color, cooldown_surf.get_rect())
    surface.blit(cooldown_surf, rect)


height_value = 140
width_value = 140


run = True
while run:
    pygame.time.Clock().tick(40)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    window.fill((255, 255, 255))

    pygame.draw.rect(window, (255, 0, 0), square)


    draw_rect_alpha(window, (0, 0, 255, 127), (55, 90, int(width_value), int(height_value)))
    height_value -= 0.5


    if height_value <= 0:
        exit()

    pygame.display.update()





# import pygame
# import time
#
# pygame.init()
#
# # Set up the display
# screen = pygame.display.set_mode((800, 600))
#
# # Set up the font
# font = pygame.font.SysFont(None, 70)
#
# # Set the timer
# start_time = time.time()
#
# # # Game loop
# cooldown = False
#
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_1:
#                 clicked = time.time()
#                 cooldown = True
#
#     if cooldown:
#         time_since_enter = time.time() - clicked
#         integer_time = int(time_since_enter)
#         print(integer_time)
#         if integer_time == 5:
#             cooldown = False
#
#     screen.fill((255, 255, 255))
#
#     elapsed_time = time.time() - start_time
#
#     timer_text = font.render(str(round(elapsed_time, 2)), True, (0, 0, 0))
#     screen.blit(timer_text, (30,30))
#
#     pygame.display.update()
#
# # Quit the game
# pygame.quit()

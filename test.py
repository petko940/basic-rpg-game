# import pygame
#
#
# window = pygame.display.set_mode((500, 500))
#
# surface = pygame.Surface((100, 100))
#
# square = surface.get_rect()
# square.x, square.y = 80, 120
#
#
# def draw_rect_alpha(surface, color, rect):
#     cooldown_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
#     pygame.draw.rect(cooldown_surf, color, cooldown_surf.get_rect())
#     surface.blit(cooldown_surf, rect)
#
#
# height_value = 140
# width_value = 140
#
# health_bar = pygame.Rect(100, 100, 300, 40)
#
# max_health = 150
# current_health = 150
# monster_dmg = 5
#
#
# run = True
# while run:
#     pygame.time.Clock().tick(40)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 run = False
#             if event.key == pygame.K_1:
#                 health_bar.width *= ((current_health - monster_dmg) / max_health)
#                 current_health -= monster_dmg
#
#     window.fill((255, 255, 255))
#
#     pygame.draw.rect(window, (255, 0, 0), square)
#
#     pygame.draw.rect(window, (255, 0, 0), health_bar)
#
#
#     draw_rect_alpha(window, (0, 0, 255, 127), (55, 90, int(width_value), int(height_value)))
#     height_value -= 0.5
#
#
#     if height_value <= 0:
#         exit()
#
#     pygame.display.update()





import pygame

window = pygame.display.set_mode((500, 500))

images = [pygame.image.load(f"characters/mage/explosion_sprites/{x}.png") for x in range(1, 9 + 1)]
index = 0

run = True
while run:
    pygame.time.Clock().tick(100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    window.fill((0, 255, 255))

    index += 0.1

    if index < len(images):
        backwards = index
        window.blit(images[int(index)], (250, 0))

    else:
        backwards -= 0.1
        window.blit(images[int(backwards)], (250, 0))

    if backwards <= 0:
        backwards = len(images) - 1
        index = 0



    pygame.display.update()


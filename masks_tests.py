import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

moving_object = [pygame.image.load(f'images/monsters/small_dragon/attack/Attack{i}.png').convert_alpha() for i in range(1, 3 + 1)]
obstacle = [pygame.image.load(f'images/war/idle/({i}).png').convert_alpha() for i in range(1, 10 + 1)]

moving_object_mask = [pygame.mask.from_surface(x) for x in moving_object]
obstacle_mask = [pygame.mask.from_surface(x) for x in obstacle]

obstacle_rect = [x.get_rect() for x in obstacle]

index = 0
index_obstacle = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    moving_object_rect = moving_object[int(index)].get_rect(center=pygame.mouse.get_pos())

    offset = (obstacle_rect[int(index_obstacle)].x - moving_object_rect.x), (obstacle_rect[int(index)].y - moving_object_rect.y)
    background_color = (0, 0, 0)
    if moving_object_mask[int(index)].overlap(obstacle_mask[int(index_obstacle)], offset):
        background_color = (40, 40, 80)

    index += 0.2
    index_obstacle += 0.2

    if index >= len(moving_object_mask):
        index = 0
    if index_obstacle >= len(obstacle_mask):
        index_obstacle = 0

    window.fill(background_color)
    window.blit(moving_object[int(index)], moving_object_rect)
    window.blit(obstacle[int(index_obstacle)], obstacle_rect[int(index_obstacle)])
    pygame.display.flip()

pygame.quit()








# import pygame as pg
#
#
# bg_surface = pg.Surface((640, 480), pg.SRCALPHA)
#
# pg.draw.lines(
#     bg_surface, (30, 90, 200), True,
#     ((60, 130), (300, 50), (600, 200), (400, 400), (150, 300)),
#     12)
#
# triangle_surface = pg.Surface((60, 60), pg.SRCALPHA)
#
# pg.draw.polygon(triangle_surface, (160, 250, 0), ((30, 0), (60, 60), (0, 60)))
#
#
# def main():
#     screen = pg.display.set_mode((640, 480))
#     clock = pg.time.Clock()
#
#     bg_mask = pg.mask.from_surface(bg_surface)
#     triangle_mask = pg.mask.from_surface(triangle_surface)
#
#     bg_rect = bg_surface.get_rect(center=(320, 240))
#     triangle_rect = triangle_surface.get_rect(center=(0, 0))
#
#     done = False
#
#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             elif event.type == pg.MOUSEMOTION:
#                 triangle_rect.center = event.pos
#
#         offset_x = triangle_rect.x - bg_rect.x
#         offset_y = triangle_rect.y - bg_rect.y
#
#         overlap = bg_mask.overlap(triangle_mask, (offset_x, offset_y))
#         if overlap:
#             print('The two masks overlap!', overlap)
#
#         screen.fill((30, 30, 30))
#         screen.blit(bg_surface, bg_rect)
#         screen.blit(triangle_surface, triangle_rect)
#
#         pg.display.flip()
#         clock.tick(30)
#
#
# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()


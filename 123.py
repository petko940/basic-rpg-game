import pygame

from actions import Actions
from warrior_character import Warrior

# Initialize Pygame
pygame.init()

# Load the images into a list
image_list = []
for i in range(1, 6):
    image = pygame.image.load(f"images/war/idle/({i}).png")
    asd = pygame.transform.scale(image, (100, 100))
    image_list.append(asd)

# Create a list of masks from the images
mask_list = []
for image in image_list:
    mask = pygame.mask.from_surface(image)
    mask_list.append(mask)

# Set up the screen
screen = pygame.display.set_mode((800, 600))
warrior = Warrior()
actions = Actions()
# Main game loop
running = True
x, y = 200, 30
rec = pygame.Rect(x, y, 300, 50)
# mask_rec = pygame.mask.from_surface(rec)
surface = pygame.Surface((rec.width, rec.height), pygame.SRCALPHA)
surface.fill((255, 255, 255, 255))
rec_mask = pygame.mask.from_surface(surface)
print(pygame.SRCALPHA)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    screen.blit(image_list[0], (10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    # Draw the images to the screen using the masks
    x -= 0.05
    print(x)
    # print(mask_list[0], image_list[0], x)
    # offset = mask_list[0].overlap(rect, (x, y))
    if mask_list[0].overlap(rec_mask, (10, 10)):
        print("colision")

    pygame.display.update()

# Quit Pygame
pygame.quit()

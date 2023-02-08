import pygame

# initialize pygame
pygame.init()

# load an image
image1 = pygame.image.load("images/war/idle/(1).png")
image2 = pygame.image.load("images/war/idle/(2).png")

# create a mask from the image
mask1 = pygame.mask.from_surface(image1)
mask2 = pygame.mask.from_surface(image2)
print(image1.get_rect())
print(image2.get_rect())
# check if the two masks overlap
offset = (10, 20)
overlap = mask1.overlap(mask2, offset)

if overlap:
    print("The two masks overlap!")
else:
    print("The two masks do not overlap.")

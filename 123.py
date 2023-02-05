import pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = (1920, 1080)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Load the sprite images
images = [pygame.image.load(f"images/({i}).png").convert_alpha() for i in range(1,9)]

# Define the sprite class
class Sprite:
    def __init__(self, images):
        self.images = images
        self.index = 0

    def update(self):
        self.index = int(self.index + 1) % len(self.images)
        print(self.index)
    def image(self):
        return self.images[self.index]

# Create an instance of the sprite class
sprite = Sprite(images)

speed = 1
# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the sprite
    sprite.update()

    # Draw the sprite on the screen
    screen.blit(sprite.image(), (500, 500))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

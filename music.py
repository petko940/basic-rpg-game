import pygame


def music(mp3):
    # pygame.mixer.music.stop()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

import pygame


def full_screen():
    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    return screen


def windowed():
    screen = pygame.display.set_mode((1366, 768))
    return screen

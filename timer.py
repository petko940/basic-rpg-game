import pygame
import time


def timer(start_time, screen):
    font = pygame.font.SysFont(None, 100)
    elapsed_time = time.time() - start_time
    timer_text = font.render(str(round(elapsed_time, 2)), True, (255, 255, 255))
    screen.blit(timer_text, (300, 300))

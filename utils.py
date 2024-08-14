import pygame as pg


def get_screen_size():
    return 1366, 768


def create_font(value:str, font:str, size_font:int, colour: tuple, bold=True, antialias=True):
    font = pg.font.SysFont(font, size_font, bold)
    return font.render(value, antialias, colour)


def numbers_format(num):
    num = float(f'{num:.3g}')
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    result = f"{str(num).rstrip('0').rstrip('.')}{['', 'K', 'M', 'B', 'T'][magnitude]}"
    return result

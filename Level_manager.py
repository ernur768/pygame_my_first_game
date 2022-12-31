import pygame
from Constants import *

stone_image = pygame.image.load('images/stone.png')


class LevelManager:

    @staticmethod
    def load_level(level_num: str) -> list:
        f = open('levels/LEVEL_' + level_num)
        level = f.read().split('\n')
        f.close()
        return level

    @staticmethod
    def set_level(level_skeleton: list, screen) -> list:
        tile_rects = []
        y = 0
        for row in level_skeleton:
            x = 0
            for tile in row:
                if tile == '1' or tile == '2':
                    screen.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

        return tile_rects

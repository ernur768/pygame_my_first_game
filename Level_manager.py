from Enemy import Enemy
from Player import Player
import Bullet
from Constants import *
from level.level_settings import *


def load_enemies(level_num: int) -> list:
    level_num = str(level_num)
    e = []
    for i in range(LEVELS[level_num]['enemy_num']):
        e.append(Enemy(LEVELS[level_num]['enemy_pos'][i],
                       LEVELS[level_num]['field_of_vision_width'][i],
                       i))

    return e


def load_level(level_num: int) -> list:
    f = open('level/level_skeletons/LEVEL_' + str(level_num) + '.txt')
    level = f.read().split('\n')
    f.close()

    return level


class LevelManager:

    def __init__(self):
        self.current_level = 2
        self.enemies = load_enemies(self.current_level)
        self.level_skeleton = load_level(self.current_level)

    @staticmethod
    def blit_images(enemies: list, screen: pygame.Surface, player: Player, current_level: int):

        current_level = str(current_level)
        for i in range(LEVELS[current_level]['enemy_num']):
            enemies[i].enemy_action(player.p_rect)
            screen.blit(pygame.transform.flip(enemies[i].image, enemies[i].flip, False),
                        (enemies[i].rect.x - player.scroll[0], enemies[i].rect.y - player.scroll[1]))

        screen.blit(pygame.transform.flip(player.image, player.flip, False),
                    (player.p_rect.x - player.scroll[0], player.p_rect.y - player.scroll[1]))

        for bullet in Bullet.bullet_list:
            screen.blit(bullet.image, (bullet.rect.x - player.scroll[0], bullet.rect.y - player.scroll[1]))

    @staticmethod
    def set_level(level_skeleton: list, screen: pygame.Surface, scroll: list) -> list:
        tile_rects = []
        y = 0
        for row in level_skeleton:
            x = 0
            for tile in row:
                if tile == '1':
                    screen.blit(stone_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                if tile == '2':
                    screen.blit(red_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

        return tile_rects

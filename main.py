import pygame
from Constants import *
from Level_manager import LevelManager
from Player import Player

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('my first python game')
    screen = pygame.Surface(SCREEN_SIZE)

    p = Player()
    level_manager = LevelManager()

    current_level = level_manager.load_level('3')

    scroll = [0, 0]

    back = pygame.image.load('images/background_v4.png').convert()

    while True:
        screen.fill(WHITE)

        scroll[0] += (p.p_rect.x - scroll[0] - (SCREEN_SIZE[0] - PLAYER_WIDTH) // 2) // 10
        scroll[1] += (p.p_rect.y - scroll[1] - (SCREEN_SIZE[1] - PLAYER_HEIGHT) // 2) // 10

        screen.blit(back, (p.p_rect.x - scroll[0], p.p_rect.y - scroll[1]))
        tile_rects = level_manager.set_level(current_level, screen, scroll)

        p.keyboard_register()
        p.move_register(tile_rects)

        screen.blit(p.image, (p.p_rect.x - scroll[0], p.p_rect.y - scroll[1]))
        window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

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

    while True:
        screen.fill(WHITE)
        tile_rects = level_manager.set_level(current_level, screen)

        p.keyboard_register()
        p.move_register(tile_rects)

        screen.blit(p.image, (p.p_rect.x, p.p_rect.y))
        window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

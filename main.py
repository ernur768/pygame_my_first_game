from Level_manager import LevelManager
from Player import Player
from Constants import *
from level.level_settings import *

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('my first python game')
    screen = pygame.Surface(SCREEN_SIZE)

    p = Player()
    level_manager = LevelManager()

    background = pygame.image.load('images/background_v4.png').convert()

    while True:
        screen.blit(background, (0.01 * (p.p_rect.x - p.scroll[0] - SCREEN_SIZE[0] // 2),
                                 0.01 * (p.p_rect.y - p.scroll[1] - SCREEN_SIZE[1] // 2)))

        tile_rects = level_manager.set_level(level_manager.level_skeleton, screen, p.scroll)

        p.camera_scroll()
        p.keyboard_register()
        p.move_register(tile_rects)
        p.animation_register()

        level_manager.blit_images(level_manager.enemies, screen, p, level_manager.current_level)

        window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

import pygame
from Constants import *
from Level_manager import LevelManager
from Player import Player

# ----------------------------------------------------------------------------
animation_image_database = {}


def add_to_image_database(animation_name: str, image_num: int) -> None:
    global animation_image_database
    for i in range(image_num):
        image_name = animation_name + '_' + str(i)
        image = pygame.image.load('animations/' + animation_name + '/' + image_name + '.png')
        image.set_colorkey(WHITE)
        animation_image_database[image_name] = image.copy()


def get_animation(animation_name: str, animation_duration: list) -> list:
    animation = []

    image_num = 0
    for frame_num in animation_duration:

        image_name = animation_name + '_' + str(image_num)

        for i in range(frame_num):
            animation.append(image_name)
        image_num += 1

    return animation


def change_action(action_var, frame, new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame


animation_database = {'stand': get_animation('stand', [15, 7]),
                      'run': get_animation('run', [7, 7])}

add_to_image_database('stand', 2)
add_to_image_database('run', 2)

player_action = 'stand'
animation_frame = 0
player_flip = False
# --------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('my first python game')
    screen = pygame.Surface(SCREEN_SIZE)

    p = Player()
    level_manager = LevelManager()

    current_level = level_manager.load_level('3')
    background = pygame.image.load('images/background_v4.png').convert()

    while True:
        screen.blit(background, (0.01 * (p.p_rect.x - p.scroll[0] - SCREEN_SIZE[0] // 2),
                                 0.01 * (p.p_rect.y - p.scroll[1] - SCREEN_SIZE[1] // 2)))

        tile_rects = level_manager.set_level(current_level, screen, p.scroll)
        p.camera_scroll()
        p.keyboard_register()
        p.move_register(tile_rects)


# ---------------------------------------------------------------------------------------------
        if p.movement[0] < 0:
            player_action, animation_frame = change_action(player_action, animation_frame, 'run')
            player_flip = True
        if p.movement[0] == 0:
            player_action, animation_frame = change_action(player_action, animation_frame, 'stand')
        if p.movement[0] > 0:
            player_action, animation_frame = change_action(player_action, animation_frame, 'run')
            player_flip = False

        animation_frame += 1
        if animation_frame == len(animation_database[player_action]):
            animation_frame = 0
        player_img_id = animation_database[player_action][animation_frame]
        p.image = animation_image_database[player_img_id]
# ----------------------------------------------------------------------------------------------

        screen.blit(pygame.transform.flip(p.image, player_flip, False),
                    (p.p_rect.x - p.scroll[0], p.p_rect.y - p.scroll[1]))
        window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

import pygame
from Constants import *
from Level_manager import LevelManager
from Player import Player

# ----------------------------------------------------------------------------
global animation_frames # self.animation_frames
animation_frames = {}


def load_animation(path: str, frame_duration):# make class method
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_duration:
        animation_frame_id = animation_name + '_' + str(n)
        image_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(image_loc)
        animation_image.set_colorkey(WHITE)
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1

    return animation_frame_data


def change_action(action_var, frame, new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame


animation_database = {'idle': load_animation('animations/stand', [15, 7]),
                      'run': load_animation('animations/run', [7, 7])}

player_action = 'idle'
player_frame = 0
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
            player_action, player_frame = change_action(player_action, player_frame, 'run')
            player_flip = True
        if p.movement[0] == 0:
            player_action, player_frame = change_action(player_action, player_frame, 'idle')
        if p.movement[0] > 0:
            player_action, player_frame = change_action(player_action, player_frame, 'run')
            player_flip = False

        player_frame += 1
        if player_frame == len(animation_database[player_action]):
            player_frame = 0
        player_img_id = animation_database[player_action][player_frame]
        p.image = animation_frames[player_img_id]
# ----------------------------------------------------------------------------------------------

        screen.blit(pygame.transform.flip(p.image, player_flip, False), (p.p_rect.x - p.scroll[0], p.p_rect.y - p.scroll[1]))
        window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

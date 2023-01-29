import pygame


stone_image = pygame.image.load('images/stone.png')
red_image = pygame.image.load('images/red.png')


LEVELS = {'2': {'enemy_num': 3,
                'enemy_pos': [[352, 160], [928, 160], [1600, 384]],
                'field_of_vision_width': [17, 17, 10]}}

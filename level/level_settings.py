import pygame


stone_image = pygame.image.load('images/stone.png')

LEVELS = {'2': {'enemy_num': 2,
                'enemy_pos': [[352, 160], [928, 160]],
                'field_of_vision_width': [16, 12]}}
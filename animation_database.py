import pygame
from Constants import *


def add_to_image_database(animation_name: str, image_num: int) -> None:
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


animation_image_database = {}

animation_database = {'stand': get_animation('stand', [15, 7]),
                      'run': get_animation('run', [7, 7])}

add_to_image_database('stand', 2)
add_to_image_database('run', 2)

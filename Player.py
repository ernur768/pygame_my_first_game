from Constants import *
from animation_database import animation_image_database, animation_database
import pygame
from Bullet import Bullet
from Bullet import bullet_list


def change_action(action_var: str, frame: int, new_value: str):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame


def collision_test(rect: pygame.Rect, tiles: list) -> list:
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)

    return hit_list


def block_stop_x(tiles: list, movement: list, p_rect: pygame.Rect):
    collision_types = {'Right': False, 'Left': False}
    hit_list = collision_test(p_rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            p_rect.right = tile.left
            collision_types['Right'] = True
        if movement[0] < 0:
            p_rect.left = tile.right
            collision_types['Left'] = True

    return collision_types, p_rect


def block_stop_y(tiles: list, movement: list, p_rect: pygame.Rect):
    collision_types = {'Top': False, 'Bottom': False}
    hit_list = collision_test(p_rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            p_rect.bottom = tile.top
            collision_types['Bottom'] = True
        if movement[1] < 0:
            p_rect.top = tile.bottom
            collision_types['Top'] = True

    return collision_types, p_rect


class Player:

    def __init__(self):
        self.reload = 0
        self.animation_frame = 0
        self.health = 30
        self.shoot = False
        self.flip = False
        self.action = 'stand'
        self.speed = 4
        self.start_pos = [0, 0]
        self.momentum_y = 0
        self.jump_force = 10
        self.air_time = 0
        self.movement = [0, 0]
        self.scroll = [0, 0]
        self.image = pygame.image.load('images/my_player.png').convert()
        self.image.set_colorkey(WHITE)
        self.p_rect = pygame.Rect(self.start_pos[0], self.start_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT)

    def animation_register(self) -> None:
        if self.movement[0] < 0:
            self.action, self.animation_frame = change_action(self.action, self.animation_frame, 'run')
            self.flip = True
        if self.movement[0] == 0:
            self.action, self.animation_frame = change_action(self.action, self.animation_frame, 'stand')
        if self.movement[0] > 0:
            self.action, self.animation_frame = change_action(self.action, self.animation_frame, 'run')
            self.flip = False

        self.animation_frame += 1
        if self.animation_frame == len(animation_database[self.action]):
            self.animation_frame = 0
        player_img_id = animation_database[self.action][self.animation_frame]
        self.image = animation_image_database[player_img_id]

    def keyboard_register(self) -> None:
        self.movement = [0, 0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_j and self.reload < 0:
                    self.shoot = True
                if event.key == pygame.K_k:
                    print(self.p_rect.x)
                if event.key == pygame.K_l:
                    print(self.p_rect.y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.movement[0] -= self.speed
        if keys[pygame.K_d]:
            self.movement[0] += self.speed
        if keys[pygame.K_SPACE]:
            if self.air_time < 10:
                self.momentum_y = -self.jump_force

    def move_register(self, tile_rects: list) -> None:
        self.movement[1] += self.momentum_y
        self.momentum_y += (3 * self.air_time)
        if self.momentum_y > 5:
            self.momentum_y = 5

        self.p_rect.x += self.movement[0]
        collision_types_x, self.p_rect = block_stop_x(tile_rects, self.movement, self.p_rect)
        self.p_rect.y += self.movement[1]
        collision_types_y, self.p_rect = block_stop_y(tile_rects, self.movement, self.p_rect)

        self.reload -= 1

        if collision_types_y['Bottom']:
            self.momentum_y = 0
            self.air_time = 1
        else:
            self.air_time += 1

        if self.shoot:
            self.reload = 60
            self.action = 'player shoot'
            if self.flip:
                bullet_list.append(Bullet(self.p_rect.x - 1, self.p_rect.y + 15, self.flip))
            else:
                bullet_list.append(Bullet(self.p_rect.x + 7, self.p_rect.y + 15, self.flip))

            self.shoot = False
            #class Bullet creates new obj and adds it to list


    def camera_scroll(self) -> None:
        self.scroll[0] += (self.p_rect.x - self.scroll[0] - (SCREEN_SIZE[0] - PLAYER_WIDTH) // 2) // 10
        self.scroll[1] += (self.p_rect.y - self.scroll[1] - (SCREEN_SIZE[1] - PLAYER_HEIGHT) // 2) // 10

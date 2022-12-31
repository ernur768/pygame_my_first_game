from Constants import *
import pygame


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)

    return hit_list


class Player:

    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.speed = 4
        self.start_pos = [0, 0]
        self.momentum_y = 0
        self.jump_force = 10
        self.air_time = 0
        self.movement = [0, 0]
        self.image = pygame.image.load('images/my_player.png').convert()
        self.image.set_colorkey(WHITE)
        self.p_rect = pygame.Rect(self.start_pos[0], self.start_pos[1],
                                  self.image.get_width(), self.image.get_height())

    def keyboard_register(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                if event.key == pygame.K_UP:
                    if self.air_time < 6:
                        self.momentum_y = -self.jump_force
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.moving_left = False

    def move_register(self, tile_rects):
        self.movement = [0, 0]
        if self.moving_right:
            self.movement[0] += self.speed
        if self.moving_left:
            self.movement[0] -= self.speed
        self.movement[1] += self.momentum_y
        self.momentum_y += ((0.3 * self.air_time) / 2)
        if self.momentum_y > 5:
            self.momentum_y = 5

        collision_types = self.move(tile_rects)

        if collision_types['Bottom'] or collision_types['Top']:
            self.momentum_y = 0
            self.air_time = 1
        else:
            self.air_time += 1

    def move(self, tiles: list):
        collision_types = {'Top': False, 'Bottom': False, 'Right': False, 'Left': False}
        self.p_rect.x += self.movement[0]
        hit_list = collision_test(self.p_rect, tiles)
        for tile in hit_list:
            if self.movement[0] > 0:
                self.p_rect.right = tile.left
                collision_types['Right'] = True
            if self.movement[0] < 0:
                self.p_rect.left = tile.right
                collision_types['Left'] = True
        self.p_rect.y += self.movement[1]
        hit_list = collision_test(self.p_rect, tiles)
        for tile in hit_list:
            if self.movement[1] > 0:
                self.p_rect.bottom = tile.top
                collision_types['Bottom'] = True
            if self.movement[1] < 0:
                self.p_rect.top = tile.bottom
                collision_types['Top'] = True

        return collision_types

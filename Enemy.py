from Constants import *
import pygame


class Enemy:

    def __init__(self, start_pos, field_of_vision_width, name):
        self.name = name
        self.animation_frame = 0
        self.action = 'walk'
        self.start_pos = start_pos
        self.speed = 1
        self.movement = 1
        self.flip = False
        self.field_of_vision_width = field_of_vision_width
        self.image = pygame.image.load('images/my_enemy.png').convert().copy()
        self.image.set_colorkey(WHITE)
        self.rect = pygame.Rect(self.start_pos[0], self.start_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT)
        self.field_of_vision = pygame.Rect(self.start_pos[0] - PLAYER_WIDTH, self.start_pos[1],
                                           self.field_of_vision_width * TILE_SIZE - TILE_SIZE, PLAYER_HEIGHT)

    def enemy_action(self, player_rect: pygame.Rect):
        if player_rect.colliderect(self.field_of_vision):
            self.action = 'stand_and_shoot'
            if player_rect.x > self.rect.x:
                self.flip = False
            else:
                self.flip = True
        else:
            self.action = 'walk'

        if not self.rect.colliderect(self.field_of_vision):
            self.flip = not self.flip

        if self.action == 'walk':
            if not self.flip:
                self.rect.x += self.speed
            if self.flip:
                self.rect.x -= self.speed

        if self.action == 'stand_and_shoot':
            print("hit", self.name)

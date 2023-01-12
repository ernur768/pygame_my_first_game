from Constants import *
import pygame
from Bullet import Bullet
from Bullet import bullet_list

class Enemy:

    def __init__(self, start_pos, field_of_vision_width, name):
        self.reload = 0
        self.name = name
        self.health = 2
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
        self.reload -= 1
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

        if self.action == 'stand_and_shoot' and self.reload < 0:
            self.reload = 100
            if self.flip:
                bullet_list.append(Bullet(self.rect.x - 1, self.rect.y + 5, self.flip))
            else:
                bullet_list.append(Bullet(self.rect.x + 7, self.rect.y + 5, self.flip))

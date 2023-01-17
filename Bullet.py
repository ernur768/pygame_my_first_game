import pygame
from Constants import *


bullet_list = []


def bullet_action(bullet_list: list):
    for bullet in bullet_list:
        if bullet.active:
            if bullet.flip:
                bullet.rect.x -= bullet.speed
            else:
                bullet.rect.x += bullet.speed


class Bullet:

    def __init__(self, posX, posY, flip):
        self.image = pygame.image.load("images/bullet_image.png")
        self.active = True
        self.flip = flip
        self.speed = 9
        self.rect = pygame.Rect(posX, posY, BULLET_WIDTH, BULLET_HEIGHT)

    def collisions(self, player, e_rect, tiles: list):
        if self.rect.colliderect(player.p_rect):
            player.health -= 1
            self.active = False
            bullet_list.remove(self.rect)
            self.rect.x = 0
            self.rect.y = 0

        for enemy in e_rect:
            if self.rect.colliderect(enemy.rect):
                enemy.health -= 1
                self.active = False
                # bullet_list.remove(self.rect)
                self.rect.x = 0
                self.rect.y = 0

        for tile in tiles:
            if self.rect.colliderect(tile):
                self.active = False
                # bullet_list.remove(self.rect)
                self.rect.x = 0
                self.rect.y = 0


# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption('hello, world!')
background = pygame.image.load('bg.jpg').convert_alpha()
plane = pygame.image.load('plane.png').convert_alpha()
bullet = pygame.image.load('bullet.png').convert_alpha()
bullet_x = 0
bullet_y = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    if bullet_y < 0:
        bullet_x = x - bullet.get_width() / 2
        bullet_y = y - bullet.get_height() / 2
    else:
        bullet_y -= 5
    screen.blit(bullet, (bullet_x, bullet_y))
    x -= plane.get_width() / 2
    y -= plane.get_height() / 2
    screen.blit(plane, (x, y))
    pygame.display.update()
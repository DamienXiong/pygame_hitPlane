# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((600, 300), 0, 32)
pygame.display.set_caption('hello, world!')
background = pygame.image.load('background.jpg').convert()
image = ['background.jpg', 'background2.jpg']
mouseclick = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseclick % 2 == 0:
                background = pygame.image.load(image[1]).convert()
            else:
                background = pygame.image.load(image[0]).convert()
            mouseclick += 1
    screen.blit(background, (0, 0))
    pygame.display.update()
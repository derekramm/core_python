#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_第一个程序.py"""

# 导入pygame模块
import random
import sys

import pygame
from pygame.locals import *

# 通过死循环固定住窗体

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load('images/bg.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()

    x, y = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))

    rgb = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    radius = random.randint(5, 15)
    width = random.randint(1, 5)

    pygame.draw.circle(screen, rgb, (x, y), radius, width)

    pygame.display.update()





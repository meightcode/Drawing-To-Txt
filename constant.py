import pygame
from pygame.locals import *

title = "Drawing to txt"
win = [500,500]

black = [0, 0, 0]
grey =[130,130,130]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
yellow = [255, 255, 0]
pink = [255, 0, 255]
light_blue = [0, 255, 255]


pygame.init()
screen = pygame.display.set_mode((win[0],win[1]))
pygame.display.set_caption(title)
screen.fill(white)
pygame.display.flip()

font_draw = pygame.font.Font(None,5)
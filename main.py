import pygame
from pygame.locals import *
import drawing
import building_txt
def main():
	running = True
	while running :
		drawing.theDrawingPage()
		building_txt.buildingTxt()


main()
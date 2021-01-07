import pygame
from constant import *
import sys
from pygame.locals import *

def theDrawingPage():

	screen.fill(white)
	pygame.display.flip()
	writing = False
	pen_color = black
	run = True
	rect_size = [0,0]
	add_radius_size = 0
	circle_radius = 1
	while run :
		
		
		mx ,my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				running = False
				pygame.quit()
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_r:
					screen.fill(white)
					pygame.display.flip()
				if event.key == pygame.K_RETURN:
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mx ,my = pygame.mouse.get_pos()
				writing = True
				if event.button == 5:
					add_radius_size += 1
				if event.button == 4 and -1<= add_radius_size:
					add_radius_size -= 1
				if event.button == 1 :
					pen_color = black
					circle_radius = 4
				if event.button == 3 :
					pen_color = white
					circle_radius = 14
				if event.button == 4 :
					writing = False
				if event.button == 5 :
					writing = False
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1 :
					writing = False
				if event.button == 3 :
					pygame.draw.circle(screen, white, (mx,my), circle_radius+ add_radius_size,2)
					pygame.display.flip()
					writing = False

				writing = False
			if writing == True:

				pygame.draw.circle(screen, pen_color, (mx,my), circle_radius+ add_radius_size)
				if pen_color == white:
					pygame.draw.circle(screen, black, (mx,my), circle_radius+ add_radius_size,2)


				pygame.display.flip()
				if pen_color == white:
					pygame.draw.circle(screen, white, (mx,my), circle_radius+ add_radius_size,2)
			






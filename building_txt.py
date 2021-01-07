import pygame, sys, time
from constant import *

def buildingTxt() : 
	with open("draw.txt", "w+") as file:
		file.write("")
		file.close
	counter = 0
	text = ""
	running = True
	couleur = screen.get_at((100,100))
	case = []
	number_case = 104
	pixels_case_x_and_y = win[0]//number_case
	case_y = 0
	case_x = 0
	case_with_number_black_pixels = []
	black_pixels = 0
	for i in range(number_case):
		case_row_y = i
		for i in range(number_case):
			case_row_x = i
			black_pixels = 0
			for i in range(pixels_case_x_and_y):
				row_x = i 
				for i in range(pixels_case_x_and_y):
					color = screen.get_at((row_x+pixels_case_x_and_y*case_row_x,i+pixels_case_x_and_y*case_row_y))
					if color == (0,0,0,255):
						black_pixels += 1
			
			with open("draw.txt", "a+") as file:
				if pixels_case_x_and_y**2/(black_pixels+1) <pixels_case_x_and_y**2 / 10 :
					if counter < number_case:
						text += "O   "
						file.write("O   ")
						counter += 1
					else :
						file.write("\n")
						file.write("O   ")
						counter = 1
						print(text)
						text = ""
				elif pixels_case_x_and_y**2/(black_pixels+1) <pixels_case_x_and_y**2 / 5:
					if counter < number_case:
						
						file.write("o   ")
						counter += 1
					else :
						file.write("\n")
						file.write("o   ")
						counter = 1
					
					
				elif pixels_case_x_and_y**2/(black_pixels+1) <pixels_case_x_and_y**2 / 2:
					if counter < number_case:
						text += ".   "
						file.write(".   ")
						counter += 1
					else :
						file.write("\n")
						file.write(".   ")
						counter = 1
						
				else :
					if counter < number_case:
						file.write("   ")
						counter +=1
		
					else :
						file.write("\n")
						file.write("   ")
				
				

				
						counter =1
				file.close()
	screen.fill(white)	
	pygame.display.flip()
	with open("draw.txt", "r+") as file:
		lines = file.readlines()
		which_line = 0
		for i in lines :
			text_surface = font_draw.render(i[:-1], True ,black)
			screen.blit(text_surface,(0,which_line*4.78))
			which_line += 1
			time.sleep(0.01)
			pygame.display.flip()
	while running : 
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				running = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				running = False







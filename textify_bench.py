import sys, os, pygame
from pygame.locals import *

sys.path.append('scummpy')
import Textify

GameScaleFactor = 3

wRect = (320,200)
oRect = (int(320*GameScaleFactor),int(200*GameScaleFactor))

#PyGame Setup
clock = pygame.time.Clock()
imPredisp = pygame.Surface(wRect)

screen = pygame.display.set_mode(oRect)

TextTester = Textify.BlitFont("resources/", "font_2")
TextTesterB = Textify.BlitFont("resources/", "font_1")
going = True
#print TextTester.LetterX
#print TextTester.LetterXE
while going:
	
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			going = False

	imPredisp.fill((125,0,255))
	TextTester.BlitText(imPredisp,(15,25),"Todd and jim are the best super-beast-men.")
	TextTester.BlitText(imPredisp,(15,45),"abcdefghijklmnopqrstuvwxyz")
	TextTester.BlitText(imPredisp,(15,65),"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	TextTester.BlitText(imPredisp,(15,85),"A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
	TextTesterB.BlitText(imPredisp,(15,125),"Todd and jim are the best super-beast-men.")
	TextTesterB.BlitText(imPredisp,(15,145),"abcdefghijklmnopqrstuvwxyz")
	TextTesterB.BlitText(imPredisp,(15,165),"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	TextTesterB.BlitText(imPredisp,(15,185),"A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
	screen.blit(pygame.transform.scale(imPredisp,oRect),(0,0))
	pygame.display.flip()
	
pygame.quit()
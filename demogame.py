#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

sys.path.append('scummpy')
import ScummPy






GameScaleFactor = 3

wRect = (320,200)
oRect = (int(320*GameScaleFactor),int(200*GameScaleFactor))

#PyGame Setup
clock = pygame.time.Clock()
imPredisp = pygame.Surface(wRect)

screen = pygame.display.set_mode(oRect)
imIcon=pygame.image.load("resources/gameicon.png")
pygame.display.set_icon(imIcon)
pygame.display.set_caption("Sissy's Bad Trip")


imLogoA=  pygame.image.load("resources/scummpylogo.png")
imLogoB=  pygame.image.load("resources/pygamelogo_bg.png")
imFader= pygame.Surface(wRect)
imFader.fill((0,0,0))

UpDownRamp = range(1,255,32)
for y in range(1,20):
	UpDownRamp.extend([255])
UpDownRamp.extend(range(255,1,-32))

for i in UpDownRamp:
	clock.tick(20)
	imLogoA.set_alpha(i)
	screen.fill((0,0,0))
	screen.blit(pygame.transform.scale(imLogoA,oRect),(0,0))
	pygame.display.flip()	

for i in UpDownRamp:
	clock.tick(20)
	imLogoB.set_alpha(i)
	screen.fill((0,0,0))
	screen.blit(pygame.transform.scale(imLogoB,oRect),(0,0))
	pygame.display.flip()
#ScummPy Setup! All non-scd attributes go here!
pygame.init()


#Create the ScummGame!
ScummGame = ScummPy.Game()
ScummGame.PlayerChar = 'sissy'

ScummGame.DebugDisplay = True
#Set up an animation (Note, move to .scd files.)
ScummGame.characters["sissy"].Animations["fall"]=ScummPy.ScummPyAnimation.Animation(pygame.image.load("resources/animations/sissyfallsheet.png"), 100, 100, -8, 25, 8, 1, False)

#Run the animation
ScummGame.characters["sissy"].Animations["fall"].Running=True
ScummGame.characters["sissy"].SheetY = ScummGame.characters["sissy"].WalkDownRow*ScummGame.characters["sissy"].SizeY
going = True






while going:
	
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			going = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				going = False
		#ScummGame.DoEvent(event)
		if event.type == MOUSEBUTTONDOWN:
			ScummGame.Click(ScummPy.ScummPyUtils.CoordMap(event.pos,oRect,wRect))
		if event.type == MOUSEMOTION:
			ScummGame.MouseOver(ScummPy.ScummPyUtils.CoordMap(event.pos,oRect,wRect))
	
	#Commands! This is your main game-writing area!
	for cmd in ScummGame.Commands:
		if cmd.verb == "Look":
			if cmd.noun == "Sky":
				ScummGame.characters["sissy"].Say("It's a sky alright.", 20)
			elif cmd.noun == "Flower":
				ScummGame.characters["sissy"].Say("Red Flowers. Wrong game, dude.", 20)
			else:
				ScummGame.characters["sissy"].Say("I can't see that.", 20)
	del ScummGame.Commands[:]

	ScummGame.Update()
	ScummGame.Display(imPredisp)
	screen.blit(pygame.transform.scale(imPredisp,oRect),(0,0))
	pygame.display.flip()
	
pygame.quit()

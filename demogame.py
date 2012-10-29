#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

sys.path.append('scummpy')
import ScummPy


ScummGame = ScummPy.Game()
ScummGame.PlayerChar = 'sissy'

GameScaleFactor = 2

wRect = (320,200)
oRect = (int(320*GameScaleFactor),int(200*GameScaleFactor))

#PyGame Setup
clock = pygame.time.Clock()
imPredisp = pygame.Surface(wRect)

screen = pygame.display.set_mode(oRect)
imIcon=pygame.image.load("resources/gameicon.png")
pygame.display.set_icon(imIcon)
pygame.display.set_caption("Sissy's Bad Trip")

#ScummPy Setup! All non-scd attributes go here!
pygame.init()
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
				ScummGame.characters["sissy"].Say("It's a sky alright.", 10)
			elif cmd.noun == "Flower":
				ScummGame.characters["sissy"].Say("Red Flowers. Wrong game, dude.", 10)
			else:
				ScummGame.characters["sissy"].Say("I can't see that.", 10)
	del ScummGame.Commands[:]

	ScummGame.Update()
	ScummGame.Display(imPredisp)
	screen.blit(pygame.transform.scale(imPredisp,oRect),(0,0))
	pygame.display.flip()
	
pygame.quit()
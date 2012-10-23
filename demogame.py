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


def Main():
	#PyGame Setup
	clock = pygame.time.Clock()
	imPredisp = pygame.Surface(wRect)
	
	if(len(sys.argv)>1):
		if(sys.argv[1]=="FULLSCREEN"):
			screen = pygame.display.set_mode(oRect,pygame.FULLSCREEN)
		else:
			screen = pygame.display.set_mode(oRect)
	else:
		screen = pygame.display.set_mode(oRect)

	imIcon=pygame.image.load("resources/gameicon.png")
	pygame.display.set_icon(imIcon)
	pygame.display.set_caption("Sissy's Bad Trip")
	


	#ScummPy Setup! All non-scd attributes go here!
	pygame.init()

	ScummGame.rooms['002'].Exits.append(ScummPy.ScummPyRoom.Exit(1,'003',(50,120)))
	ScummGame.rooms['003'].Exits.append(ScummPy.ScummPyRoom.Exit(1,'002',(300,120)))
	ScummGame.rooms['003'].Exits.append(ScummPy.ScummPyRoom.Exit(2,'left',(45,75)))
	ScummGame.rooms['left'].Exits.append(ScummPy.ScummPyRoom.Exit(2,'003',(300,120)))

	#Set up an animation (Note, move to .scd files.)
	ScummGame.characters["sissy"].Animations["fall"]=ScummPy.ScummPyAnimation.Animation(pygame.image.load("resources/animations/sissyfallsheet.png"), 100, 100, -8, 25, 8, 1, False)
	ScummGame.characters["sissy"].Animations["fall"].Running=True
	ScummGame.characters["sissy"].SheetY = ScummGame.characters["sissy"].WalkDownRow*ScummGame.characters["sissy"].SizeY
	
	ScummGame.characters["sissy"].Say("WELP.  Here we go.", 40)

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
		
		ScummGame.Update()
		ScummGame.Display(imPredisp)
		screen.blit(pygame.transform.scale(imPredisp,oRect),(0,0))
		pygame.display.flip()
		
	pygame.quit()

Main()





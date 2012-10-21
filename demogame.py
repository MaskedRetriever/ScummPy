#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

sys.path.append('scummpy')
import ScummPy

ScummGame = ScummPy.Game()
ScummGame.PlayerChar = 'sissy'

GameScaleFactor = 2.5

wRect = (320,200)
oRect = (int(320*GameScaleFactor),int(200*GameScaleFactor))


def Main():
	clock = pygame.time.Clock()
	

	imPredisp = pygame.Surface(wRect)
	
	if(len(sys.argv)>1):
		if(sys.argv[1]=="FULLSCREEN"):
			screen = pygame.display.set_mode(oRect,pygame.FULLSCREEN)
		else:
			screen = pygame.display.set_mode(oRect)
	else:
		screen = pygame.display.set_mode(oRect)
	pygame.init()

	
	imIcon=pygame.image.load("resources/gameicon.png")
	pygame.display.set_icon(imIcon)
	pygame.display.set_caption("Sissy's Bad Trip")
	
	
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
		
		ScummGame.Update()
		ScummGame.Display(imPredisp)
		screen.blit(pygame.transform.scale(imPredisp,oRect),(0,0))
		pygame.display.flip()
		
	pygame.quit()

Main()


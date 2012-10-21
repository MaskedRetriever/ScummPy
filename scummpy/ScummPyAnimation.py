import pygame
from pygame.locals import *

class Animation:
	def __init__(self,imSurface, SizeX=32, SizeY=64, Y=0, Steps=10, Speed=1.0, Loops = True, Layer = 0):
		self.SizeX=SizeX
		self.SizeY=SizeY
		self.Y=Y
		self.Steps=Steps
		self.Speed=Speed
		self.imAnimation = pygame.Surface((SizeY,SizeX*Steps))
		self.imAnimation.blit(imSurface,(0,-(SizeY+Y)))
		self.Running = False
		self.frame = 0
		self.blitRect = pygame.Rect(0,Y,SizeX,SizeY)
		self.Loops = Loops
		self.Layer = Layer

	def Display(self, imOut, pos):
		if self.Running:
			self.frame = (self.frame+1)%self.Steps
			self.blitRect.move(self.SizeX*self.frame,0)
		imOut.blit(self.imAnimation,pos,self.blitRect)
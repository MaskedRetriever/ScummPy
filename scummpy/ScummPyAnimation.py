import pygame
from pygame.locals import *

class Animation:
	def __init__(self,imSurface, SizeX=32, SizeY=64, X=0, Y=0, Steps=10, Speed=1.0, Loops = True, Layer = 0):
		self.SizeX=SizeX
		self.SizeY=SizeY
		self.X=X
		self.Y=Y
		self.Steps=Steps
		self.Speed=Speed
		#self.imAnimation = pygame.Surface((SizeY,SizeX*Steps))
		#self.imAnimation.blit(imSurface,(0,0))
		self.imAnimation=imSurface
		self.imPane = pygame.Surface((SizeY,SizeX))
		self.Running = False
		self.frame = 0
		self.blitRect = pygame.Rect(0,-SizeY,SizeX,SizeY)

		self.Loops = Loops
		self.Layer = Layer

	def Display(self, imOut, pos):
		self.imPane.fill((255,0,255))
		self.imPane.set_colorkey((255,0,255)) #probably inefficient, move to constructor if laggy?

		if self.Running:
			self.frame = (self.frame+1)%self.Steps
			#self.blitRect.move(-self.SizeX*self.frame,0)
			
			if ((not self.Loops) & (self.frame==(self.Steps-1))):
				self.Running=False

		self.imPane.blit(self.imAnimation,(-(self.SizeX*self.frame),0))
		imOut.blit(self.imPane,(pos[0]+self.X,pos[1]+self.Y))


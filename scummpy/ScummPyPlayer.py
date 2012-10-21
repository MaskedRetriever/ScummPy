import math
import pygame
from pygame.locals import *

class Character:
	
	def __init__(self, ResourcePath="../"):
	
		self.ResourcePath=ResourcePath
	
		self.x=250
		self.y=120
		self.scale=1
		self.xDest=self.x
		self.yDest=self.y
	
		self.Speed=4
		self.xVel=0
		self.yVel=0
	
		self.SheetX=0
		self.SheetY=0
		self.WalkStep=0
	
		self.imPlayer =  pygame.image.load(self.ResourcePath + "cSissy/sissyF1.png")
		self.imWM = pygame.image.load(self.ResourcePath + "rooms/002/room002_walkmask.png")	
		self.imSheet = pygame.image.load(self.ResourcePath + "cSissy/spritesheet.png")
		
	
	def WalkTo(self, WalkX, WalkY):
		#print "X " + str(WalkX) + " Y " + str(WalkY) + " "
		
		#Set Destination
		self.xDest=WalkX
		self.yDest=WalkY

		#Set Velocity
		Mag=math.sqrt((self.xDest-self.x)*(self.xDest-self.x)+(self.yDest-self.y)*(self.yDest-self.y))
		self.xVel=-self.Speed*(self.x-self.xDest)/Mag
		self.yVel=-self.Speed*(self.y-self.yDest)/Mag
		
	def Update(self):
		Distance = ((self.xDest-self.x)*(self.xDest-self.x)+(self.yDest-self.y)*(self.yDest-self.y))
		MaskPix=self.imWM.get_at((int(self.x),int(self.y)))
		self.scale=float(MaskPix[0])/255
		if (Distance<25):
			self.xVel=0
			self.yVel=0
		else:
			self.x=self.xVel+self.x
			self.y=self.yVel+self.y
			MaskPix=self.imWM.get_at((int(self.x),int(self.y)))
			if(MaskPix[0]==0):
				self.x=-self.xVel+self.x
				self.y=-self.yVel+self.y
				self.xVel=0
				self.yVel=0

			
			#Animation
			self.WalkStep=(self.WalkStep+1)%4

			if(self.yVel>3):
				self.SheetX = self.WalkStep*32
				self.SheetY = 70
			if(self.yVel<-3):
				self.SheetX = self.WalkStep*32
				self.SheetY = 140
			if(self.xVel>3):
				self.SheetX = self.WalkStep*32
				self.SheetY = 0
			if(self.xVel<-3):
				self.SheetX = self.WalkStep*32
				self.SheetY = 210
						
	def Display(self, imOutPut):
		#Spit to display
		self.imPlayer.fill((255,0,255))
		self.imPlayer.set_colorkey((255,0,255)) #probably inefficient, move to constructor if laggy?
		
		
		self.imPlayer.blit(self.imSheet,(-self.SheetX,-self.SheetY))
		imOutPut.blit(pygame.transform.scale(self.imPlayer,(int(32*self.scale),int(70*self.scale))), (self.x-int(16*self.scale),self.y-int(70*self.scale)))
		
	def SetWalkMask(self, newWalkMask):
		self.imWM.fill((0,0,0))
		self.imWM.blit(newWalkMask,(0,0))
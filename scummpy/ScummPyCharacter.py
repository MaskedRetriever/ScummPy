import math
import pygame
from pygame.locals import *

import ScummPyUtils
import ScummPyAnimation
import Textify

class Character:
	
	def __init__(self, ResourcePath="resources/", CharacterName="bozo"):
	
		self.ResourcePath=ResourcePath

		#Read in Character properties
		charFP = open(self.ResourcePath + "characters/" + CharacterName + "/" + CharacterName + ".scd", "r")
		for line in charFP:
			if len(line)>0:
				words = line.split()
				if words[0] == 'StartX':
					self.x = int(words[1])
				if words[0] == 'StartY':
					self.y = int(words[1])
				if words[0] == 'Speed':
					self.Speed = int(words[1])
				if words[0] == 'Layer':
					self.Layer = int(words[1])
				if words[0] == 'Startroom':
					self.Startroom = words[1]
				if words[0] == 'WalkSteps':
					self.WalkSteps = int(words[1])
				if words[0] == 'WalkLeftRow':
					self.WalkLeftRow = int(words[1])
				if words[0] == 'WalkRightRow':
					self.WalkRightRow = int(words[1])
				if words[0] == 'WalkUpRow':
					self.WalkUpRow = int(words[1])
				if words[0] == 'WalkDownRow':
					self.WalkDownRow = int(words[1])
				if words[0] == 'SizeX':
					self.SizeX = int(words[1])
				if words[0] == 'SizeY':
					self.SizeY = int(words[1])
				if words[0] == 'FontFile':
					self.FontFile = words[1]
				if words[0] == 'TalkX':
					self.TalkX = int(words[1])
				if words[0] == 'TalkY':
					self.TalkY = int(words[1])


		charFP.close()		
	
		self.scale=1
		self.xDest=self.x
		self.yDest=self.y
		self.pos=(int(self.x),int(self.y))
	
		self.xVel=0
		self.yVel=0
	
		self.SheetX=0
		self.SheetY=0
		self.WalkStep=0
	
		#Masks and Sprite Sheet
		self.imPlayer =  pygame.image.load(self.ResourcePath + "characters/" + CharacterName + "/" + CharacterName + "Scale.png")
		self.imLayer = pygame.image.load(ResourcePath + "rooms/" + self.Startroom + "/room" + self.Startroom + "_layers.png")
		self.imWM = pygame.image.load(ResourcePath + "rooms/" + self.Startroom + "/room" + self.Startroom + "_walkmask.png")
		self.imSheet = pygame.image.load(self.ResourcePath + "characters/" + CharacterName + "/" + CharacterName + "Sheet.png")

		#This is a "hook" for allowing the main.py to attach animations to a character.
		#Display code will need to be updated to add it...
		self.Animations = dict()

		#Speaking setup
		self.TalkFont = Textify.BlitFont(ResourcePath + self.FontFile)
		self.SayString = ""
		self.TicsToTalk = 0

	
	def GoTo(self, destRoom, coords):
		self.imLayer = pygame.image.load(destRoom.ResourcePath + "rooms/" + destRoom.RoomName + "/room" + destRoom.RoomName + "_layers.png")
		self.imWM = pygame.image.load(destRoom.ResourcePath + "rooms/" + destRoom.RoomName + "/room" + destRoom.RoomName + "_walkmask.png")
		self.pos = coords
		self.x = coords[0]
		self.y = coords[1]
		self.xDest = coords[0]
		self.yDest = coords[1]
	
	def WalkTo(self, WalkX, WalkY):
		#print "X " + str(WalkX) + " Y " + str(WalkY) + " "
		
		#Set Destination
		self.xDest=WalkX
		self.yDest=WalkY

		#Set Velocity
		Mag=math.sqrt((self.xDest-self.x)*(self.xDest-self.x)+(self.yDest-self.y)*(self.yDest-self.y))
		self.xVel=-self.Speed*(self.x-self.xDest)/Mag
		self.yVel=-self.Speed*(self.y-self.yDest)/Mag
		#print ("X: "+str(self.x)+"Y:"+str(self.y))
		
	def Update(self):
		#print(self.x)
		
		Distance = ((self.xDest-self.x)*(self.xDest-self.x)+(self.yDest-self.y)*(self.yDest-self.y))
		MaskPix=self.imWM.get_at((int(self.x),int(self.y)))
		self.scale=float(MaskPix[0])/255
		if (Distance<25):
			#print("Stopping")
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
			self.WalkStep=(self.WalkStep+1)%self.WalkSteps

			if(self.yVel>3):
				self.SheetX = self.WalkStep*self.SizeX
				self.SheetY = self.WalkDownRow*self.SizeY
			if(self.yVel<-3):
				self.SheetX = self.WalkStep*self.SizeX
				self.SheetY = self.WalkUpRow*self.SizeY
			if(self.xVel>3):
				self.SheetX = self.WalkStep*self.SizeX
				self.SheetY = self.WalkRightRow*self.SizeY
			if(self.xVel<-3):
				self.SheetX = self.WalkStep*self.SizeX
				self.SheetY = self.WalkLeftRow*self.SizeY

		self.Layer=ScummPyUtils.GetIndex(self.imLayer.get_at((int(self.x),int(self.y))))
		self.pos=(int(self.x),int(self.y))
						
	def Display(self, imOutPut):
		#Spit to display
		self.imPlayer.fill((255,0,255))
		self.imPlayer.set_colorkey((255,0,255)) #probably inefficient, move to constructor if laggy?
		
		Middle = self.SizeX/2
		
		self.imPlayer.blit(self.imSheet,(-self.SheetX,-self.SheetY))
		imOutPut.blit(pygame.transform.scale(self.imPlayer,(int(self.SizeX*self.scale),int(self.SizeY*self.scale))), (self.x-int(Middle*self.scale),self.y-int(self.SizeY*self.scale)))
		if self.TicsToTalk > 0:
			self.TalkFont.BlitTextCenter(imOutPut,(self.pos[0]+self.TalkX,self.pos[1]+self.TalkY),self.SayString)
			self.TicsToTalk -= 1
		
	def SetWalkMask(self, newWalkMask):
		self.imWM.fill((0,0,0))
		self.imWM.blit(newWalkMask,(0,0))

	def Say(self, inputString = "!!!", duration = "15"):
		self.TicsToTalk = duration
		self.SayString = inputString


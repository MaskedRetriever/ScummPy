import pygame
from pygame.locals import *
import os

import ScummPyUtils

class Room:
	
	def __init__(self, ResourcePath="resources/", RoomName="002"):
		self.ResourcePath = ResourcePath
		self.RoomName = RoomName
		self.roomsFP = open(self.ResourcePath + "rooms.scd", "r")

		#Assign Special Layers
		self.imWM = pygame.image.load(self.ResourcePath + "rooms/" + RoomName + "/room" + RoomName + "_walkmask.png")
		self.imLayers = pygame.image.load(self.ResourcePath + "rooms/" + RoomName + "/room" + RoomName + "_layers.png")
		self.imHotspots = pygame.image.load(self.ResourcePath + "rooms/" + RoomName + "/room" + RoomName + "_hotspots.png")

		#Assign Visible Layers
		self.imLayers = []
		imNamesInDir = os.listdir(self.ResourcePath + "rooms/" + RoomName)
		imNamesInDir.remove("room" + RoomName + "_walkmask.png")
		imNamesInDir.remove("room" + RoomName + "_layers.png")
		imNamesInDir.remove("room" + RoomName + "_hotspots.png")

		for imName in imNamesInDir:
			self.imLayers.append(pygame.image.load(self.ResourcePath + "rooms/" + RoomName + "/" + imName))
		

		#Set up exits
		self.Exits = [Exit()]
		for line in self.roomsFP:
			if len(line)>0:
				words = line.split()
				if (len(words)==11):
					#print(words)
					if(words[2]==self.RoomName):
						self.Exits.append(Exit(int(words[4]),words[6],(int(words[8]),int(words[10]))))
						#print(words[4] + " " + words[6] + " " + words[8])
		self.roomsFP.close()

		self.Animations=dict()
	
	def Display(self, imOutPut, Characters):
		i=0
		for imLay in self.imLayers:
			imOutPut.blit(imLay,(0,0))
			for k, Character in Characters.iteritems():
				if Character.Layer == i:
					Character.Display(imOutPut)
			i+=1


	def GetExit(self, pos):
		SpotCheck = ScummPyUtils.GetIndex(self.imHotspots.get_at(pos))
		for iExit in self.Exits:
			if SpotCheck == iExit.spotnum:
				return iExit
		return Exit() #Dummy Exit to indicate failure
		
class Exit:
	def __init__(self,spotnum=0,roomdest='NOEXIT',coords=(0,0)):
		self.spotnum=spotnum
		self.roomdest=roomdest
		self.coords=coords

	def Printout(self):
		print "Spotnum=" + str(self.spotnum) + " Roomdest=" + self.roomdest + " Coords="+ str(self.coords)
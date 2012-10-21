#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

import ScummPyRoom
import ScummPyUtils
import ScummPyCharacter
import ScummPyHud

class Game:
 def __init__(self,ResourcePath="resources/",StartRoom="002"):
	self.ResourcePath=ResourcePath
	self.PlayerChar = 'bozo'

	#Load GUI Mask
	self.imGUIMask = pygame.image.load(ResourcePath + "/layout.png")

	#Load Rooms
	self.rooms = dict()
	for roomname in os.listdir(ResourcePath + "rooms"):
		self.rooms[roomname]=ScummPyRoom.Room(self.ResourcePath,roomname)
	
	self.RoomSelect=StartRoom

	self.characters = dict()
	for charname in os.listdir(ResourcePath + "characters"):
		self.characters[charname]=ScummPyCharacter.Character(self.ResourcePath,charname)

	

	settingsFP = open(self.ResourcePath + "gamesettings.scd", "r")
	for line in settingsFP:
		if len(line)>0:
			words = line.split()
			if words[0] == 'GUIOffsetX':
				self.GUIOffsetX = int(words[1])
			if words[0] == 'GUIOffsetY':
				self.GUIOffsetY = int(words[1])
			if words[0] == 'PlayerChar':
				self.PlayerChar = words[1]
	settingsFP.close()		


	self.RoomSelect=self.characters[self.PlayerChar].Startroom


	#self.characters = []
	#self.characters.append(ScummPyCharacter.Character(self.ResourcePath))
	
	self.GameGUI = ScummPyHud.GUI(ResourcePath, (self.GUIOffsetX,self.GUIOffsetY))
 
 def Display(self, surf):
	self.rooms[self.RoomSelect].Display(surf,self.characters)
	self.GameGUI.Display(surf)
	
 def Update(self):
	self.characters[self.PlayerChar].Update()
	ExitCheck = self.rooms[self.RoomSelect].GetExit(self.characters[self.PlayerChar].pos)
	Destination = ExitCheck.roomdest
	if(Destination != 'NOEXIT'):
	 print(ExitCheck.roomdest)
	 self.RoomSelect=ExitCheck.roomdest
	 self.characters[self.PlayerChar].GoTo(self.rooms[self.RoomSelect],ExitCheck.coords)
	

 def Click(self, pos):
 	point = ScummPyUtils.GetIndex(self.imGUIMask.get_at(pos))
 	if point == 1:
 		self.characters[self.PlayerChar].WalkTo(pos[0],pos[1])
 		#print pos
 	else:
 		self.GameGUI.GUIText = "Spot Clicked: " + str(point)
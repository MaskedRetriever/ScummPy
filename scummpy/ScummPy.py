#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

import ScummPyRoom
import ScummPyUtils
import ScummPyCharacter
import ScummPyHud
import ScummPyAnimation
import ScummPyEvent
import Textify

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

		self.DebugDisplay = False
	
		#Command Queue
		self.Commands = []

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
				if words[0] == 'DebugFont':
					self.FontFile = words[1]
		settingsFP.close()      
		self.DebugFont = Textify.BlitFont(ResourcePath, self.FontFile)

		self.RoomSelect=self.characters[self.PlayerChar].Startroom
	
	
		#self.characters = []
		#self.characters.append(ScummPyCharacter.Character(self.ResourcePath))
		
		self.GameGUI = ScummPyHud.GUI(ResourcePath, (self.GUIOffsetX,self.GUIOffsetY))
		
	def Display(self, surf):
		self.rooms[self.RoomSelect].Display(surf,self.characters)
		self.GameGUI.Display(surf)

		if self.DebugDisplay:
			DebugString1 = "X: " + str(int(self.characters[self.PlayerChar].x)) 
			DebugString1 += " Y: " + str(int(self.characters[self.PlayerChar].y))
			self.DebugFont.BlitText(surf,(1,1),DebugString1)
			self.DebugFont.BlitText(surf,(1,11),self.GameGUI.State)
			#surf.blit(self.characters[self.PlayerChar].imSheet,(200,0),self.characters[self.PlayerChar].blitRect)

		
	def Update(self):
		self.characters[self.PlayerChar].Update()
		ExitCheck = self.rooms[self.RoomSelect].GetExit(self.characters[self.PlayerChar].pos)
		Destination = ExitCheck.roomdest
		if(Destination != 'NOEXIT'):
			print(ExitCheck.roomdest)
			self.RoomSelect=ExitCheck.roomdest
			self.characters[self.PlayerChar].GoTo(self.rooms[self.RoomSelect],ExitCheck.coords)
			self.characters[self.PlayerChar].Update()
			self.GameGUI.GUIText = ""
		
	
	def Click(self, pos):
		point = ScummPyUtils.GetIndex(self.imGUIMask.get_at(pos))
		if point == 1:
			RoomPoint = ScummPyUtils.GetIndex(self.rooms[self.RoomSelect].imHotspots.get_at(pos))
			if self.GameGUI.State == "inactive":
				self.characters[self.PlayerChar].WalkTo(pos[0],pos[1])
			else:
				if RoomPoint != 0:
					self.Commands.append(ScummPyEvent.Command(self.GameGUI.State,self.rooms[self.RoomSelect].HotSpots[RoomPoint]))
				self.GameGUI.State = "inactive"

		else:
			if point in self.GameGUI.Actions:
				self.GameGUI.GUIText = self.GameGUI.Actions[point]
				self.GameGUI.State = self.GameGUI.Actions[point]
			if point in self.GameGUI.TwoNounActions:
				self.GameGUI.GUIText = self.GameGUI.TwoNounActions[point]

	def MouseOver(self,pos):
		GUIpoint = ScummPyUtils.GetIndex(self.imGUIMask.get_at(pos))
		if GUIpoint == 1:
			RoomPoint = ScummPyUtils.GetIndex(self.rooms[self.RoomSelect].imHotspots.get_at(pos))
			if self.GameGUI.State == "inactive":
				if RoomPoint in self.rooms[self.RoomSelect].HotSpots:
					self.GameGUI.GUIText = self.rooms[self.RoomSelect].HotSpots[RoomPoint]
				else:
					self.GameGUI.GUIText = ""
			else:
				if RoomPoint in self.rooms[self.RoomSelect].HotSpots:
					self.GameGUI.GUIText = self.GameGUI.State + " " + self.rooms[self.RoomSelect].HotSpots[RoomPoint]
				else:
					self.GameGUI.GUIText = self.GameGUI.State

		else:
			if GUIpoint in self.GameGUI.Actions:
				self.GameGUI.GUIText = self.GameGUI.Actions[GUIpoint]

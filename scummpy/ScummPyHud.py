#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

import Textify

class GUI:
	def __init__(self, ResourcePath = "resources/", GUIOffset = (0,0)):
		self.GUIText = ""
		#self.imGUI = pygame.transform.scale(pygame.image.load("resources/gui_new_comp.png"),(320,75))
		self.imGUI = pygame.image.load(ResourcePath + "GUI.png")
		self.imGUI.set_colorkey((255,0,255))
		self.Arial = Textify.BlitFont(ResourcePath, "font_1")
		self.State = "inactive"
		self.GUIOffset = GUIOffset

		self.Actions = dict()
		self.TwoNounActions = dict()

		settingsFP = open(ResourcePath + "gui.scd", "r")
		for line in settingsFP:
			if len(line)>0:
				words = line.split()
				if words[0] == 'Action':
					self.Actions[int(words[1])]=words[2]
				if words[0] == 'Action2':
					self.TwoNounActions[int(words[1])]=words[2]
		settingsFP.close()     

	
	def Display(self, imDest):		
		imDest.blit(self.imGUI,self.GUIOffset)
		self.Arial.BlitTextCenter(imDest,(160,126),self.GUIText)
		
	def OverSpot(self, spotnum, roomnum):
		for spot in self.Spots:
			if (roomnum==spot.roomnum) & (spotnum==spot.spotnum):
				self.GUIText = self.State + " " + spot.sName
		

#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *

import Textify

class GUI:
	def __init__(self, ResourcePath = "resources/", GUIOffset = (0,0)):
		self.GUIText = "Use existential angst with gophers"
		#self.imGUI = pygame.transform.scale(pygame.image.load("resources/gui_new_comp.png"),(320,75))
		self.imGUI = pygame.image.load(ResourcePath + "GUI.png")
		self.imGUI.set_colorkey((255,0,255))
		self.Arial = Textify.BlitFont(ResourcePath + "font_1.png")
		self.State = "Walk to"
		self.GUIOffset = GUIOffset
	
	def Display(self, imDest):		
		imDest.blit(self.imGUI,self.GUIOffset)
		self.Arial.BlitTextCenter(imDest,(160,126),self.GUIText)
		
	def OverSpot(self, spotnum, roomnum):
		for spot in self.Spots:
			if (roomnum==spot.roomnum) & (spotnum==spot.spotnum):
				self.GUIText = self.State + " " + spot.sName
		

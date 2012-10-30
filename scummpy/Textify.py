#!/usr/bin/env python

import sys, os, pygame
from pygame.locals import *
#814x32
class BlitFont:
	
	def __init__(self, FontPath="resources/", FontName="font_1"):
		#self.FontPlate = pygame.transform.scale(pygame.image.load("font_1.png"),(814*2,32*2))
		self.FontPlate = pygame.image.load(FontPath+FontName + ".png")
		self.XCaps = 8
		self.YCaps = 0
		self.Hs = 10
		self.FontPlate.set_colorkey((255,0,255))
		
		settingsFP = open(FontPath + FontName + ".scd", "r")
		for line in settingsFP:
			if len(line)>0:
				words = line.split()
				if words[0] == 'Indicator':
					self.Indicator = int(words[1])
				if words[0] == 'YVal':
					self.YCaps = int(words[1])
				if words[0] == 'Height':
					self.Hs = int(words[1])
				if words[0] == 'Spacing':
					self.FontFile = int(words[1])
		settingsFP.close()    

		self.LetterX=[-1]
		self.LetterXE=[-1]
		for xv in range(self.FontPlate.get_width()):
			if(self.FontPlate.get_at((xv,self.Indicator))==(0,255,0)):
				self.LetterX.append(xv)
			if(self.FontPlate.get_at((xv,self.Indicator))==(255,0,0)):
				self.LetterXE.append(xv)
		#print self.LetterX
		#print self.LetterXE

		
	def BlitText(self, imDest, xyDest, text):
		#demo
		cursor=0;
		
		for C in text:
			cha=ord(C)
			#print(cha)
			if cha == 32:
				cursor=cursor+4
			else:
				#charwidth=(self.LetterX[cha-32]-self.LetterX[cha-33])
				charwidth=self.LetterXE[cha-32]-self.LetterX[cha-33]
				imDest.blit(self.FontPlate,(xyDest[0]+cursor,xyDest[1]),Rect(self.LetterX[cha-33],self.YCaps,charwidth,self.Hs))
				cursor=cursor+charwidth

	def BlitTextCenter(self, imDest, xyDest, text):
		#demo
		cursor=0;
		imTray=pygame.Surface((320,40))
		imTray.fill((255,0,255))
		imTray.set_colorkey((255,0,255))
		
		for C in text:
			cha=ord(C)
			#print(cha)
			if cha == 32:
				cursor=cursor+4
			else:
				#charwidth=(self.LetterX[cha-32]-self.LetterX[cha-33])
				charwidth=self.LetterXE[cha-32]-self.LetterX[cha-33]
				imTray.blit(self.FontPlate,(cursor,0),Rect(self.LetterX[cha-33],self.YCaps,charwidth,self.Hs))
				cursor=cursor+charwidth
		imDest.blit(imTray,(xyDest[0]-(cursor/2),xyDest[1]))		
		
#In order, now:
# !"#$%&'()*+,-./0123456789:;<=>?
#@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
#`abcdefghijklmnopqrstuvwxyz{|}~		
